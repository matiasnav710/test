from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class TimeSlotAPITest(APITestCase):
    def test_create_timeslot(self):
        url = reverse('timeslot-list')
        data = {
            'day_of_week': 'monday',
            'start_time': '08:00',
            'stop_time': '10:00',
            'ids': [1, 2, 3]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
