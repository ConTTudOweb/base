from rest_framework import viewsets

from base.accounting.models import Bank
from base.accounting.serializers import BankSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
