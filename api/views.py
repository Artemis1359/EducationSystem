from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api.group_algo import add_user_to_group
from api.permissions import IsAdminOrReadOnly, IsAuthor
from api.serializers import (
    GroupSerializer,
    LessonSerializer,
    ProductSerializer,
    ShortGroupSerializer,
    ShortProductSerializer,
    UserProductSerializer
)
from products.models import Group, Lesson, Product, UserProduct


class GroupViewSet(viewsets.ModelViewSet):
    """Вьюсет для класса Group."""
    permission_classes = (IsAuthenticated, IsAdminOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return Group.objects.filter(student_groups__student=user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ShortGroupSerializer
        return GroupSerializer


class LessonViewSet(viewsets.ModelViewSet):
    """Вьюсет для класса Lesson."""
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated, IsAuthor)

    def get_queryset(self):
        user = self.request.user
        purchased_products_ids = (UserProduct.objects.filter(
            client=user
        ).values_list('product_id', flat=True))
        queryset = Lesson.objects.filter(product_id__in=purchased_products_ids)
        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    """Вьюсет для класса Product."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductSerializer
        return ShortProductSerializer

    @action(detail=True, methods=['post'])
    def purchase(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = UserProductSerializer(
            data={
                'client': request.user.id,
                'product': pk
            },
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        if UserProduct.objects.filter(
                client=request.user,
                product=product
        ).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        UserProduct.objects.create(
            client=request.user,
            product=product)
        add_user_to_group(request.user, product)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
