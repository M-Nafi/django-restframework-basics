from django.urls import path
from .views import MarketsView, MarketDetails, sellers_view, seller_single_view, products_view, product_single_view

urlpatterns = [
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketDetails.as_view(), name='market-detail'),
    path('seller/', sellers_view),
    path('seller/<int:pk>/', seller_single_view, name='seller-single'),
    path('product/', products_view),
    path('product/<int:pk>/', product_single_view),
]