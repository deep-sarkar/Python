from django.urls import path
from poll.views import *

urlpatterns = [
   path('', index, name='pools_list'),
   path('<int:id>/details/', details, name="poll_details"),
   path('<int:id>/', poll, name="single_poll")
]