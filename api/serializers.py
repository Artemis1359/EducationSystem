from rest_framework import serializers

from products.models import Group, Lesson, Product, StudentGroup, UserProduct


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'product', 'name', 'link',)

    def to_representation(self, instance):
        user = self.context['request'].user
        purchased_products_ids = UserProduct.objects.filter(client=user).values_list('product_id', flat=True)
        if instance.product_id in purchased_products_ids:
            return super().to_representation(instance)
        return None


class ProductSerializer(serializers.ModelSerializer):
    purchases = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'author', 'name', 'date', 'price', 'purchases', 'lessons',)

    def get_purchases(self, obj):
        return obj.user_products.count()


class ShortProductSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('id', 'author', 'name', 'date', 'price', 'lessons')

    def get_lessons(self, obj):
        return obj.lessons.count()


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ('student',)


class GroupSerializer(serializers.ModelSerializer):

    students = StudentGroupSerializer(many=True, source='student_groups')

    class Meta:
        model = Group
        fields = ('id', 'name', 'product', 'students',)

class ShortGroupSerializer(serializers.ModelSerializer):
    students = StudentGroupSerializer(many=True, source='student_groups')

    class Meta:
        model = Group
        fields = ('name', 'students',)


class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = ('id', 'product', 'client',)
