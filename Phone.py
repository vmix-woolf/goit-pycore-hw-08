from Field import Field
from Exceptions import ExactDigitException
import constants

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = value
    
    def validation_phone(phone_number)-> bool:
        try:
            if len(phone_number) == constants.DIGITS_IN_PHONE_NUMBER and phone_number.isdigit():
                return True
            else:
                raise ExactDigitException()
        except ExactDigitException:
            return False
