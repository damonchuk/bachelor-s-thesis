from django.db import models

__all__ = ['Car', 'CarComment', 'CarCommentForm']

from django.forms import ModelForm


class Car(models.Model):
    TRANSMISSION_MANUAL = 1
    TRANSMISSION_AUTOMAT = 2

    TRANSMISSION_CHOICES = (
        (TRANSMISSION_MANUAL, 'Manual'),
        (TRANSMISSION_AUTOMAT, 'Automat'),
    )

    FUEL_PETROL = 1
    FUEL_DIESEL = 2

    FUEL_CHOICES = (
        (FUEL_PETROL, 'Petrol'),
        (FUEL_DIESEL, 'Diesel'),
    )

    name = models.CharField(verbose_name='Name', max_length=1024)

    photo = models.ImageField(
        verbose_name='Photo',
        upload_to='cars_photo',
        blank=True,
        null=True,
    )

    cost_hour = models.DecimalField(
        'Cost Hour',
        max_digits=42,
        decimal_places=2,
        default=0
    )
    cost_day = models.DecimalField(
        'Per Day Rate',
        max_digits=42,
        decimal_places=2,
        default=0
    )
    leasing = models.DecimalField(
        'Leasing',
        max_digits=42,
        decimal_places=2,
        default=0
    )

    mileage = models.CharField(
        verbose_name='Mileage',
        max_length=64,
        null=True,
        blank=True
    )

    transmission = models.PositiveSmallIntegerField('Transmission', choices=TRANSMISSION_CHOICES, default=TRANSMISSION_MANUAL)

    seats = models.CharField(
        verbose_name='Seats',
        max_length=64,
        null=True,
        blank=True
    )

    luggage = models.CharField(
        verbose_name='Luggage',
        max_length=64,
        null=True,
        blank=True
    )

    fuel = models.PositiveSmallIntegerField('Fuel', choices=FUEL_CHOICES, default=FUEL_PETROL)

    description = models.TextField(
        verbose_name='Description',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class CarComment(models.Model):
    car = models.ForeignKey(
        'core.Car',
        verbose_name='Car',
        related_name='comments',
        on_delete=models.CASCADE
    )

    name = models.CharField(
        verbose_name='Name',
        max_length=128,
    )
    email = models.CharField(
        verbose_name='Email',
        max_length=128,
    )

    message = models.TextField(
        verbose_name='Message',
    )

    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Car Comment'
        verbose_name_plural = 'Car Comments'


class CarCommentForm(ModelForm):
    class Meta:
        model = CarComment
        fields = ['car', 'name', 'email', 'message']

