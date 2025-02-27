from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('list_books/one_book/', views.viewbook, name="books.one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('html5/links',views.links, name = "books.html5"),
 path('html5/text/formatting', views.formatting, name='formatting'),
 path('html5/listing', views.listing, name='listing'),
 path('html5/tables', views.tables, name='tables'),
]

