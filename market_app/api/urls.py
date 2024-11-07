from django.urls import path
from .views import markets_view

urlpatterns = [  
    path('', markets_view),
]