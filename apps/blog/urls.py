from django.urls import path, include

app_name = 'blog'

urlpatterns = [
    path('api/', include('apps.blog.api.urls', namespace='api'))

]
