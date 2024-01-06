# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class Balloon:

    def __init__(self, volume: Union[int, float], diameter: Union[int, float]):
        """

    :param volume: объем воздуха в шаре
    :param diameter: диаметр шара

    Примеры:
        >>> balloon = Balloon(500, 100) #инициализация экземпляра класса

       """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем шара должен быть типа int или float")
        if not volume >= 0:
            raise ValueError("Объем шара не может быть меньше нуля")
        self.volume = volume

        if not isinstance(diameter, (int, float)):
            raise TypeError("Диаметр должен быть int или float")
        if diameter < 0:
            raise ValueError("Диаметр не может быть отрицательным числом")
        self.diameter = diameter

    def add_air_to_balloon(self, air: Union[int, float]) -> None:
        """
        Добавление воздуха в шар
        :param air: добавляемый воздух

        :raise ValueError: Если количество добавляемого воздуха превышает свободное место в шаре, то вызываем ошибку
        :return новый объем шара
        Примеры:
        >>> balloon = Balloon(500, 150)
        >>> balloon.add_air_to_balloon(50)
        """
        if not isinstance(air, (int, float)):
            raise TypeError("Добавляемый воздух должен быть размерности int или float")
        if not air > 0:
            raise ValueError("Объем добавляемого воздуха должен быть больше нуля")

        ...

    def remove_air_from_balloon(self, air: Union[int, float]) -> None:
        """
        Удаление воздуха из шара
        :param air: выпускаемый воздух

         :raise ValueError: Если количество удаляемого воздуха превышает объем воздуха в шаре, то вызываем ошибку
         :return новый объем шара
        Примеры:
        >>> balloon = Balloon(500, 150)
        >>> balloon.remove_air_from_balloon(50)
        """

        if not isinstance(air, (int, float)):
            raise TypeError("Удаляемый воздух должен быть размерности int или float")
        if not air > 0:
            raise ValueError("Объем удаляемого воздуха должен быть больше нуля")

    ...


if __name__ == "__main__":
    doctest.testmod()


class DebitCard:
    def __init__(self, amount_of_money: Union[int, float], card_maintenance: int):
        """

        :param amount_of_money: кол-во денег на карте
        :param card_maintenance: плата за обслуживание

        Пример:
        >>> card = DebitCard(10000, 100) #инициализация экземпляра класса
        """
        if not isinstance(amount_of_money, (int, float)):
            raise TypeError("Количество денег на карте должно быть типа int или float")
        if not amount_of_money >= 0:
            raise ValueError("Количество денег на карте не может быть меньше нуля")

        if not isinstance(card_maintenance, (int, float)):
            raise TypeError("Плата за обслуживание должна быть типа int или float")
        if not card_maintenance >= 0:
            raise ValueError("Плата за обслуживание не может быть меньше нуля")

    def add_money_to_card(self, money: Union[int, float]) -> Union[int, float]:
        """
        Функция осуществляет пополнение карты
        :param money: сумма добавленных денег
        :return: новая сумма средств на карте

        Примеры:
        >>> card1 = DebitCard(5000, 200)
        >>> card1.add_money_to_card(4000)
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Сумма пополнения должна быть типа int или float")
        if money <= 0:
            raise ValueError("Сумма пополнения не может быть меньше нуля")
        ...

    def withdraw_money_from_card(self, money: Union[int, float]) -> Union[int, float]:
        """
        Функция осуществляет снятие денег с карты
        :param money: сумма снятия
        :return: новая сумма средств на карте

        Пример:
        >>> card1 = DebitCard(7500, 100)
        >>> card1.withdraw_money_from_card(3000)
        """

        if not isinstance(money, (int, float)):
            raise TypeError("Сумма снятия должна быть типа int или float")
        if money <= 0:
            raise ValueError("Сумма снятия не может быть меньше нуля")
        ...

    def tariff_change(self, price_change: int) -> int:
        """
        Функция осуществляет переход на более дорогой или дешевый тариф
        :param price_change: новая сумма тарифа
        :return: новая плата за тариф

        Пример:
    >>> card1 = DebitCard(10000, 500)
    >>> card1.tariff_change(300)
        """
        if not isinstance(price_change, int):
            raise TypeError("Сумма тарифа должна быть типа int или float")
        if price_change <= 0:
            raise ValueError("Плата за тариф не может быть меньше нуля")
        ...


if __name__ == "__main__":
    doctest.testmod()


class PhotoAlbum:
    def __init__(self, amount_of_sections: int, amount_of_photos: int, amount_of_pages: int):
        """

        :param amount_of_sections: общее количество секций для размещения фотографий в альбоме
        :param amount_of_photos: количество фото, в данный момент находящееся в альбоме
        :param amount_of_pages: количество страниц в альбоме

           Пример:
            >>> album = PhotoAlbum(100, 50, 25)

         """

        if not isinstance(amount_of_sections, int):
            raise TypeError("Количество мест в альбоме должно быть типа int")
        if not amount_of_sections >= 0:
            raise ValueError("Количество мест в альбоме не может быть меньше нуля")

        if not isinstance(amount_of_photos, int):
            raise TypeError("Количество фотографий в альбоме должно быть типа int")
        if not amount_of_photos >= 0:
            raise ValueError("Количество фотографий в альбоме не может быть меньше нуля")

        if not isinstance(amount_of_pages, int):
            raise TypeError("Количество cтраниц в альбоме должно быть типа int")
        if not amount_of_photos >= 0:
            raise ValueError("Количество cтраниц в альбоме не может быть меньше нуля")

    def is_empty_album(self) -> bool:
        """
        Функция проверяет, есть ли фотографии в альбоме
        :return: Является ли альбом пустым

        Пример:
        >>> album = PhotoAlbum(100, 50, 25)
        >>> album.is_empty_album()
        """
        ...

    def free_pages_in_album(self, photos_for_page: int) -> int:
        """
        Функция показывает, сколько целых пустых страниц осталось в альбоме
        :param photos_for_page: количество фотографий на странице
        :return: количество целых свободных страниц в альбоме

        Пример:
        >>> album = PhotoAlbum(100, 50, 25)
        >>> album.free_pages_in_album(4)

        """

        if not isinstance(photos_for_page, int):
            raise TypeError("Количество фотографий на странице должно быть типа int")
        if not photos_for_page >= 0:
            raise ValueError("Количество фотографий на странице  не может быть меньше нуля")
        ...

if __name__ == "__main__":
    doctest.testmod()





