from rest_framework.routers import SimpleRouter

from .views import DummiesViewSet

router = SimpleRouter()

router.register('', DummiesViewSet, basename='dummies')

urlpatterns = router.urls
