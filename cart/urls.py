from django.urls import path

urlpatterns = [
    path('view-my-cart/', lambda r: None, name='cart-view'),
    path('add-item-to-cart/', lambda r: None, name='cart-add'),
]
