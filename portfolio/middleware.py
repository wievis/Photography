import requests
from .models import Visitor

class Track:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/admin/') and not request.user.is_authenticated:
            ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
            Visitor.objects.create(
                ip=ip,
                ua=request.META.get('HTTP_USER_AGENT'),
                ref=request.META.get('HTTP_REFERER')
            )
        return self.get_response(request)