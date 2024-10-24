from datetime import datetime
from Field import Field
from decorations import input_error
from Exceptions import InvalidDateFormatError
import re

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value

    def validation_birthday(date_of_birth)-> bool:
        if bool(re.match(r'\d{2}\.\d{2}\.\d{4}', date_of_birth)):
            if datetime.strptime(date_of_birth, '%d.%m.%Y'):
                return True
            else:
                raise ValueError
        else:
            raise InvalidDateFormatError   
       
