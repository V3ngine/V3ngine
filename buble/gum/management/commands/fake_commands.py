from tkinter.font import names
from unicodedata import name
from django.core.management.base import BaseCommand, CommandError
from gum.models import CreateUsers
from faker import Faker


class Command(BaseCommand):
    help = 'Create users from Faker'

    
    
        
   

    def handle(self, *args, **kwargs):
        
        fake_users = CreateUsers()
        fake = Faker()
        names = []
        

        for i in range(3):
                names.append([[fake.name()],[fake.email()], [fake.password()]]) 
        

        for i in range(3):
            print(f'{i} + cool')
            for k in range(3):
                names[i][k]
                print(i,k)
        
       
        
            
            
           
      
            
