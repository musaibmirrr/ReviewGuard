# backendApp/middleware.py

from django.conf import settings
from django.contrib.sessions.backends.db import SessionStore
from django.utils.deprecation import MiddlewareMixin

class MultiAppSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/shop/'):
            settings.SESSION_ENGINE = settings.SHOP_SESSION_ENGINE
            request.session = SessionStore(session_key=request.COOKIES.get('shop_sessionid'))
        elif request.path.startswith('/reviewGuard/'):
            settings.SESSION_ENGINE = settings.ADMIN_SESSION_ENGINE
            request.session = SessionStore(session_key=request.COOKIES.get('admin_sessionid'))
        else:
            settings.SESSION_ENGINE = 'django.contrib.sessions.backends.db'
    
    def process_response(self, request, response):
        if hasattr(request, 'session'):
            # If the request is for the shop, set the shop session cookie
            if request.path.startswith('/shop/'):
                response.set_cookie('shop_sessionid', request.session.session_key, httponly=True)
            # If the request is for reviewGuard (admin), set the admin session cookie
            elif request.path.startswith('/reviewGuard/'):
                response.set_cookie('admin_sessionid', request.session.session_key, httponly=True)
        return response







































