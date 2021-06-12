from django.urls import include, path

urlpatterns = [
    path('auth/', include('apps.authentication.api.urls')),
    path('users/', include('apps.users.api.urls'))
]
