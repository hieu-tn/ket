from rest_framework import routers

from .views import AuthViewSet

router = routers.SimpleRouter()

router.register('', AuthViewSet, basename='auth')

urlpatterns = router.urls
