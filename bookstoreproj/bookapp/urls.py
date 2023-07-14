from django.urls import path
from .views import BookList, BookDetail, BookCheckoutView, PaymentComplete, home, SearchResultsView, cart, add_to_cart, \
    remove_from_cart
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('book_list/', BookList.as_view(), name='books'),
    path('book_details/<int:pk>/', BookDetail.as_view(), name='details'),
    path('checkout/<int:pk>/', BookCheckoutView.as_view(), name='checkout'),
    path('complete/', PaymentComplete, name='complete'),
    path('cart/', cart, name='mycart'),
    path('cart/add/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:book_id>/', remove_from_cart, name='remove_from_cart')
]
