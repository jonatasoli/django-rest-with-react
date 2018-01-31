from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('api.urls', namespace='api', app_name='api')),
]
