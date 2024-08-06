from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

# Create your tests here.
class FacebookAdsTests(APITestCase):
  def setUp(self):
    user=User.objects.create_user(username='admin',password='admin',email='admin@localhost')
    self.client.force_authenticate(user)
    
  def test_search_ads(self):
    response = self.client.get("/facebook-ads/search/?search_term=monkey?country_code=FR")
    print(response.json())
    self.assertEqual(response.status_code,200)