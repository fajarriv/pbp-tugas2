from django.test import TestCase, Client
from django.urls import resolve
from .views import *

# Create your tests here.
class AppTest(TestCase):
    def test1(self):
        response_html = Client().get('/mywatchlist/html')
        response_xml = Client().get('/mywatchlist/xml/')
        response_json = Client().get('/mywatchlist/json/')
        self.assertEqual(response_html.status_code,200)
        self.assertEqual(response_xml.status_code,200)
        self.assertEqual(response_json.status_code,200)