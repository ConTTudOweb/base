from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status

from base.accounting.models import Bank
from base.authentication.models import User
from base.urls import BankViewSet

_description = 'Bank 1'


def get_fields_bank():
    _code = '001'
    return {
        'code': _code,
        'description': _description
    }


def create_bank():
    bank = Bank.objects.create(**get_fields_bank())
    return bank


class BankModelTest(TestCase):
    def setUp(self):
        self.bank = create_bank()

    def test_create(self):
        self.assertTrue(Bank.objects.exists())

    def test_str(self):
        self.assertEqual(_description, str(self.bank))

    def test_unique_code(self):
        with self.assertRaises(IntegrityError):
            create_bank()


class AccountTests(APITestCase):
    fixtures = ['banks.json', 'users.json']

    def setUp(self):
        self.user = User.objects.first()
        self.client.force_authenticate(self.user)

    def test_list_api(self):
        url = reverse('bank-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_api(self):
        bank = Bank.objects.first()
        url = reverse('bank-detail', args=[bank.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_api(self):
        expected_count = Bank.objects.count() + 1
        url = reverse('bank-list')
        data = get_fields_bank()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bank.objects.count(), expected_count)
        self.assertEqual(Bank.objects.last().description, _description)

    def test_put_api(self):
        expected_count = Bank.objects.count()
        bank = Bank.objects.first()
        url = reverse('bank-detail', args=[bank.pk])
        data = get_fields_bank()
        _description_new = _description + " new"
        data.update({'description': _description_new})
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Bank.objects.count(), expected_count)
        self.assertEqual(Bank.objects.get(pk=bank.pk).description, _description_new)
