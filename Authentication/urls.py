
from django.contrib import admin
from django.urls import path

from .views import home

from accounts.views import login_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
    path('accounts/login/', login_view)
]
