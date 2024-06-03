from django.urls import path
from .views import HomePageView, BookListView, BookDetailView, AuthorListView, LoanedBooksByUserListView,\
    AuthorCreate, AuthorDelete, AuthorUpdate, renew_book_librarian, AuthorDetailView


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('book/', BookListView.as_view(), name='book_list'),
    path('book/<pk>/', BookDetailView.as_view(), name='book_detail'),
    path('author/', AuthorListView.as_view(), name='author_list'),
    path('author/create/', AuthorCreate.as_view(), name='author_create'),
    path('author/<pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('book/<pk>/renew/', renew_book_librarian, name='renew-book-librarian'),
    path('author/<pk>/update/', AuthorUpdate.as_view(), name='author_update'),
    path('author/<pk>/delete/', AuthorDelete.as_view(), name='author_delete'),

]
