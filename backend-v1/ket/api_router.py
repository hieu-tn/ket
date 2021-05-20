from django.urls import include, path

from apps.authentication.api.urls import urlpatterns as auth_urls
from apps.users.api.urls import urlpatterns as user_urls

urlpatterns = [
    path('auth/', include(auth_urls)),
    path('users/', include(user_urls))
]
