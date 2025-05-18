from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_503_SERVICE_UNAVAILABLE
from typing import Optional
import requests
import os


class PingPayments(APIView):

    payments_container_ip: str = os.environ.get("PAYMENTS_CONTAINER_IP")
    payments_container_port: int = os.environ.get("PAYMENTS_CONTAINER_PORT")
    payments_host: str = str().join([payments_container_ip, ':', payments_container_port])

    def get(self, request: Request, format: Optional[str] = None) -> Response:
        response = requests.get(url=f"http://{PingPayments.payments_host}/health/")
        return Response(data=response.json() if response.headers.get('Content-Type') == 'application/json' else response.text,
                        status=HTTP_200_OK if response.status_code == 200 else HTTP_503_SERVICE_UNAVAILABLE)
