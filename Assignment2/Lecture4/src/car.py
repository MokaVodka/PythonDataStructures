class Car:
    def __init__(self, make, model):
        self.set_make(make)
        self.set_model(model)

    def set_make(self, make):
        if make is None or type(make) is not str:
            raise ValueError('Make must be a string')
        self.__make = make

    def get_make(self):
        return self.__make

    def set_model(self, model):
        if model is None or type(model) is not str:
            raise ValueError('Model must be a string')
        self.__model = model

    def get_model(self):
        return self.__model

    def __str__(self):
        return ' '.join([self.__make, self.__model])


# -- Example program --
def example():
    models = ['XC90', 'V60', 'S90']
    cars = [Car('Volvo', model) for model in models]

    print('Original car list:')
    for car in cars:
        print(car)
    print('')

    cars[1].set_model('XC60')

    print('After modyfing second car:')
    for car in cars:
        print(car)


try:
    example()
except Exception as e:
    print(f'An error occured: {e}')
