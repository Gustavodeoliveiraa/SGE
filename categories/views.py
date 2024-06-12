from django.views.generic import (
    ListView
)
import models


class CategoriesListView(ListView):
    models = models.Category
    template_name = 'categories_list.html'
    context_object_name = 'brands'

    def get_queryset(self):
        queryset = super().get_queryset()
        name_category = self.request.GET.get('name')

        if name_category:
            queryset = queryset.filter(name__icontains=name_category)

        return queryset
