from faker import Faker
from .models import CreateUsers



class FakeUser:
    fake = Faker()
    fake_user = CreateUsers()
    

    def create(self):
        for i in range(40):
            self.fake_user.name = self.fake.name()
            self.fake_user.password =self.fake.password()
            self.fake_user.mail = self.fake.email()
            self.fake_user.save()
    
# print(fake_user)
 