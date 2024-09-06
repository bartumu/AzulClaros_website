from django.http import HttpResponseRedirect
from django.urls import reverse

class RedirectAdminLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/login/'):
            return HttpResponseRedirect(reverse('login') + '?next=' + request.get_full_path())
        response = self.get_response(request)
        return response
