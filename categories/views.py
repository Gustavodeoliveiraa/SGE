from django.views.generic import (
    ListView, CreateView, DetailView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Category
from .forms import CategoryForm


class CategoriesListView(ListView):
    model = Category
    template_name = 'cotegories_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = super().get_queryset()
        name_category = self.request.GET.get('name')

        if name_category:
            queryset = queryset.filter(name__icontains=name_category)

        return queryset


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')
