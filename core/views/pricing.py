from django.views.generic import TemplateView
from core.models import Car


__all__ = ['PricingView']


class PricingView(TemplateView):
    template_name = 'pricing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'cars': Car.objects.all()
        })

        return context
