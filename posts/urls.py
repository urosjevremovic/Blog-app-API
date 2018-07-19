from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet, UserViewSet


router = DefaultRouter()
router.register('users', UserViewSet, base_name='users')
router.register('posts', PostViewSet, base_name='posts')

urlpatterns = router.urls