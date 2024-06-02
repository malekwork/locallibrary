from django.urls import path
from .views import HomePageView, BookListView, BookDetailView, AuthorListView, LoanedBooksByUserListView,\
    renew_book_librarian

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('book/', BookListView.as_view(), name='book_list'),
    path('book/<pk>/', BookDetailView.as_view(), name='book_detail'),
    path('author/', AuthorListView.as_view(), name='author_list'),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/<pk>/renew/', renew_book_librarian, name='renew-book-librarian')
]
