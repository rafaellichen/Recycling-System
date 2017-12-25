from django.test import TestCase

# Create your tests here.
from recycle101.models import HowTo

class HowToModelTest(TestCase):

    @classmethod
    def setUp(self):
        '''This method will set up non-modified objects for How To model
           and will be used by all test methods'''
        self.howTo = HowTo.objects.create(recycleType='Test Type',
                                       description='Test description')

    def test_public_recycle_bin_name(self):
        """
        Testing the how to model values
        """
        self.assertEqual(self.howTo.recycleType, "Test Type")
        self.assertEqual(self.howTo.description, "Test description")

    def tearDown(self):
        del self
