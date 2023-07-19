import base64
import json
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from app.models import Trip

password = 'pAsswOrd!'

@database_sync_to_async
def create_user(username,password):
    user = get_user_model().objects.create_user(
        username=username,
        password=password
    )
    access = AccessToken.for_user(user)
    return user,access
class AuthenticationTest(APITestCase):
    def test_user_can_sign_up(self):
        response = self.client.post(reverse('sing_up'),data={
            'username': 'ismatilloismatov1995@gmail.com',
            'first_name': 'ismatillo',
            'last_name': 'ismatillo',
            'password1': password,
            'password': password,
        })
    def test_user_can_login(self):
        user = create_user()
        response = self.client.post(reverse('log_in'), data={
            'username':user.username,
            'password':password
        })
        access = response.data['access']
        header,payload,signatura = access.sqlit('.')
        decoded_payload = base64.b64decode(f'{payload}==')
        paylaod_data = json.loads(decoded_payload)
        self.assertEqual(status.HTTP_201_CREATED,response.status_code)
        self.assertIsNotNone(response.data['refresh'])
        self.assertEqual(response.data['id'],user.id)
        self.assertEqual(response.data['username'],user.username)
        self.assertEqual(response.data['first_name'],user.first_name)
        self.assertEqual(response.data['last_name'],user.last_name)



class HttpTripsTest(APITestCase):
    def setup(self):
        user = create_user()
        response = self.client.post(reverse('log_in'),data={
            'username': user.username,
            'password':password,
        })
        self.access = response.data['access']

    def test_user_can_list_trips(self):
        trips = [
            Trip.objects.create(pick_up_adress='A',drop_off_adress='B'),
            Trip.objects.create(pick_up_adress='B',drop_off_adress='C')
        ]
        response = self.client.get(reverse('trip:trip_list'),
                                   HTTP_AUTHORIZATION=f'Bearer{self.access}'
                                   )
        self.assertEqual(status.HTTP_200_OK,response.status_code)
        exp_trip_ids  = [str(trips.id) for trip in trips]
        act_trip_ids = [trip.get('id') for trip in response.data]
        self.assertCountEqual(exp_trip_ids,act_trip_ids)

    def test_user_can_retrieve_trip_by_id(self) -> object:
        trip = Trip.objects.create(pick_up_address='A',drop_off_address='B')
        response = self.client.get(trip.get_absolute_url,
                                   HTTP_AUTHORIZATION=f'Bearer {self.access}'
                                   )  
        self.assertEqual(status.HTTP_200_OK,response.status_code)
        self.assertEqual(str(trip.id),response.data.get('id'))

import config
DJANGO_SETTINGS_MODULE = config.settings
from django.conf import settings

def pytest_configure():
    settings.configure()
   
   