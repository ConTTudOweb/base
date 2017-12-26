from django.test import TestCase

from base.accounting.models import Entity


_name = 'Entity 1'


def create_entity():
    entity = Entity.objects.create(
        name=_name
    )
    return entity


class EntityModelTest(TestCase):
    def setUp(self):
        self.entity = create_entity()

    def test_create(self):
        self.assertTrue(Entity.objects.exists())

    def test_str(self):
        self.assertEqual(_name, str(self.entity))
