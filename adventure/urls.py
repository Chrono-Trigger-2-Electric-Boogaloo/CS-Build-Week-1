from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('unlock_basement', api.unlock_basement)
    url('unlock_door', api.unlock_door)
]