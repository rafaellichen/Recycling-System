"""
Created on 15 November 2017
@author: Rupesh Basnet
"""
from __future__ import unicode_literals
from django.test import TestCase
from mainRecycleApp.models import RecyclingCenter, PublicRecyclingBin, SpecialWasteSite, Description
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
    def setUp(self):
        '''This method will set up non-modified objects for RecyclingCenterModel
           and will be used by all test methods'''
        self.recyclingCenter = RecyclingCenter.objects.create(idc='1',
                                       name='TestRecycle',
                                       address='123 Test Street',
                                       type='Plastic',
                                       Monday = '1130,1900',
                                       Tuesday = 'closed',
                                       Wednesday = '1130,1900',
                                       Thursday = '1130,1900',
                                       Friday = '1130,1900',
                                       Saturday = '1130,1900',
                                       Sunday = '1130,1900',
                                       borough='Queens',
                                       zip='11104',
                                       cell='123-123-1234',
                                       picksup='1',
                                       url='www.website.com')

    def test_recycle_center_values(self):
        """
        Testing the recycle center values
        """
        self.assertEqual(self.recyclingCenter.idc, "1")
        self.assertEqual(self.recyclingCenter.name, "TestRecycle")
        self.assertEqual(self.recyclingCenter.address, "123 Test Street")
        self.assertEqual(self.recyclingCenter.type, "Plastic")
        self.assertEqual(self.recyclingCenter.Monday, "1130,1900")
        self.assertEqual(self.recyclingCenter.Tuesday, "closed")
        self.assertEqual(self.recyclingCenter.Wednesday, "1130,1900")
        self.assertEqual(self.recyclingCenter.Thursday, "1130,1900")
        self.assertEqual(self.recyclingCenter.Friday, "1130,1900")
        self.assertEqual(self.recyclingCenter.Sunday, "1130,1900")
        self.assertEqual(self.recyclingCenter.borough, "Queens")
        self.assertEqual(self.recyclingCenter.zip, "11104")
        self.assertEqual(self.recyclingCenter.cell, "123-123-1234")
        self.assertEqual(self.recyclingCenter.picksup, "1")
        self.assertEqual(self.recyclingCenter.url, "www.website.com")

    def tearDown(self):
        del self

class RecyclingCenterModelLabelTest(TestCase):

    @classmethod
    def setUp(cls):
        '''This method will set up non-modified objects for RecyclingCenterModel
           and will be used by all test methods'''
        RecyclingCenter.objects.create(idc='1',
                                       name='TestRecycle',
                                       address='123 Test Street',
                                       type='Plastic',
                                       Monday = '1130,1900',
                                       Tuesday = 'closed',
                                       Wednesday = '1130,1900',
                                       Thursday = '1130,1900',
                                       Friday = '1130,1900',
                                       Saturday = '1130,1900',
                                       Sunday = '1130,1900',
                                       borough='Queens',
                                       zip='11104',
                                       cell='123-123-1234',
                                       picksup='1',
                                       url='www.website.com')

    def test_name_label(self):
        """
        Test returns true when the label for name is correct
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_schedule_label(self):
        """
        Test returns true when the label for address is correct
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label_monday = RECYCLINGCENTER._meta.get_field('Monday').verbose_name
        field_label_tuesday = RECYCLINGCENTER._meta.get_field('Tuesday').verbose_name
        field_label_wednesday = RECYCLINGCENTER._meta.get_field('Wednesday').verbose_name
        field_label_thursday = RECYCLINGCENTER._meta.get_field('Thursday').verbose_name
        field_label_friday = RECYCLINGCENTER._meta.get_field('Friday').verbose_name
        field_label_saturday = RECYCLINGCENTER._meta.get_field('Saturday').verbose_name
        field_label_sunday = RECYCLINGCENTER._meta.get_field('Sunday').verbose_name
        self.assertEqual(field_label_monday, 'Monday')
        self.assertEqual(field_label_tuesday, 'Tuesday')
        self.assertEqual(field_label_wednesday, 'Wednesday')
        self.assertEqual(field_label_thursday, 'Thursday')
        self.assertEqual(field_label_friday, 'Friday')
        self.assertEqual(field_label_saturday, 'Saturday')
        self.assertEqual(field_label_sunday, 'Sunday')

    def test_address_label(self):
        """
        Test returns true when the label for address is correct
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_borough_label(self):
        """
        Test returns true when the label for borough is correct
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('borough').verbose_name
        self.assertEqual(field_label, 'borough')


    def test_zipcode_label(self):
        """
        Test returns true when the label for zipcode is correct
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('zip').verbose_name
        self.assertEqual(field_label, 'zip')

    def test_phone_label(self):
        """
        Test returns true when the label for phone is correct
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('cell').verbose_name
        self.assertEqual(field_label, 'cell')

    def test_picks_up_label(self):
        """
        Test returns true when the label for picks up is correct
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('picksup').verbose_name
        self.assertEqual(field_label, 'picksup')

    def test_recycleType_label(self):
        """
        Test returns true when the label for recycleType is correct
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('type').verbose_name
        self.assertEqual(field_label, 'type')

    def test_website_label(self):
        """
        Test returns true when the label for the website is correct
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        field_label = RECYCLINGCENTER._meta.get_field('url').verbose_name
        self.assertEqual(field_label, 'url')

    def test_object_name_is_name(self):
        """
        Test returns true when __str__ method returns the name of the Recycling center 
        """
        RECYCLINGCENTER = RecyclingCenter.objects.get(id=1)
        output_name = RECYCLINGCENTER.name
        self.assertEqual(output_name, str(RECYCLINGCENTER))

class DescriptionModelsTest(TestCase):

    @classmethod
    def setUp(self):
        self.description = Description.objects.create(idc='1',
                                       name='TestSiteName',
                                       description='TestDescription',
                                       pickup_info='Test pickup information')

    def test_public_recycle_bin_name(self):
        self.assertEqual(self.description.idc, "1")
        self.assertEqual(self.description.name, "TestSiteType")
        self.assertEqual(self.description.description, "TestDescription")
        self.assertEqual(self.description.pickup_info, "Test pickup information")

    def tearDown(self):
        del self

class PublicRecyclingBinsModelsTest(TestCase):

    @classmethod
    def setUp(self):
        '''This method will set up non-modified objects for public recycle bins model
           and will be used by all test methods'''
        self.publicRecyclingBin = PublicRecyclingBin.objects.create(borough='Queens',
                                       siteType='TestSiteType',
                                       siteName='TestSiteName',
                                       address='E 227 St/Bronx River Pkway',
                                       latitude='40.890848989',
                                       longitude='-73.864223918')

    def test_public_recycle_bin_name(self):
        """
        Testing the public recycle bins values
        """
        self.assertEqual(self.publicRecyclingBin.borough, "Queens")
        self.assertEqual(self.publicRecyclingBin.siteType, "TestSiteType")
        self.assertEqual(self.publicRecyclingBin.siteName, "TestSiteName")
        self.assertEqual(self.publicRecyclingBin.address, "E 227 St/Bronx River Pkway")
        self.assertEqual(self.publicRecyclingBin.latitude, "40.890848989")
        self.assertEqual(self.publicRecyclingBin.longitude, "-73.864223918")

    def tearDown(self):
        del self

class PublicRecyclingBinsModelsLabelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''This method will set up non-modified objects for public recycle bins model
           and will be used by all test methods'''
        PublicRecyclingBin.objects.create(borough='Queens',
                                       siteType='TestSiteType',
                                       siteName='TestSiteName',
                                       address='E 227 St/Bronx River Pkway',
                                       latitude='40.890848989',
                                       longitude='-73.864223918')

    def test_borough_label(self):
        """
        Test Borough label
        """
        PUBLICRECYCLEBIN = PublicRecyclingBin.objects.get(id=1)
        field_label = PUBLICRECYCLEBIN._meta.get_field('borough').verbose_name
        self.assertEqual(field_label, 'borough')

    def test_siteType_label(self):
        """
        Test Site Type label
        """
        PUBLICRECYCLEBIN = PublicRecyclingBin.objects.get(id=1)
        field_label = PUBLICRECYCLEBIN._meta.get_field('siteType').verbose_name
        self.assertEqual(field_label, 'siteType')

    def test_siteName_label(self):
        """
        Test SiteName Type label
        """
        PUBLICRECYCLEBIN = PublicRecyclingBin.objects.get(id=1)
        field_label = PUBLICRECYCLEBIN._meta.get_field('siteName').verbose_name
        self.assertEqual(field_label, 'siteName')

    def test_address_label(self):
        """
        Test Address label
        """
        PUBLICRECYCLEBIN = PublicRecyclingBin.objects.get(id=1)
        field_label = PUBLICRECYCLEBIN._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_latitude_label(self):
        """
        Test Latitude label
        """
        PUBLICRECYCLEBIN = PublicRecyclingBin.objects.get(id=1)
        field_label = PUBLICRECYCLEBIN._meta.get_field('latitude').verbose_name
        self.assertEqual(field_label, 'latitude')

    def test_longitude_label(self):
        """
        Test Longitude label
        """
        PUBLICRECYCLEBIN = PublicRecyclingBin.objects.get(id=1)
        field_label = PUBLICRECYCLEBIN._meta.get_field('longitude').verbose_name
        self.assertEqual(field_label, 'longitude')

    def test_object_name_is_siteName(self):
        """
        Test returns true when __str__ method returns the siteName of the public recycling bins 
        """
        PUBLICRECYCLEBIN = PublicRecyclingBin.objects.get(id=1)
        output_name = PUBLICRECYCLEBIN.siteName
        self.assertEqual(output_name, str(PUBLICRECYCLEBIN))

    
class SpecialWasteSiteModelTest(TestCase):

    @classmethod
    def setUp(self):
        '''This method will set up non-modified objects for SpecialWasteSiteModel
           and will be used by all test methods'''
        self.specialWasteSite = SpecialWasteSite.objects.create(name='TestName',
                                       latitude='40.890848989',
                                       longitude='-73.864223918',
                                       location='E 227 St/Bronx River Pkway',
                                       hours='Saturdays and the last Friday of every month from 10 AM to 5 PM.',
                                       url='http://www.nyc.gov/html/dsny/html/collection/special_schedule.shtml')
        
    def test_special_waste_site_name(self):
        """
        Testing the special waste site values
        """
        self.assertEqual(self.specialWasteSite.name, "TestName")
        self.assertEqual(self.specialWasteSite.latitude, "40.890848989")
        self.assertEqual(self.specialWasteSite.longitude, "-73.864223918")
        self.assertEqual(self.specialWasteSite.location, "E 227 St/Bronx River Pkway")
        self.assertEqual(self.specialWasteSite.hours, "Saturdays and the last Friday of every month from 10 AM to 5 PM.")
        self.assertEqual(self.specialWasteSite.url, "http://www.nyc.gov/html/dsny/html/collection/special_schedule.shtml")        

    def tearDown(self):
        del self

class SpecialWasteSiteModelLabelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''This method will set up non-modified objects for SpecialWasteSiteModel
           and will be used by all test methods
        '''
        SpecialWasteSite.objects.create(name='TestName',
                                       latitude='40.890848989',
                                       longitude='-73.864223918',
                                       location='E 227 St/Bronx River Pkway',
                                       hours='Saturdays and the last Friday of every month from 10 AM to 5 PM.',
                                       url='http://www.nyc.gov/html/dsny/html/collection/special_schedule.shtml')
        
    def test_name_label(self):
        """
        Test name label
        """
        SPECIALWASTESITE = SpecialWasteSite.objects.get(id=1)
        field_label = SPECIALWASTESITE._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_latitude_label(self):
        """
        Test latitude label
        """
        SPECIALWASTESITE = SpecialWasteSite.objects.get(id=1)
        field_label = SPECIALWASTESITE._meta.get_field('latitude').verbose_name
        self.assertEqual(field_label, 'latitude') 

    def test_location_label(self):
        """
        Test location label
        """
        SPECIALWASTESITE = SpecialWasteSite.objects.get(id=1)
        field_label = SPECIALWASTESITE._meta.get_field('location').verbose_name
        self.assertEqual(field_label, 'location') 

    def test_hours_label(self):
        """
        Test hours label
        """
        SPECIALWASTESITE = SpecialWasteSite.objects.get(id=1)
        field_label = SPECIALWASTESITE._meta.get_field('hours').verbose_name
        self.assertEqual(field_label, 'hours') 

    def test_url_label(self):
        """
        Test url label
        """
        SPECIALWASTESITE = SpecialWasteSite.objects.get(id=1)
        field_label = SPECIALWASTESITE._meta.get_field('url').verbose_name
        self.assertEqual(field_label, 'url')

    def test_object_name_is_siteName(self):
        """
        Test returns true when __str__ method returns the name of the special waste location
        """
        SPECIALWASTESITE = SpecialWasteSite.objects.get(id=1)
        output_name = SPECIALWASTESITE.name
        self.assertEqual(output_name, str(SPECIALWASTESITE))
