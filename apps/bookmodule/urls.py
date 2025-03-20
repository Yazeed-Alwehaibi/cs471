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
 path('search/', views.search, name='search'),
 path('simple/query', views.simple_query, name='simpleQuery'),
 path('complex/query', views.complex_query, name='complexQuery'),
 path('lab8/task1', views.task1, name='task1'),
 path('lab8/task2', views.task2, name='task2'),
 path('lab8/task3', views.task3, name='task3'),
 path('lab8/task4', views.task4, name='task4'),
 path('lab8/task5', views.task5, name='task5'),
 path('lab8/task7', views.task7, name='task7'),
]

