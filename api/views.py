from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from api.serializers import GroupSerializer, LessonSerializer, ProductSerializer, StudentGroupSerializer, UserProductSerializer
from products.models import Group, Lesson, Product, UserProduct


class GroupViewSet(viewsets.ModelViewSet):
    """Вьюсет для класса Group."""
    queryset = Group.objects.all()
    permission_classes = []

    def get_serializer_class(self):
        if self.request.method == 'retrieve':
            return StudentGroupSerializer
        return GroupSerializer


class LessonViewSet(viewsets.ModelViewSet):
    """Вьюсет для класса Lesson."""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = []


class ProductViewSet(viewsets.ModelViewSet):
    """Вьюсет для класса Product."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []

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
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
