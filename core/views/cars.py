from django.views.generic import TemplateView
from core.models import Car, CarComment, CarCommentForm
from django.utils.decorators import method_decorator
from core.views import json_response


__all__ = ['CarsView', 'CarDetailView']


class CarsView(TemplateView):
    template_name = 'cars.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'cars': Car.objects.all()
        })

        return context


class CarDetailView(TemplateView):
    template_name = 'car-single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'car': Car.objects.get(id=kwargs['id']),
            'car_comments': CarComment.objects.filter(car_id=kwargs['id'])
        })

        return context

    @method_decorator(json_response(check_ajax=False))
    def post(self, request, *args, **kwargs):
        form = CarCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return {
                'success': True,
                'message': 'Your Message Accepted!',
                }
        else:
            return {'success': False, 'errors': form.errors}
