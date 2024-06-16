from django.urls import path
from .views import (
        SupplierListView, SupplierCreateView, SupplierUpdateView,
        SupplierDetailView, SupplierDeleteView
    )

urlpatterns = [
    path(
        'supplier/list/', SupplierListView.as_view(), name='supplier_list'
    ),
    path(
        'supplier/create/', SupplierCreateView.as_view(),
        name='supplier_create'
    ),
    path(
        'supplier/<int:pk>/update', SupplierUpdateView.as_view(),
        name='supplier_update'
    ),
    path(
        'supplier/<int:pk>/detail', SupplierDetailView.as_view(),
        name='supplier_detail'
    ),
    path(
        'supplier/<int:pk>/delete', SupplierDeleteView.as_view(),
        name='supplier_delete'
    ),
]
