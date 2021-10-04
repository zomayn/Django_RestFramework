from django.urls import path
from . import views

urlpatterns=[
    path('',views.apiOverview, name='api-lists'),
    path('booklist', views.booksList, name='all-books' ),
    path('bookdetails/<str:pk>/', views.booksDetail, name='book-details' ),
    path('bookcreate', views.booksCreate, name='book-create' ),
    path('bookupdate/<str:pk>/', views.booksUpdate, name='book-update' ),
    path('bookdelete/<str:pk>/', views.booksDelete, name='book-details' ),
]