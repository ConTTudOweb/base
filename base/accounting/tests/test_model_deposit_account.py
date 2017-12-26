from django.test import TestCase

from base.accounting.models import DepositAccount
from base.accounting.tests.test_model_entity import create_entity


class DepositAccountModelTest(TestCase):
    def setUp(self):
        self._name = 'Deposit Account 1'
        self.depositAccount = DepositAccount.objects.create(
            entity=create_entity(),
            type=DepositAccount.DepositAccountTypes.current_account.value,
            bank=None,
            agency_number=None,
            agency_digit=None,
            account_number=None,
            account_digit=None,
            name=self._name
        )

    def test_create(self):
        self.assertTrue(DepositAccount.objects.exists())

    def test_str(self):
        self.assertEqual(self._name, str(self.depositAccount))
