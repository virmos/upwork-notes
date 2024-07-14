from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.urls import URLPattern, URLResolver
import logging

urlconf = __import__(settings.ROOT_URLCONF, {}, {}, [''])

def list_urls(lis, acc=None):
    if acc is None:
        acc = []
    if not lis:
        return
    l = lis[0]
    if isinstance(l, URLPattern):
        yield acc + [str(l.pattern)]
    elif isinstance(l, URLResolver):
        yield from list_urls(l.url_patterns, acc + [str(l.pattern)])
    yield from list_urls(lis[1:], acc)


def redirect_to_login(request):
    logging.error("FOUND")
    logging.error("redirect login")
    logging.error(vars(request))
    for p in list_urls(urlconf.urlpatterns):
        logging.error(''.join(p))
    return redirect('login')

urlpatterns = [
    path('', redirect_to_login, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
]