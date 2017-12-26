from django.test import TestCase

from base.accounting.models import ClassificationCenter
from base.accounting.tests.test_model_entity import create_entity

_name = 'Classification Center 1'


def create_classification_center(**kwargs):
    classification_center = ClassificationCenter.objects.create(
        entity=create_entity(),
        name=_name,
        **kwargs
    )
    return classification_center


class ClassificationCenterModelTest(TestCase):
    def setUp(self):
        self.classification_center = create_classification_center()

    def test_create(self):
        self.assertTrue(ClassificationCenter.objects.exists())

    def test_create_cost_center(self):
        classification_center_cost = create_classification_center(cost_center=True)
        self.assertTrue(classification_center_cost.is_cost_center())

    def test_create_revenue_center(self):
        classification_center_revenue = create_classification_center(revenue_center=True)
        self.assertTrue(classification_center_revenue.is_revenue_center())

    def test_str(self):
        self.assertEqual(_name, str(self.classification_center))
