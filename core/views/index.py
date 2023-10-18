from django.views.generic import TemplateView
from core.models import Car

__all__ = ['IndexView']


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'cars': Car.objects.all()
        })

        return context
