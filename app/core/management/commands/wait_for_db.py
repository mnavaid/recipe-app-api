"""
Django command to ait for the Db to be available
"""
import time
from psycopg2 import OperationalError as psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the DB"""

    def handle(self, *args, **options):
        """Entry point for Command."""
        self.stdout.write("Waiting for Database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(psycopg2OpError, OperationalError):
                self.stdout.write("Database unavailable. && \
                                    Wait for 1 second!")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database is available!"))
