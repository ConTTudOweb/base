from django.test import TestCase

from base.accounting.models import Category


class CategoryModelTest(TestCase):
    def setUp(self):
        self._description = 'Category 1'
        self.category = Category.objects.create(
            description=self._description
        )

    def test_create(self):
        self.assertTrue(Category.objects.exists())

    def test_str(self):
        self.assertEqual(self._description, str(self.category))
