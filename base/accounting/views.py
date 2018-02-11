from rest_framework import viewsets

from base.accounting.filters import *
from base.accounting.serializers import *


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filter_class = BankFilter


class DepositAccountViewSet(viewsets.ModelViewSet):
    queryset = DepositAccount.objects.all()
    serializer_class = DepositAccountSerializer
    filter_class = DepositAccountFilter
