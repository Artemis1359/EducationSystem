from django.contrib import admin

from products.models import Group, Lesson, Product, StudentGroup, UserProduct


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product')
    list_filter = ('name', 'product')
    search_fields = ('id', 'name', 'product')
    empty_value_display = '-пусто-'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'name', 'link')
    list_filter = ('product', 'name', 'link')
    search_fields = ('id', 'product', 'name', 'link')
    empty_value_display = '-пусто-'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name', 'date', 'price')
    list_filter = ('author', 'name', 'date', 'price')
    search_fields = ('id', 'author', 'name', 'date', 'price')
    empty_value_display = '-пусто-'


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('student', 'group',)
    list_filter = ('student', 'group',)
    search_fields = ('student', 'group',)
    empty_value_display = '-пусто-'


@admin.register(UserProduct)
class UserProductAdmin(admin.ModelAdmin):
    list_display = ('client', 'product',)
    list_filter = ('client', 'product',)
    search_fields = ('client', 'product',)
    empty_value_display = '-пусто-'
