from django.test import TestCase

from base.accounting.models import People


_name = 'People 1'


def create_people(**kwargs):
    people = People.objects.create(
        name=_name,
        **kwargs
    )
    return people


class PeopleModelTest(TestCase):
    def setUp(self):
        self.people = create_people()

    def test_create(self):
        self.assertTrue(People.objects.exists())

    def test_create_customer(self):
        person_customer = create_people(customer=True)
        self.assertTrue(person_customer.is_customer())

    def test_create_supplier(self):
        person_supplier = create_people(supplier=True)
        self.assertTrue(person_supplier.is_supplier())

    def test_str(self):
        self.assertEqual(_name, str(self.people))
