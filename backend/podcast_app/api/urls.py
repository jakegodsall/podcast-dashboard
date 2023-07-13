from rest_framework.routers import SimpleRouter

from .views import AuthorViewSet

router = SimpleRouter()

router.register('author', AuthorViewSet, basename='author')

urlpatterns = []
    
urlpatterns += router.urls