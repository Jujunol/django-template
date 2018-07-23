from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from .models import Record


class RecordBaseTestCase(TestCase): 
    def setUp(self):
        user = User.objects.create(username='tester')

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.record_data = {
            'name': "Test",
            'owner': user.id,
        }

        self.create_url = reverse('api:record_create')
        self.details_url = reverse('api:record_details', kwargs={'pk': 1})
        self.response = self.client.post(self.create_url, self.record_data, format="json")


class RecordTestCase(RecordBaseTestCase):
    """ Workflow Tests """

    def test_can_create_record(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_can_view_record(self):
        record = Record.objects.get()
        response = self.client.get(self.details_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], record.id)

    def test_can_update_record(self):
        update_data = self.record_data.copy()
        update_data['name'] = 'Changed name'

        response = self.client.put(self.details_url, update_data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_record(self):
        response = self.client.delete(self.details_url, follow=True)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class GuestRecordTestCase(RecordBaseTestCase):
    """ Testing whether guest can make changes """

    def setUp(self):
        super().setUp()
        self.client = APIClient()

    def test_can_guest_create_record(self):
        record_data = self.record_data.copy()
        response = self.client.post(self.create_url, record_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_guest_view_record(self):
        response = self.client.get(self.details_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_guest_modify_record(self):
        update_data = self.record_data.copy()
        update_data['name'] = 'Changed name'

        response = self.client.put(self.details_url, update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_guest_delete_record(self):
        response = self.client.delete(self.details_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class AnotherUserRecordTestCase(RecordBaseTestCase):    
    """ Testing whether another user can interact with another's records """
    
    def setUp(self):
        super().setUp()

        user = User.objects.create(username='another')
        self.client.force_authenticate(user=user)

    def test_can_user_create_anothers_record(self):
        record_data = self.record_data.copy()
        response = self.client.post(self.create_url, record_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_user_view_anothers_record(self):
        response = self.client.get(self.details_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_user_modify_anothers_record(self):
        update_data = self.record_data.copy()
        update_data['name'] = 'Changed name'

        response = self.client.put(self.details_url, update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_user_create_anothers_record(self):
        response = self.client.delete(self.details_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
