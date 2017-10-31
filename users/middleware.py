from django.core.urlresolvers import reverse
from utils.wrappers import *


class RecordUrlMiddleware(object):
    def process_request(self, request):
        exclude_urls = [
            reverse('users:index'),
            reverse('users:order'),
            reverse('users:address'),
            reverse('users:login'),
            reverse('users:register'),
            reverse('users:register_handle'),
            reverse('users:login_handle'),
            reverse('users:check_exist'),
            reverse('users:logoff'),
            reverse('carts:index'),
        ]
        if request.path not in exclude_urls:
            set_session(request, 'pre_url', request.get_full_path())
