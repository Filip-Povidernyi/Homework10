from collections import UserDict


class Field:
    
    def __init__(self, value):
        self.value = value


class Name(Field):

    pass


class Phone(Field):

    pass

class Email(Field):

    pass

class Record:
    
    def __init__(self, name, phone=None, email=None):
        self.name = name
        self.phones = []
        self.emails = []
        if phone:
            self.phones.append(phone)
        if email:
            self.emails.append(email)

    def add_phone(self, phone):

        if not isinstance(phone, Phone):
            raise ValueError("Phone must be an instance of Phone class")
            self.phones.append(phone)

    def remove_phone(self, phone):

        if not isinstance(phone, Phone):
            raise ValueError("Phone must be an instance of Phone class")
            self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):

        if not isinstance(old_phone, Phone) or not isinstance(new_phone, Phone):
            raise ValueError("Phone must be an instance of Phone class")
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone

    def add_email(self, email):

        if not isinstance(email, Email):
            raise ValueError("E-mail must be an instance of Email class")
            self.emails.append(email)

    def remove_email(self, email):

        if not isinstance(email, Email):
            raise ValueError("E-mail must be an instance of Email class")
            self.emails.remove(email)

    def edit_phone(self, old_email, new_email):

        if not isinstance(old_email, Email) or not isinstance(new_email, Email):
            raise ValueError("E-mail must be an instance of Email class")
            index = self.emails.index(old_email)
            self.emails[index] = new_email
    
class AddressBook(UserDict):


    def add_record(self, record):
        self.data[rec.name.value] = record
        print(self.data)


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    email = Email('example@gmail.com')
    rec = Record(name, phone, email)
    ab = AddressBook()
    ab.add_record(rec)
    
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    
    print('All Ok)')