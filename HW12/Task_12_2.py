class Car:
    def __init__(self, brand:str, model:str = None, issued:int = None, speed:int = 0):
        self.__brand = brand
        self.__model = model
        self.__issued = issued
        self.__speed = speed

    def increase_speed(self):
        return self.__speed + 5

    def decrease_speed(self):
        return self.__speed - 5

    def stop(self):
        self.__speed = 0
        return self.__speed

    def speed_display(self):
        print(self.__speed)

