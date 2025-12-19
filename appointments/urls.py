from django.urls import path

urlpatterns = [
    path('book-session/', lambda r: None, name='appointment-book'),
    path('my-appointments/', lambda r: None, name='appointment-list'),
]
