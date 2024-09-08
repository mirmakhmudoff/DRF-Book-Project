from django.urls import path, include
from rest_framework import routers
from .views import AuthorModelView, CategoryViewSet, BookViewSet

router = routers.DefaultRouter()
router.register(r'authors', AuthorModelView)
router.register(r'categories', CategoryViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]
