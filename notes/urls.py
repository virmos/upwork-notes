from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
import logging

def redirect_to_login(request):
    logging.error("FOUND")
    logging.error("redirect login")
    return redirect('login')

urlpatterns = [
    path('', redirect_to_login, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
]