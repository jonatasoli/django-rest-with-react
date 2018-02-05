from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('login', views.LoginViewSet, base_name='login')
router.register('listweek', views.WeekViewSet, base_name='week')
router.register('listdone', views.DoneViewSet, base_name='done')
router.register('listlate', views.LateViewSet, base_name='late')

urlpatterns = [
    url(r'', include(router.urls))
]
