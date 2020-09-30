import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()


from AppTwo.models import Users
from faker import Faker

fakegen = Faker()


def populate(N=5):

    for i in range(N):

        # create the fake data for entry
        # using Faker class methods to generate different data types

        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        u = Users.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]



if __name__ == '__main__':
    print('Running population script for AppTwo')
    populate(10)
    print('Populating complete!')
