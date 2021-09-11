from django.urls import include, path

urlpatterns = [
    path('dummies/', include('apps.dummies.urls')),
    path('auth/', include('apps.authentication.urls')),
    path('users/', include('apps.users.urls')),
    path('notifications/', include('apps.notifications.urls')),
]
