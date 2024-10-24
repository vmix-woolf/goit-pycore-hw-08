import constants
from Exceptions import (
    ExactDigitException,
    NoSuchPhoneNumberError,
    ContactInBookError,
    ContactHasBirthdayException,
    NoSuchContactException,
    InvalidDateFormatError
)

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return constants.VALUE_ERROR
        except KeyError:
            return constants.KEY_ERROR
        except IndexError:
            return constants.INDEX_ERROR
        except ExactDigitException:
            return constants.DIGITS_ERROR
        except NoSuchPhoneNumberError:
            return constants.NO_PHONE_NUMBER
        except ContactInBookError:
            return constants.CONTACT_IS_IN_BOOK
        except ContactHasBirthdayException:
            return constants.CONTACT_HAS_BIRTHDAY
        except NoSuchContactException:
            return constants.NO_SUCH_CONTACT
        except InvalidDateFormatError:
            return constants.INVALID_FORMAT_ERROR

    return inner
