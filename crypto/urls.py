# crypto/urls.py
from django.urls import path
from .views import CryptoPriceView

urlpatterns = [
    path('prices/', CryptoPriceView.as_view(), name='crypto-prices'),
]
