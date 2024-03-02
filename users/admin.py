from django.contrib import admin

# Register your models here.
from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
    )
    search_fields = ('username','first_name','last_name', 'email',)
    list_filter = (
        'username',
        'email',
    )
    empty_value_display = '-пусто-'

