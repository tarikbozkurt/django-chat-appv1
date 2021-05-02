from django.urls import path
from django.conf.urls import include

from .views import RoomView

urlpatterns = [

    path('hoe',RoomView.as_view()),
]