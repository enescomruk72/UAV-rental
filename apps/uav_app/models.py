from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from decimal import Decimal
# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    founded_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class AircraftCategory(models.Model):
    name = models.CharField(max_length=55, unique=True)
    description = models.TextField(editable=False, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('id',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    
class UCAV(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='ucav_brand')
    aircraft_category = models.ForeignKey(AircraftCategory, on_delete=models.CASCADE, related_name='ucav_category')
    max_takeoff_weight = models.FloatField(blank=True, null=True)  # ton
    max_speed_mach = models.FloatField(blank=True, null=True)  # mach
    max_altitude_feet = models.IntegerField(blank=True, null=True) # ft
    autonomous_takeoff_and_landing = models.BooleanField(default=False)
    unit_rental_price = models.DecimalField(max_digits=10, decimal_places=2, default=1000)



    def __str__(self) -> str:
        return f'{self.name} | {self.aircraft_category}, {self.model}'

    class Meta:
        ordering = ('id', 'name',)
        verbose_name = 'UCAV'
        verbose_name_plural = 'UCAVs'


class Rental(models.Model):
    ucav = models.ForeignKey(UCAV, on_delete=models.CASCADE, related_name='rental_ucav')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rental_user')
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.ucav.name} rented by {self.user}"

    def calculate_price(self):
        if self.start_date and self.end_date:
            duration = self.end_date - self.start_date
            unit_rental_price = self.ucav.unit_rental_price
            total_price = duration.days * unit_rental_price
            self.price = Decimal(total_price)
        else:
            self.price = None

    def save(self, *args, **kwargs):
        self.calculate_price()
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = (
            'start_date',
            'end_date',
            'price',
        )
        verbose_name = 'Rental'
        verbose_name_plural = 'Rentals'