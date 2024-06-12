from django.urls import path
from . import views


urlpatterns = [
    path(
        'category/list/', views.CategoriesListView.as_view(),
        name='category_list'
    ),
]
