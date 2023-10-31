from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Menu 1', price='12.09')
        Menu.objects.create(title='Menu 2', price='13.89')
        self.client = APIClient()

    def test_getall(self):
        url = reverse('MenuItemsView')

        response = self.client.get(url)

        menus = Menu.objects.all()

        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, serializer.data)