from django.test import TestCase

from base.accounting.models import AccountPayable
from base.accounting.tests.test_model_account import create_account


class AccountPayableModelTest(TestCase):
    def setUp(self):
        self._description = 'Account Payable 1'
        self.accountPayable = AccountPayable.objects.create(
            **create_account(self._description)
        )

    def test_create(self):
        self.assertTrue(AccountPayable.objects.exists())

    def test_str(self):
        self.assertEqual(self._description, str(self.accountPayable))
