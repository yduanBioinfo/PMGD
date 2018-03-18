from django.test import TestCase
from django.urls import reverse
from django.test import Client

client = Client()

# Create your tests here.

class HomeViewTests(TestCase):
    def test_view_on_about(self):
        '''
        About page.
        '''
        response = self.client.get(reverse('database:home'))
        self.assertEqual(response.status_code,200)

    def test_view_on_genome_browser(self):
        response = self.client.get(reverse('database:genome_browser'))
        self.assertEqual(response.status_code,200)

    def test_view_on_tools(self):
        response = self.client.get(reverse('database:tools'))
        self.assertEqual(response.status_code,200)
    
    def test_view_on_tools(self):
        response = self.client.get(reverse('database:tutorial'))
        self.assertEqual(response.status_code,200)

    def test_view_on_tools(self):
        response = self.client.get(reverse('database:upload'))
        self.assertEqual(response.status_code,200)

