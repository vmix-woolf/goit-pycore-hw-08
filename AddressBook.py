from collections import UserDict
from datetime import datetime as dt, timedelta


class AddressBook(UserDict):
    current_id = 1

    def add_record(self, record):
        self.data[AddressBook.current_id] =  record
        AddressBook.current_id += 1

   
    def find(self, user_name):
        for _, user in self.data.items():
            if user.name.value == user_name:
                return user

    
    def delete(self, user_name):
        {key: value for key, value in self.data.items() if value.name.value != user_name}
