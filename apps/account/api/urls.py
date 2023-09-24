from django.urls import path, include

from .views import Login

app_name = 'api'

urlpatterns = [
    path('token/', Login.as_view(), name='token'),

    path('v1/', include('apps.account.api.v1.urls', namespace='v1')),
]