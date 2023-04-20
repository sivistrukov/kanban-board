from django.urls import path, include
from rest_framework import routers

from board.views import *
from board.api.views import *

app_name = 'board'

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/board/', include(router.urls)),
]
