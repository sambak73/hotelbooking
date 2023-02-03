


class User:

    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        return self.name.upper()

    def age(self, current_year):
        age = current_year - self.birthyear
        return age

user1 = User('John', 1999)
user1_age = user1.age(2023)
print(user1_age)
print(user1.get_name())