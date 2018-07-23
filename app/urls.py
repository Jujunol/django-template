from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path, include


def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    return redirect('login')


def home(request):
    return render(request, 'layouts/react.html')


urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('accounts/', include('users.urls')),
]
