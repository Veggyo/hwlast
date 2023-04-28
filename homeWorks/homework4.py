class Name:
    def __int__(self, name):
        self.name = name
class Age:
    def __init__(self, age):
        self.age = age

class Year:
    def ad(self):
        add = input(f'enter ur birth year: ')
        year = 2023
        return f'your age: {year - int(add)}'

class Date:
    def ads(self):
        ad = int(input(f'enter ur birth month: '))
        now = int(input(f'enter month now: '))
        return f'moths before your bd: {ad - now}'

class Fifth(Name, Age, Year, Date):
    def __init__(self, name, age):
        Name.__init__(name)
        Age.__init__(self, age)

    @property
    def get_age(self):
        return self.age

    @get_age.setter
    def get_age(self, age):
        self.__age = age

    def __str__(self):
        return f'name: {self.name}, age: {self.__age}'

user = Fifth('Adelina', 16)
print(Fifth.ad(user))
print(Fifth.ads(user))
