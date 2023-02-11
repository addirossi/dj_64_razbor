from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from main.models import Book


class BooksList(View):
    def get(self, request):
        queryset = Book.objects.all()
        # print(request.GET)
        year = request.GET.get('year', 0)
        if year:
            queryset = queryset.filter(year__lte=year)
        q = request.GET.get('q', '')
        if q:
            queryset = queryset.filter(title__icontains=q)
        return render(request, 'main/list.html', {'books': queryset})


class BookDetails(View):
    def get(self, request, book_id):
        ...

# def book_details(request, book_id):
#     ...


class BookDetails(DetailView):
    queryset = Book.objects.all()
    template_name = '...'
