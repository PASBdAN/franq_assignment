import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Checking database connectivity!')
        client = None
        count = 0
        while not client:
            try:
                client = connections['default']
            except OperationalError:
                count+=1
                self.stdout.write(f'Could not connect to the database, trying again ({count})')
                time.sleep(1)
        self.stdout.write('Connection successfully done!')
