from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include


def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return redirect('login')


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
]
