class Dog:

    def __init__(self, name: str, age: int, master='Dina'):
        self.name = name
        self.age = age
        self.master = master

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def bark(self):
        print(f'{self.name}, quiet!')

    def sleep(self):
        print(f'{self.name}, sleep!')

    def birthday(self):
        return self.age + 1


    def name(self):
        return self.name


    def master(self):
        return self.master


    def age(self):
        return self.age

class Cat:

    def __init__(self, name: str, age: int, master='Dina'):
        self.name = name
        self.age = age
        self.master = master

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def meow(self):
        print(f'{self.name}, do not meow!')

    def sleep(self):
        print(f'{self.name}, sleep!')

    def birthday(self):
        return self.age + 1

    def name(self):
        return self.name


    def master(self):
        return self.master


    def age(self):
        return self.age

class Parrot:

    def __init__(self, name: str, age: int, master='Dina'):
        self.name = name
        self.age = age
        self.master = master

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')

    def fly(self):
        print(f'{self.name}, fly!')

    def sleep(self):
        print(f'{self.name}, sleep!')

    def birthday(self):
        return self.age + 1


    def name(self):
        return self.name


    def master(self):
        return self.master


    def age(self):
        return self.age

dog = Dog('Dog', 2)
print(dog.birthday())
dog.bark()

cat = Cat('Ponka', 7)
print(cat.birthday())
cat.meow()

parrot = Parrot('Kesha', 4)
print(parrot.birthday())
parrot.fly