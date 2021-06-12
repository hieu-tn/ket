from rest_framework import routers

from .views import AuthenticationViewSet

router = routers.SimpleRouter()

router.register('', AuthenticationViewSet, basename='auth')

urlpatterns = router.urls
