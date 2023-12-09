from rest_framework import serializers

from apps.uav_app.models import Brand, AircraftCategory, UCAV, Rental



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'



class AircraftCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AircraftCategory
        fields = '__all__'



class UCAVSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)
    category_name = serializers.CharField(source='aircraft_category.get_name_display', read_only=True)

    class Meta:
        model = UCAV
        fields = '__all__'
        read_only_fields = ('image',)  


class RentalSerializer(serializers.ModelSerializer):
    rental_ucav = serializers.HyperlinkedRelatedField( read_only=True, view_name='rental_ucav',)
    rental_user = serializers.HyperlinkedRelatedField( read_only=True, view_name='rental_user',)
    ucav_name = serializers.CharField(source='ucav.name', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)
    duration = serializers.DurationField(read_only=True)


    class Meta:
        model = Rental
        fields = '__all__'
        read_only_fields = ('duration', 'ucav_name', 'user_username', 'price')  # Süre ve isimler otomatik olacak




