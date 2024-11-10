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


class SellerSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        many=True,
        write_only=True,
        source='markets'
    )

    class Meta:
        model = Seller
        exclude = []


# alte funktion sellerdetailsserializer!
# class SellerDetailSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     contact_info = serializers.CharField()
#     markets = MarketSerializer(many=True, read_only=True)

class SellerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


# class SellerCreateSerializer(serializers.ModelSerializer):
#      class Meta:
#         model = Seller
#         fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
