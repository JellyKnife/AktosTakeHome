from django.test import TestCase, Client
from accounts.models import Account
from django.core.management import call_command
import os


class AccountTests(TestCase):

  def setUp(self):
    # Create some test data
    Account.objects.create(consumer_name='John Doe',
                           balance=100.00,
                           status='in_collection')
    Account.objects.create(consumer_name='Jane Doe',
                           balance=200.00,
                           status='collected')

  def test_ingest_csv(self):
    # Test the CSV ingestion command
    call_command(
        'read_csv',
        '/home/runner/AktosTakeHome/collection_agency/csv_files/consumers_balances.csv'
    )
    self.assertEqual(Account.objects.count(), 1002)

  def test_get_accounts(self):
    client = Client()

    # Test without filters
    response = client.get('/accounts')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.json()), 2)

    # Test with min_balance filter
    response = client.get('/accounts?min_balance=150')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.json()), 1)

    # Test with consumer_name filter
    response = client.get('/accounts?consumer_name=John')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.json()), 1)

    # Test with status filter
    response = client.get('/accounts?status=collected')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.json()), 1)
