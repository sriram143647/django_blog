from django.urls import path,include
from .views import register,profile,login_view

urlpatterns = [
    path('signup/', register, name='signup'),
    path('login/', login_view, name='login'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', profile, name='profile'),
]