from base.accounting.models import Bank
from base.common.filters import FilterSet


class BankFilter(FilterSet):
    class Meta:
        model = Bank
        fields = {
            'code': ['contains'],
            'description': ['contains'],
        }
