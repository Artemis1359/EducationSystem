from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Доступ только пользователея с ролью 'Admin', либо только чтение."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_staff


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
