from django.test import TestCase

from base.accounting.models import AccountReceivables
from base.accounting.tests.test_model_account import create_account


class AccountReceivablesModelTest(TestCase):
    def setUp(self):
        self._description = 'Account Receivables 1'
        self.accountReceivables = AccountReceivables.objects.create(
            **create_account(self._description)
        )

    def test_create(self):
        self.assertTrue(AccountReceivables.objects.exists())

    def test_str(self):
        self.assertEqual(self._description, str(self.accountReceivables))
