from django.urls import path
from .views import *


urlpatterns = [
    path('get_messages', MessagesListView.as_view(), name='get_messages'),
    path('mark_read', MessageUpdateView.as_view(), name='mark_read_message'),
]
