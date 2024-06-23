from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from .forms import ProductForm
from django.urls import reverse_lazy
from .models import Product


class ProductLIstView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        brand = self.request.GET.get('brand')
        category = self.request.GET.get('category')

        queryset = super().get_queryset()
        if title:
            queryset = Product.objects.filter(title__icontains=title)
        if serie_number:
            queryset = Product.objects.filter(
                serie_number__icontains=serie_number
            )
        if brand:
            queryset = Product.objects.filter(brand__icontains=brand)
        if category:
            queryset = Product.objects.filter(category__icontains=category)

        return queryset


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
