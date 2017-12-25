import unittest
import mainRecycleApp
from mock import patch, MagicMock
from django.test import TestCase
from django.test.client import RequestFactory

@patch('mainRecycleApp.views.render')
class TestViewsMainRecycleAppUnit(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.requestIndex = self.factory.get('/')
        self.requestAbout = self.factory.get('/about')
        self.requestContact = self.factory.get('/contact')
        self.requestFaq = self.factory.get('/faqs')

    def test_index_gets_index_template(self, render_mock):
        mainRecycleApp.views.index(self.requestIndex)
        self.assertTrue(render_mock.called)
        render_mock.assert_called_with(self.requestIndex, 'mainRecycleApp/home.html')

    def test_about_gets_about_template(self, render_mock):
        mainRecycleApp.views.about(self.requestAbout)
        self.assertTrue(render_mock.called)
        render_mock.assert_called_with(self.requestAbout, 'mainRecycleApp/about.html')

    def test_about_gets_contact_template(self, render_mock):
        mainRecycleApp.views.about(self.requestContact)
        self.assertTrue(render_mock.called)
        render_mock.assert_called_with(self.requestContact, 'mainRecycleApp/contact.html')

    def test_about_gets_faqs_template(self, render_mock):
        mainRecycleApp.views.about(self.requestFaq)
        self.assertTrue(render_mock.called)
        render_mock.assert_called_with(self.requestFaq, 'mainRecycleApp/faqs.html')
