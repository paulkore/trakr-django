"""
This is a data migration script for the following schema update:

---
New table: mt_allccations
---

The script creates allocations for every expense record in the event,
assuming that all expense records apply to the entire group.

"""
from django.db import transaction

from trakr.models import Event, Participant, Allocation, MoneyRecordType, AllocationType


def run():
    migrate_data()
    print('Kthxbai.')


def migrate_data():
    with transaction.atomic():

        events = Event.objects.all()

        for event in events:
            print('\nProcessing event: ' + event.name)

            participants = event.participants()
            print('Participants: ' + str(len(participants)))

            money_records = event.money_records()
            print('Records: ' + str(len(money_records)))

            expenses = 0
            transfers = 0
            allocations = 0

            for money_record in money_records:
                if money_record.type == MoneyRecordType.TRANSFER:
                    # skip transfer
                    transfers += 1
                else:
                    expenses += 1
                    for participant in participants:
                        allocation = Allocation.objects.create(
                            money_record=money_record,
                            participant=participant,
                            type=AllocationType.EQUAL,
                            amount=None)
                        allocation.save()
                        allocations += 1

            print ('Allocations (new): ' + str(allocations))

