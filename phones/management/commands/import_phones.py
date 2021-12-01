import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phones = csv.reader(csvfile, delimiter=';')
            next(phones)

            for phone in phones:
                phone_bd = Phone(
                    id=phone[0],
                    name=phone[1],
                    image=phone[2],
                    price=phone[3],
                    release_date=phone[4],
                    lte_exists=phone[5]
                )
                phone_bd.save()

