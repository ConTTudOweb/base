from django.test import TestCase

from base.accounting.models import Bank


_description = 'Bank 1'


def create_bank():
    _code = '001'
    bank = Bank.objects.create(
        code=_code,
        description=_description
    )
    return bank


class BankModelTest(TestCase):
    def setUp(self):
        self.bank = create_bank()

    def test_create(self):
        self.assertTrue(Bank.objects.exists())

    def test_str(self):
        self.assertEqual(_description, str(self.bank))
