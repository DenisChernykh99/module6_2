class Vehicle:
    def __init__(self, owner, model, engine_power, color):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)
        self._COLOR_VARIANTS = ['red', 'blue', 'green', 'yellow', 'pink']

    def get_model(self):
        return f'Модель транспорта: {self.__model}'

    def get_horsepower(self):
        return f'Мощьность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(f'{self.get_model()}\n'
              f'{self.get_horsepower()}\n'
              f'{self.get_color()}\n'
              f'Владелец: {self.owner}'
              )

    def set_color(self, new_color):
        self.new_color = str.lower(new_color)
        if self.new_color not in self._COLOR_VARIANTS:
            print(f'Нельзя изменить цвет на: {new_color}')
        else:
            self.__color = new_color


class Sedan(Vehicle):
    __PASSENGER_LIMIT = 5


# текущие цвета _COLOR_VARIANTS = ['red', 'blue', 'green', 'yellow', 'pink']
if __name__ == "__main__":
    Vehicle1 = Sedan('Vasya', 'Tesla Model Y', 500, 'red')
    # изначальные свойства
    Vehicle1.print_info()

    # Меняем свойства
    Vehicle1.set_color('White')
    Vehicle1.set_color('GrEEn')
    Vehicle1.owner = 'Petya'

    # проверяем новые свойства
    Vehicle1.print_info()
