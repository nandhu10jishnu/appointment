# filters.py
import django_filters
from .models import Booking

class BookingFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='p_name', lookup_expr='icontains', label='Name')
    phone = django_filters.CharFilter(field_name='p_phone', lookup_expr='icontains', label='Phone')

    class Meta:
        model = Booking
        fields = ['p_name', 'p_phone']
