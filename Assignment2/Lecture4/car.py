class Car:
    def __init__(self, brand, make):
        self.__model = brand
        self.__make = make

    def set_make(self, make):
        self.__make = make

    def get_make(self):
        return self.__make

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def __str__(self):
        return ' '.join([self.__make, self.__model])
