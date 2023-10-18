from django.views.generic import TemplateView
from core.models import UserMessageForm
from django.utils.decorators import method_decorator
from core.views import json_response


__all__ = ['ContactView']


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
        })

        return context

    @method_decorator(json_response(check_ajax=False))
    def post(self, request, *args, **kwargs):
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return {
                'success': True,
                'message': 'Your Message Accepted!',
                }
        else:
            return {'success': False, 'errors': form.errors}
