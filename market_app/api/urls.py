from django.urls import include, path
from .views import ProductViewSet, MarketsView, MarketDetails, SellerOfMarketList, SellerView, SellerDetailsView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketDetails.as_view(), name='market-detail'),
    path('market/<int:pk>/sellers/', SellerOfMarketList.as_view()),
    path('seller/', SellerView.as_view()),
    path('seller/<int:pk>/', SellerDetailsView.as_view(), name='seller-detail'),
]