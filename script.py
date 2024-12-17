import os
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = "check.settings"
django.setup()
import django
from myapp.models import Person
from faker import Faker

fake=Faker()

def Createperson(number):
  create=[Person(person_name=fake.name())for _ in range(number)]
  Person.objects.bulk_create(create)

# Createperson(1000)



def updatePerson(name):
  Person.objects.filter(person_name__icontains=name).count()

updatePerson("Richard")


def deleteperson(number):
  for _ in range(number):
    Person.objects.all().delete()

# deleteperson(1000)




