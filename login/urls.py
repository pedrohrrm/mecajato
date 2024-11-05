from django.urls import path
from .views import (
    login_view,
    signup_view,
    logout_view,
    base_view,
)

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('home/', base_view, name='home'),  # Ponto de entrada
]