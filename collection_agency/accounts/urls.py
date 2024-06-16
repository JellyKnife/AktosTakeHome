from django.urls import path
from .views import get_accounts

urlpatterns = [
    path('accounts', get_accounts, name='get_accounts'),
]
