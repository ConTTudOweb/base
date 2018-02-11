from base.accounting.models import *
from base.common.filters import FilterSet


class BankFilter(FilterSet):
    class Meta:
        model = Bank
        fields = {
            'code': ['contains'],
            'description': ['contains'],
        }


class DepositAccountFilter(FilterSet):
    class Meta:
        model = DepositAccount
        fields = {
            'name': ['contains'],
        }
