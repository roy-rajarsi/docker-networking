from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from typing import Optional


class Health(APIView):

    def get(self, request: Request, format: Optional[str] = None) -> Response:
        return Response(data='OK', status=HTTP_200_OK)
