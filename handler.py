import constants
from datetime import datetime as dt, timedelta
from decorations import input_error
from AddressBook import AddressBook
from Record import Record
from Phone import Phone
from Birthday import Birthday
from Exceptions import (
    ExactDigitException, 
    NoSuchPhoneNumberError, 
    NoSuchContactException,
    ContactHasBirthdayException,
    InvalidDateFormatError
)


@input_error
def add_contact(args, book: AddressBook):
    name, phone_number, *_ = args
    record = book.find(name)
    
    if record is None:  # if such name is new
        if Phone.validation_phone(phone_number):
            record = Record(name)
            book.add_record(record)
            record.add_phone(phone_number)
            
            return constants.CONTACT_ADDED
        else:
            raise ExactDigitException()
    else :  # continue if such name is already kept
        if record.find_phone(phone_number):
            return constants.PHONE_IS_IN_BOOK
        else:
            record.add_phone(phone_number)
        
            return constants.CONTACT_UPDATED
    


@input_error
def change_contact(args, book):
    name, old_phone_number, new_phone_number, *_ = args
    record = book.find(name)
    
    if record is None:
        raise IndexError

    if record.find_phone(old_phone_number):
        if Phone.validation_phone(new_phone_number):
            record.edit_phone(old_phone_number, new_phone_number)
        else:
            raise ExactDigitException()
    else:
        raise NoSuchPhoneNumberError()
    
    return constants.CONTACT_UPDATED


@input_error
def show_phone(args, book):
    name, *_ = args
    record = book.find(name)
    
    if record is None:
        raise IndexError
    else:
        return f"{record.name.value} has the following phone numbers: {'; '.join(p for p in record.phones)}."


@input_error
def add_birthday(args, book):
    name, date_of_birth, *_ = args
    record = book.find(name)
    
    if record is None:
        raise IndexError
    else:
        if record.birthday is None:  # if such name is new
            if Birthday.validation_birthday(date_of_birth):
                record.add_birthday(date_of_birth)
                
                return constants.CONTACT_UPDATED
            else:
                raise InvalidDateFormatError
        else:
            raise ContactHasBirthdayException


@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
        
    if record is None:
        raise IndexError
    else:
        if record.name.value == name:
            return f"{record.name.value} has the following birthday: {record.birthday.value}"
        else:
            raise NoSuchContactException()
    

@input_error
def birthdays(book):
    if len(book) == 0:
        print(constants.CONTACT_LIST_EMPTY)
    else:
        upcoming_birthdays = []
        today = dt.today().date()
        
        for user in book.values():
            bd_date = dt.strptime(user.birthday.value, "%d.%m.%Y")
            # birthday_this_year = (dt.strptime(bd_date, "%d.%m.%Y")).date().replace(year=today.year)
            birthday_this_year = bd_date.date().replace(year=today.year)
            
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)  

            if (birthday_this_year - today).days < 7:
                if birthday_this_year.weekday() < 5:  # weekday
                    upcoming_birthday = {
                        "name": user.name.value,
                        "congratulation_date": dt.strftime(birthday_this_year, '%d.%m.%Y')
                    }
                elif birthday_this_year.weekday() == 5:  # Saturday
                    upcoming_birthday = {
                        "name": user.name.value,
                        "congratulation_date": dt.strftime(birthday_this_year + timedelta(days=2), '%y.%m.%d')
                    }   
                else:  # Sunday
                    upcoming_birthday = {
                        "name": user.name.value,
                        "congratulation_date": dt.strftime(birthday_this_year + timedelta(days=1), '%y.%m.%d')
                    }
            else: 
                continue

            upcoming_birthdays.append(upcoming_birthday)

        if upcoming_birthdays:
            print(constants.TITLE_TO_CONGRATULE)
            for item in upcoming_birthdays:
                print(f"Contact {item['name']} should be mailed {item['congratulation_date']}")
        else:
            print(constants.NO_NECESSARY_TO_CONGRATULATE)


@input_error
def show_all(book):
    if len(book) == 0:
        print(constants.CONTACT_LIST_EMPTY)
    else:
        for _, item in book.items():
            print(item)
