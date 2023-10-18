import logging
from functools import wraps
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render


__all__ = [
    'json_response',
    'AjaxError',
    'AjaxFormError',
]

logger = logging.getLogger('django.request')


class AjaxError(Exception):
    def __init__(self, *args, **kwargs):
        self.is_need_push = kwargs.pop('is_need_push', True)
        super(AjaxError, self).__init__(*args)
        self.error = args[0]


class AjaxFormError(Exception):
    def __init__(self, *args, **kwargs):
        super(AjaxFormError, self).__init__(*args)
        self.errors = args[0]


def json_response(need_auth=False, check_ajax=True):
    def json_responser(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            request = args[0]

            if need_auth and not request.user.is_authenticated:
                return HttpResponse('Unauthorized', status=401)

            if check_ajax:
                if not request.is_ajax():
                    raise Http404

            status_code = 200
            try:
                json_res = f(*args, **kwargs)
                json_res = {'status': True, 'data': json_res}
            except AjaxError as e:
                json_res = {'status': False, 'error': e.error, 'is_need_push': e.is_need_push}
            except AjaxFormError as e:
                json_res = {'status': False, 'form_errors': e.errors}
            except Exception as e:

                json_res = {
                    'status': False,
                    'is_need_push': True,
                    'error': "An error occurred while processing the request. Try again or contact support",
                }

                logger.exception(
                    e,
                    exc_info=True,
                    extra={
                        'status_code': status_code,
                        'request': request
                    }
                )

            response = JsonResponse(json_res, status=status_code)
            response['Vary'] = 'Accept'
            return response

        return wrapper

    return json_responser


def view_404(request, exception):
    return HttpResponse(
        content=render(request, '404.html', {}),
        content_type='text/html; charset=utf-8',
        status=404
    )


def view_500(request):
    return HttpResponse(
        content=render(request, '500.html', {}),
        content_type='text/html; charset=utf-8',
        status=500
    )

