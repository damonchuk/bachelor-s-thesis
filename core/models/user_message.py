from django.db import models

__all__ = ['UserMessage', 'UserMessageForm']

from django.forms import ModelForm


class UserMessage(models.Model):

    name = models.CharField(
        verbose_name='Name',
        max_length=128,
    )
    email = models.CharField(
        verbose_name='Email',
        max_length=128,
    )

    theme = models.CharField(
        verbose_name='Theme',
        max_length=128,
    )

    message = models.TextField(
        verbose_name='Message',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Message #{self.pk} - {self.name}'

    class Meta:
        verbose_name = 'User Message'
        verbose_name_plural = 'UserMessages'


class UserMessageForm(ModelForm):
    class Meta:
        model = UserMessage
        fields = '__all__'
