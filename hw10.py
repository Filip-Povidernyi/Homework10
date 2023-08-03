from collections import UserDict

class Name:

    def __init__(self, name):
        self.name = name


class Field:
    pass

class Phone:

    def __init__(self, phone):
        self.phone = phone

class Record:
    
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phone = Phone(phone)

    def save(self):
        pass

    
class AddressBook(UserDict):


    def add_record(self, record):
        self.data[Record.name.value] = record



if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    
    print('All Ok)')