from django.test import TestCase
import recycle101
# Create your tests here.
from recycle101.models import HowTo
from mock import patch, MagicMock
from django.test import TestCase
from django.test.client import RequestFactory

@patch('recycle101.views.render')
class TestViewsRecycle101AppUnit(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.requestRecycle = self.factory.get('/recycle101')
        self.requestSearch = self.factory.post('/search101', {'recycleType' : 'test'})

    def test_index_gets_main_template(self, render_mock):
        recycle101.views.index(self.requestRecycle)
        self.assertTrue(render_mock.called)
        render_mock.assert_called_with(self.requestRecycle, 'main.html')

    def test_search_gets_main_template(self, render_mock):
        recycle101.views.searchHowTo(self.requestSearch)
        self.assertTrue(render_mock.called)
        render_mock.assert_called_with(self.requestSearch, 'main.html', {'data' : []})


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

