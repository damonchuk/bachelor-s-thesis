from django.views.generic import TemplateView
from core.models import Car, RentIssue, RentIssueForm
from django.utils.decorators import method_decorator
from core.views import json_response


__all__ = ['RentView']


class RentView(TemplateView):
    template_name = 'rent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'cars': Car.objects.all(),
            'rent_types': RentIssue.RENT_TYPE_CHOICES
        })

        return context

    @method_decorator(json_response(check_ajax=False))
    def post(self, request, *args, **kwargs):
        form = RentIssueForm(request.POST)
        if form.is_valid():
            form.save()
            return {
                'success': True,
                'message': 'Rent Issue Accepted!',
                }
        else:
            return {'success': False, 'errors': form.errors}
