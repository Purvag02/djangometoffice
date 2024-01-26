# metoffice_app/tests/test_models.py

from django.test import TestCase
from metoffice_app.models import Region, Parameter

class RegionModelTest(TestCase):
    def test_create_region(self):
        region = Region.objects.create(name='Test Region')
        self.assertEqual(region.name, 'Test Region')

class ParameterModelTest(TestCase):
    def test_create_parameter(self):
        parameter = Parameter.objects.create(name='Test Parameter')
        self.assertEqual(parameter.name, 'Test Parameter')
