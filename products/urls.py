from django.urls import path

urlpatterns = [
    path('list-products/', lambda r: None, name='product-list'),
    path('add-new-product/', lambda r: None, name='product-add'),
]
