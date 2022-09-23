from django.urls import path
from .views import *

urlpatterns = [
    path('details', UserDetail.as_view()),
    path('signup', SignupUser.as_view()),
]