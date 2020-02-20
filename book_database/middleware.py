from django.conf import settings
import re
from django.shortcuts import redirect

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        return response

    # will be run when django is about to run one of the view functions
    def process_view(self, request, view_func, view_args, view_kwargs):
        # check if request has the attribute of user
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')  # the url a user is going to

        if not request.user.is_authenticated:
            if not any(url.match(path) for url in EXEMPT_URLS):
                return redirect(settings.LOGIN_URL)
