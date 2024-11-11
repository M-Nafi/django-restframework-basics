from rest_framework import serializers
from market_app.models import Market, Seller, Product


class MarketSerializer(serializers.ModelSerializer):

    sellers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Market
        fields = '__all__'
        # exclude = [] macht das selbe wie '__all__'!

    def validate_name(self, value):
        errors = []

        if 'X' in value:
            errors.append('no X in location')
        if 'Y' in value:
            errors.append('no Y in location')
        if errors:
            raise serializers.ValidationError(errors)

        return value


class MarketHyperlinkedSerializer(MarketSerializer, serializers.HyperlinkedModelSerializer):


    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    # sellers = None  # hiermit kann das in der gesamtansicht nicht anzeigen !
    class Meta:
        model = Market
        fields = ['id', 'url', 'name', 'location', 'description', 'net_worth']
        # exclude = ['net_worth']  # hiermit kann das in der gesamtansicht nicht anzeigen !


class SellerSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        many=True,
        write_only=True,
        source='markets'
    )

    market_count = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = ["id", "name", "market_ids", "market_count", "markets", "contact_info"]

    def get_market_count(self, obj):
        return obj.markets.count()


# alte funktion sellerdetailsserializer!
# class SellerDetailSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     contact_info = serializers.CharField()
#     markets = MarketSerializer(many=True, read_only=True)

# class SellerDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Seller
#         fields = '__all__'
 
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# das ist die variante vom serializer ohne "model" diese vriante 
# wird wenig genutzt, aber dennoch kann es vorkommen. 

# class ProductDetailSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     description = serializers.CharField()
#     market = serializers.IntegerField(write_only=True)
#     seller = serializers.IntegerField(write_only=True)  # Neues Feld für Seller ID
#     price = serializers.DecimalField(max_digits=50, decimal_places=2)

#     def validate_market(self, value):
#         if not Market.objects.filter(id=value).exists():
#             raise serializers.ValidationError("Invalid market id")
#         return value
    
#     def validate_seller(self, value):
#         if not Seller.objects.filter(id=value).exists():
#             raise serializers.ValidationError("Invalid seller id")
#         return value
    
#     def create(self, validated_data):
#         market_id = validated_data.pop('market')
#         seller_id = validated_data.pop('seller')
#         product = Product.objects.create(market_id=market_id, seller_id=seller_id, **validated_data)
#         return product
    
#     def update(self,instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.market = validated_data.get('market', instance.market)
#         instance.seller = validated_data.get('seller', instance.seller)
#         instance.save()
#         return instance