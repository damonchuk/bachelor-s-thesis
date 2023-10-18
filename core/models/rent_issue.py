from django.db import models

__all__ = ['RentIssue', 'RentIssueForm']

from django.forms import ModelForm


class RentIssue(models.Model):

    RENT_TYPE_HOUR = 1
    RENT_TYPE_DAY = 2
    RENT_TYPE_LEASING = 3

    RENT_TYPE_CHOICES = (
        (RENT_TYPE_HOUR, 'Per Hour Rate'),
        (RENT_TYPE_DAY, 'Per Day Rate'),
        (RENT_TYPE_LEASING, 'Leasing'),
    )

    car = models.ForeignKey(
        'core.Car',
        verbose_name='Car',
        related_name='rent_issue',
        on_delete=models.CASCADE
    )

    rent_type = models.PositiveSmallIntegerField('Rent Type', choices=RENT_TYPE_CHOICES, default=RENT_TYPE_HOUR)

    pick_up_location = models.CharField(
        verbose_name='Pick-Up Location',
        max_length=128,
        null=True,
        blank=True
    )
    drop_off_location = models.CharField(
        verbose_name='Drop-Off Location',
        max_length=128,
        null=True,
        blank=True
    )

    pick_up_date = models.DateTimeField('Pick_Up Date')
    drop_off_date = models.DateTimeField('Drop-Off Date')

    pick_up_time = models.CharField(
        verbose_name='Pick-Up Time',
        max_length=128,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Issue #{self.pk} - {self.car.name}'

    class Meta:
        verbose_name = 'Rent Issue'
        verbose_name_plural = 'Rent Issues'


class RentIssueForm(ModelForm):
    class Meta:
        model = RentIssue
        fields = '__all__'
