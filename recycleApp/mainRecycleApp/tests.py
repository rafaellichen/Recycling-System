# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase

# Create your tests here.
class SimpleTest(TestCase):
    def test_home(self):
        response = self.client,get('/mainRecycleApp/home/')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client,get('/mainRecycleApp/about/')
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = self.client,get('/mainRecycleApp/contact/')
        self.assertEqual(response.status_code, 200)
