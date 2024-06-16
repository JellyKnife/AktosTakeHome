# accounts/management/commands/ingest_csv.py

import csv
from django.core.management.base import BaseCommand
from accounts.models import Account


class Command(BaseCommand):
    help = 'Ingest a CSV file of accounts'

    def add_arguments(self, parser):
        parser.add_argument('csv_file',
                            type=str,
                            help='The path to the CSV file to be ingested')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        with open(csv_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Account.objects.create(
                    client_ref_no=row['client reference no'],
                    balance=row['balance'],
                    status=row['status'],
                    consumer_name=row['consumer name'],
                    consumer_address=row['consumer address'],
                    ssn=row['ssn'])

        self.stdout.write(self.style.SUCCESS('Successfully ingested CSV data'))
