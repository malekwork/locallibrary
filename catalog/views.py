from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(generic.TemplateView):
    template_name = "catalog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_books'] = Book.objects.all().count()
        context['num_instances'] = BookInstance.objects.all().count()
        context['num_instances_available'] = BookInstance.objects.filter(status__exact='a').count()
        context['num_authors'] = Author.objects.count()
        return context


class BookListView(generic.ListView):
    model = Book
    template_name = "catalog/book_list.html"


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "catalog/book_detail.html"


class AuthorListView(generic.ListView):
    model = Author
    template_name = "catalog/author_list.html"


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
