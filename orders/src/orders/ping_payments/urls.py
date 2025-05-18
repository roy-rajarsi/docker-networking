from django.urls import path

from .views import PingPayments

urlpatterns = [
    path('', PingPayments.as_view())
]
