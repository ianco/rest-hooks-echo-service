### urls.py ###

from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'webhooks', views.HookViewSet, 'webhook')

urlpatterns = router.urls
urlpatterns.append(path('echo', views.echo_view, name='echo'))
