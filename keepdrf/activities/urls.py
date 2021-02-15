from django.urls import include, path
from rest_framework import routers
from .views import ActivityViewSet, TagViewSet, ResponsibleViewSet


router = routers.DefaultRouter()
router.register(r'activities', ActivityViewSet)
router.register(r'tag', TagViewSet)
router.register(r'responsible', ResponsibleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
