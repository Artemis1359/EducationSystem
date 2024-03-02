from rest_framework import serializers
from products.models import Group, Lesson, Product, StudentGroup, UserProduct


class ProductSerializer(serializers.ModelSerializer):
    purchases = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'author', 'name', 'date', 'price', 'purchases',)

    def get_purchases(self, obj):
        return obj.user_products.count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'product', 'name', 'link',)


class StudentGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ('student',)


class GroupSerializer(serializers.ModelSerializer):

    students = StudentGroupSerializer(many=True, source='student_groups')

    class Meta:
        model = Group
        fields = ('id', 'name', 'product', 'students',)




class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = ('id', 'product', 'client',)
