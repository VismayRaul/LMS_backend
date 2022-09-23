from django.urls import path
from .views import *
urlpatterns = [
    path('books', BookList.as_view()),
    path('books/<int:pk>', BookList.as_view()),
]
