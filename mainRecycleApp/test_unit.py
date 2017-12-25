"""Unit test for MainRecycleApp with mock testing"""
import mainRecycleApp
from mainRecycleApp.views import get_borough_from_zip, get_safe_disposal_events, get_public_recycle_bins
from mock import patch, MagicMock
import json
from django.test import TestCase
from django.test.client import RequestFactory

@patch('mainRecycleApp.views.render')
class TestViewsMainRecycleAppUnit(TestCase):

    def setUp(self):
        """Setup Method for the Test Views Main Recycle App"""
        self.factory = RequestFactory()
        self.requestIndex = self.factory.get('/')
        self.requestAbout = self.factory.get('/about')
        self.requestContact = self.factory.get('/contact')
        self.requestFaq = self.factory.get('/faqs')

    def test_index_gets_index_template(self, render_mock):
        """Method to test if the render is being called and is being called with home.html"""
        mainRecycleApp.views.index(self.requestIndex)
        self.assertTrue(render_mock.called)
        render_mock.assert_called_with(self.requestIndex, 'mainRecycleApp/home.html')

    def test_about_gets_about_template(self, render_mock):
        """Method to test if the render is being called and is being called with about.html"""
        mainRecycleApp.views.about(self.requestAbout)
        self.assertTrue(render_mock.called)
        render_mock.assert_called_with(self.requestAbout, 'mainRecycleApp/about.html')

    def test_contact_gets_contact_template(self, render_mock):
        """Method to test if the render is being called and is being called with contact.html"""
        mainRecycleApp.views.contact(self.requestContact)
        self.assertTrue(render_mock.called)
        render_mock.assert_called_with(self.requestContact, 'mainRecycleApp/contact.html')

    def test_faqs_gets_faqs_template(self, render_mock):
        """Method to test if the render is being called and is being called with faqs.html"""
        mainRecycleApp.views.faqs(self.requestFaq)
        self.assertTrue(render_mock.called)
        render_mock.assert_called_with(self.requestFaq, 'mainRecycleApp/faqs.html')

class TestHelperMethodsMainRecycleAppUnit(TestCase):

    def test_get_borough_from_zip(self):
        self.assertTrue(get_borough_from_zip("11104"), "Queens")
        self.assertTrue(get_borough_from_zip("asdfj"), '')
        self.assertFalse(get_borough_from_zip("1243234"), "Queens")

