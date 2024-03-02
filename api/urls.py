from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import GroupViewSet, LessonViewSet, ProductViewSet

router_v1 = DefaultRouter()
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register('lessons', LessonViewSet, basename='lessons')
router_v1.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]