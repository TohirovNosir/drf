from django.urls import path, include


app_name = 'main'


urlpatterns = [
    path('api/', include('apps.main.api.urls', namespace='api')),

]