from django.urls import include, path
from .views import ProductViewSet, MarketsView, MarketDetails, SellerOfMarketList, sellers_view, seller_single_view
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketDetails.as_view(), name='market-detail'),
    path('market/<int:pk>/sellers/', SellerOfMarketList.as_view()),
    path('seller/', sellers_view),
    path('seller/<int:pk>/', seller_single_view, name='seller-detail'),
]