from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarketSerializer, ProductDetailSerializer, SellerSerializer, MarketHyperlinkedSerializer
from market_app.models import Market, Seller, Product
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics


class MarketsView (generics.ListCreateAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
       
class MarketDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

class SellerOfMarketList(generics.ListAPIView):
    serializer_class = SellerSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        market = Market.objects.get(pk = pk)
        return market.sellers.all()


@api_view(['GET', 'POST'])
def sellers_view(request):

    if request.method == 'GET':
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True, context={'request': request})
        return Response(serializer.data)    
    
    if request.method == 'POST':
       serializer = SellerSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       else:
           return Response(serializer.errors)


@api_view(['GET', 'DELETE', 'PUT'])
def seller_single_view(request, pk):

    if request.method == 'GET':
        seller = Seller.objects.get(pk=pk)
        serializer = SellerSerializer(seller, context={'request': request})
        return Response(serializer.data)   

    if request.method == 'PUT':
        seller = Seller.objects.get(pk=pk)
        serializer = SellerSerializer(seller, data=request.data, partial=True)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        seller = Seller.objects.get(pk=pk)
        serializer = SellerSerializer(seller)
        seller.delete()
        return Response(serializer.data)   
    


@api_view(['GET', 'POST'])
def products_view(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)    
    
    if request.method == 'POST':
       serializer = ProductDetailSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       else:
           return Response(serializer.errors)
       
       
@api_view(['GET', 'DELETE', 'PUT'])
def product_single_view(request, pk):

    if request.method == 'GET':
        products = Product.objects.get(pk=pk)
        serializer = ProductDetailSerializer(products)
        return Response(serializer.data)   

    if request.method == 'PUT':
        product = Product.objects.get(pk=pk)
        serializer = ProductDetailSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method == 'DELETE':
        product = Product.objects.get(pk=pk)
        serializer = ProductDetailSerializer(product)
        product.delete()
        return Response(serializer.data)   
    