from rest_framework import routers

from .views import UsersViewSet

router = routers.SimpleRouter()

router.register('', UsersViewSet, basename='users')

urlpatterns = router.urls
