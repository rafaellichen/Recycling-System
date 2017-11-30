"""
Created on 15 November 2017
@author: Rupesh Basnet
"""
from __future__ import unicode_literals
from django.test import TestCase
from mainRecycleApp.models import RecyclingCenter
from django.core.urlresolvers import reverse


class MainRecycleAppViewTest(TestCase):
    """
    Create Tests for the MainRecycleApp Views
    """
    def test_home_from_url(self):
        """
        Test returns true when home is redered properly with URL
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_from_url(self):
        """
        Test returns true when about is redered properly with URL
        """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_contact_from_url(self):
        """
        Test returns true when contact is redered properly with URL
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_about_from_name(self):
        """
        Test returns true when about is redered properly with name
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_from_name(self):
        """
        Test returns true when contact is redered properly with name
        """
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_home_template_use(self):
        """
        Test returns true when home is redered properly with right template
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'mainRecycleApp/home.html')

    def test_about_template_use(self):
        """
        Test returns true when about is redered properly with right template
        """
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'mainRecycleApp/about.html')
    
    def test_contact_template_use(self):
        """
        Test returns true when contact is redered properly with right template
        """
        response = self.client.get('/contact/')
        self.assertTemplateUsed(response, 'mainRecycleApp/contact.html')   

class RecyclingCenterModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''This method will set up non-modified objects for RecyclingCenterModel
           and will be used by all test methods'''
        RecyclingCenter.objects.create(name='TestRecycle',
                                       address='123 Test Street',
                                       borough='Queens',
                                       state='NY',
                                       zipcode='11104',
                                       phone='123-123-1234',
                                       picks_up='1',
                                       recycleType='Plastic',
                                       website='www.website.com')

    def test_name_label(self):
        """
        Test returns true when about is redered properly with right template
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_address_label(self):
        """
        Test returns true when about is redered properly with right template
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_borough_label(self):
        """
        Test returns true when about is redered properly with right template
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('borough').verbose_name
        self.assertEqual(field_label, 'borough')

    def test_state_label(self):
        """
        Test returns true when about is redered properly with right template
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('state').verbose_name
        self.assertEqual(field_label, 'state')

    def test_zipcode_label(self):
        """
        Test returns true when about is redered properly with right template
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('zipcode').verbose_name
        self.assertEqual(field_label, 'zipcode')

    def test_phone_label(self):
        """
        Test returns true when about is redered properly with right template
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, 'phone')

    def test_picks_up_label(self):
        """
        Test returns true when about is redered properly with right template
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('picks_up').verbose_name
        self.assertEqual(field_label, 'picks up')

    def test_recycleType_label(self):
        """
        Test returns true when about is redered properly with right template
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('recycleType').verbose_name
        self.assertEqual(field_label, 'recycleType')

    def test_website_label(self):
        """
        Test returns true when about is redered properly with right template
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('website').verbose_name
        self.assertEqual(field_label, 'website')

    def test_object_name_is_name(self):
        """
        Test returns true when about is redered properly with right template
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        output_name = RECYCLINGCENTER.name
        self.assertEqual(output_name, str(RECYCLINGCENTER))
