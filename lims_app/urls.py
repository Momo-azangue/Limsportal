from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home),
    path('home', home),
    path('readers', readers_tab),
    path('mybag', mybag),
    path('returns', returns),
    path('shopping', shopping),
    path('save', save_student),
    path('readers/add', save_reader),
    path('books', books_tab),
    path('books/add', save_book, name='save_book'),
    path('book/<int:book_id>/add-to-bag/', add_to_bag, name='add_to_bag'),
    path('book/<int:book_id>/remove-from-bag/', remove_from_bag, name='remove_from_bag'),
    path('mybag/', mybag, name='mybag'),
]
