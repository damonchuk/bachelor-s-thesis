from django.views.generic import TemplateView


__all__ = ['AboutView']


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
        })

        return context
