import time
from django.db import  connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    '''pause execution while the database is ready'''
    def handle(self,*args, **kwargs):
        self.stdout.write('Wating for connection')
        db_conn =None
        while not db_conn:
            try:
                db_conn=connections['default']
            except OperationalError:
                self.stdout.write('waiting for database .......')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database avalible'))           