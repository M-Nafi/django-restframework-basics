from rest_framework import serializers
from market_app.models import Market, Seller, Product


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

    def validate_name(self, value):
        errors = []
        
        if 'X' in value:
            errors.append('no X in location')
        if 'Y' in value:
            errors.append('no Y in location')    
        if errors:
            raise serializers.ValidationError(errors)      
        
        return value
    
      # diese funktion ist wichtig und kann bei join verwendet werden, wenn 
    # man nicht möchte, dass etwas bestimmtes eingegeben werden soll. 
    #  
    # def validate_location(self, value):
    #     if 'X' in value:
    #         raise serializers.ValidationError('das X gehört da nicht rein!')
    #     return value

class SellerDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    contact_info = serializers.CharField()
    markets = MarketSerializer(many=True, read_only=True)


class SellerCreateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Seller
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
