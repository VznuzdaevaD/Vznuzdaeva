class Plane: #Класс "Самолет"
    def __init__(self, name: str, speed: int):
        self.name = name
        self._speed = speed  # Скорость самолета нежелательно менять

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r}, скорость {self._speed!r}) '

    def __str__(self) -> str:
        return f'Самолет "{self.name}" с максимальной скоростью {self._speed} км/ч. '

    # Публичный метод, который внутри работает с защищенным атрибутом self._speed
    def change_speed(self, new_speed: int) -> None:  # Задает новую скорость самолета
        if not isinstance(new_speed, int):
            raise TypeError("Скорость должна быть типа int")

        if new_speed <= 0:
            raise ValueError("Скорость должна быть положительным числом")

        self._speed = new_speed

    def type_assignment(self, plane_type: str) -> str:  # Добавляет тип модели самолета
        if len(plane_type) > 5:
            raise ValueError("Наименование типа может включать до 5 знаков")

        if not isinstance(plane_type, str):
            raise TypeError("Наименование типа должно быть строкой")
        return f'{self.name} {plane_type}'  # Возвращает наименование модели с её типом



class PassengerPlane(Plane):  # Класс "Пассажирский самолёт"
    def __init__(self, name: str, speed: int, number_of_passengers: int):
        super().__init__(name, speed)
        self.number_of_passengers = number_of_passengers

    def __repr__(self) -> str:
        return super.__repr__(self) + f' с количеством пассажиров "{self.number_of_passengers}"'

    def __str__(self) -> str:
        return super().__str__() + f'Максимальное количество пассажирских мест {self.number_of_passengers}.'

    def type_assignment(self, plane_type: int) -> str:
        if len(str(plane_type)) > 3:
            raise ValueError("Наименование типа может включать до 3 знаков")

        if not isinstance(plane_type, int):
            raise TypeError("Наименование типа должно быть числом")
        return f'{self.name} {plane_type}'


if __name__ == "__main__":
    print(Plane("Boeing", 70))

    plane1 = PassengerPlane("Airbus", 100, 250)
    print(plane1)
    # применяем метод для смены скорости
    plane1.change_speed(139)
    print(plane1)
    # применяем метод для добавления типа модели
    print(plane1.type_assignment(352))
