import os
import uuid
import tempfile
import pandas as pd
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Account

class CSVUploadViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('imports-accounts')

    def test_upload_csv_file(self):
        # Create a temporary CSV file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
        try:
            df = pd.DataFrame({
                'ID': [str(uuid.uuid4()), str(uuid.uuid4())],
                'Name': ['John Doe', 'Jane Doe'],
                'Balance': [1234.56, 7890.12]
            })
            df.to_csv(temp_file.name, index=False)
            temp_file.seek(0)

            with open(temp_file.name, 'rb') as csvfile:
                response = self.client.post(self.url, {'file': csvfile}, format='multipart')

            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Account.objects.count(), 2)
        finally:
            os.remove(temp_file.name)

class CustomerListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('accounts')
        self.customer1 = Account.objects.create(id=uuid.uuid4(), owner_name='John Doe', balance=1234.56)
        self.customer2 = Account.objects.create(id=uuid.uuid4(), owner_name='Jane Doe', balance=7890.12)

    def test_get_customers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['owner_name'], self.customer1.owner_name)
        self.assertEqual(response.data[1]['owner_name'], self.customer2.owner_name)
        
        
        
class AccountDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Account.objects.create(id=uuid.uuid4(), owner_name='John Doe', balance=1234.56)
        # Convert UUID to string before passing to reverse
        self.url = reverse('account-detail', args=[str(self.customer.id)])

    def test_get_customer_detail(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['owner_name'], self.customer.owner_name)
        self.assertEqual(response.data['balance'], str(self.customer.balance))

    def test_get_nonexistent_customer(self):
        url = reverse('account-detail', args=[str(uuid.uuid4())])  # Convert UUID to string
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        
        
class TransferFundsViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sender = Account.objects.create(id=uuid.uuid4(), owner_name='Sender', balance=5000.00)
        self.receiver = Account.objects.create(id=uuid.uuid4(), owner_name='Receiver', balance=1000.00)
        self.url = reverse('transfer_funds')

    def test_transfer_funds_success(self):
        data = {
            "sender_id": str(self.sender.id),
            "receiver_id": str(self.receiver.id),
            "amount": 1000.00
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Transfer completed successfully")

        self.sender.refresh_from_db()
        self.receiver.refresh_from_db()
        self.assertEqual(self.sender.balance, 4000.00)
        self.assertEqual(self.receiver.balance, 2000.00)

    def test_transfer_funds_insufficient_balance(self):
        data = {
            "sender_id": str(self.sender.id),
            "receiver_id": str(self.receiver.id),
            "amount": 6000.00  # More than sender's balance
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Insufficient funds')

    def test_transfer_funds_missing_fields(self):
        data = {
            "sender_id": str(self.sender.id),
            "amount": 1000.00
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Missing required fields')

    def test_transfer_funds_invalid_uuid(self):
        data = {
            "sender_id": "invalid-uuid",
            "receiver_id": str(self.receiver.id),
            "amount": 1000.00
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
