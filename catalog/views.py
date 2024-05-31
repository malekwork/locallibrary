from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


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
