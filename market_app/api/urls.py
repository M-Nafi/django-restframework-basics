from django.urls import path
from .views import markets_view, market_single_view

urlpatterns = [  
    path('', markets_view),
    path('<int:pk>/', market_single_view),
]