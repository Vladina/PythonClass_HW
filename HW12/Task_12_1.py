class Planet:
    def __init__(self, name: str, distance: int = None, size: int = None, system: str = 'Solar'):
        self.__name = name
        self.__distance = distance
        self.__size = size
        self.__system = system

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system: str):
        self.__system = system

    def is_far(self):
        if self.__distance > 10000:
            print(f'{self.__name} is too far from Earth!')
        else:
            pass

    def beautiful(self):
        print(f'The {self.__name} is beautiful')


class Tree:
    def __init__(self, name: str, av_height: int = None, continent: str = 'Eurasia'):
        self.__name = name
        self.__av_height = av_height
        self.__continent = continent

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def av_height(self):
        return self.__av_height

    @av_height.setter
    def av_height(self, av_height: int):
        self.__av_height = av_height

    @property
    def continent(self):
        return self.__continent

    @continent.setter
    def continent(self, continent: str):
        self.__continent = continent

    def water(self):
        if self.__continent == 'Africa':
            print(f"{self.__name} does need lot's of water")

    def blossom(self):
        print(f'Enjoy the blossom time of {self.__name}')



class Animal:
    def __init__(self, name: str, is_predator: bool = True, color: str = 'Grey'):
        self.__name = name
        self.__predator = is_predator
        self.__color = color

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def is_predator(self):
        return self.__predator

    @is_predator.setter
    def is_predator(self, is_predator: bool):
        self.__predator = is_predator

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    def danger(self):
        if self.__predator is True:
            print(f'{self.__name} bites!')
        if self.__name == 'Snake' or self.__name == 'Spider':
            print("This can be poisonous!")



class House:
    def __init__(self, address: str, material: str = 'Brick', storeys: int = 2):
        self.__address = address
        self.__material = material
        self.__storeys = storeys

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, material: str):
        self.material = material

    @property
    def storeys(self):
        return self.__storeys

    @storeys.setter
    def storeys(self, storeys: int):
        self.__storeys = storeys

    def elevator(self):
        if self.__storeys >= 3:
            print('You might need an elevator')

    def address(self):
        print('Your lucky location!')



class Currency:
    def __init__(self, country: str, amount: int, change_rate: int):
        self.__country = country
        self.__amout = amount
        self.__change_rate = change_rate

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def amount(self):
        return self.__amout

    @amount.setter
    def amount(self, amount: int):
        self.amount = amount

    @property
    def change_rate(self):
        return self.__change_rate

    @change_rate.setter
    def change_rate(self, change_rate: int):
        self.__change_rate = change_rate

    def to_rubles(self):
        return self.__amout * self.__change_rate

    def rent(self):
        if self.__amout <= 200:
            print('Sorry, you cannot afford to rent a house')
        else:
            print('Change your currency to rubles first')