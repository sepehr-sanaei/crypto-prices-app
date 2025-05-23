# crypto/views.py
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class CryptoPriceView(APIView):
    def get(self, request):
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        return Response(data)
