from myapp.models import *
from faker import Faker
import random
fake = Faker('en_IN')

def dbSeeder(records = 10)->None:
  # college_name = ['IIT MADRAS','MITIS','VU','SHREERAM','BHU','IIT DELHI']
  # for i in college_name :
  #  address = fake.address()
  #  College.objects.create(
  #    college_name = i ,
  #    college_address = address
  #  )
  colleges = College.objects.all()
  for i in range(records):
    college= random.choice(colleges)
    name = fake.name()
    mobile_number = fake.phone_number()
    age = random.randint(18,25)

    Student.objects.create(
      college=college,
      name=name,
      mobile_number=mobile_number,
      age=age
    )
