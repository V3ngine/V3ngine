from django.core.management.base import BaseCommand
from faker import Faker
from gum.models import CreateUsers

   
class Command(BaseCommand):
    help = 'Create users from Faker'
   
    



    def handle(self, *args, **options) :
        fake = Faker()
       
        for i in range(8):
            CreateUsers.objects.create(name=fake.name(),
            password=fake.password(),mail=fake.email())
        return "Hello" 
 