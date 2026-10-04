from rest_framework import serializers
from .models import MenuItem, Booking


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id',
            'first_name',
            'reservation_date',
            'reservation_slot'
        ]