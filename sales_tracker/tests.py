from django.test import TestCase
from rest_framework.test import APITestCase
from sales_tracker.models import Store
from django.contrib.auth.models import User
# Create your tests here.

class StoreTests(APITestCase):
  def setUp(self):
    user=User.objects.create_user(username='admin',password='admin',email='admin@localhost')
    self.client.force_authenticate(user)
    
  def test_retrieve_store(self):
    response = self.client.post("/sales-tracker/",data={
      "url":"https://mycustom-cars.com"
    })
    print(response.json())
    self.assertEqual(response.status_code,201)
    
    response = self.client.post("/sales-tracker/",data={
      "url":"https://mycustom-cars.com"
    })
    print(response.json())
    self.assertEqual(response.status_code,201)
    
    response = self.client.get("/sales-tracker/1/")
    self.assertEqual(response.status_code,200)
    print(response.json())