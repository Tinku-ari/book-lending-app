from django.urls import path
from . import views

urlpatterns = [
        path('people_list', views.people_list, name='people_list'),
        path('books_list', views.books_list, name='books_list'),
]

