from django.urls import path
from .views import markets_view, market_single_view, sellers_view, seller_single_view, products_view, product_single_view

urlpatterns = [
    path('market/', markets_view),
    path('market/<int:pk>/', market_single_view),
    path('seller/', sellers_view),
    path('seller/<int:pk>/', seller_single_view, name='seller_single'),
    path('product/', products_view),
    path('product/<int:pk>/', product_single_view),
]