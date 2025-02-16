if __name__ == "__main__":
    # Write your solution here
    pass
class Auto:
    """
    Базовый класс, представляющий автомобиль.
    """
    def __init__(self, model: str, weight: float, color: str) -> None:
        """
        Конструктор класса Auto.
        Args:
            model: Модель автомобиля - строковый тип.
            weight: Вес автомобиля в килограммах - float.
            color: Цвет автомобиля - строковый тип.
        """
        self._model = model #модель изменит нельзя
        self._weight = weight  # Используем _weight для внутреннего хранения
        self.color = color

    def __str__(self) -> str:
        """
        Возвращает строковое представление об обьекте для пользователя приложением.
        """
        return f"{self.__class__.__name__}: {self.model}, {self.color}, {self.weight} кг"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление об объекте для разработчиков приложения.
        """
        return f"{self.__class__.__name__}(model='{self.model}', weight={self.weight}, color='{self.color}')"

    @property
    def weight(self) -> float:
        """
        Getter для веса.
        возвращает:  Вес автомобиля.
        """
        return self._weight

    @weight.setter
    def weight(self, new_weight: float) -> None:
        """
        Setter для веса. Может быть переопределен в подклассах для валидации.
        """
        self._weight = new_weight

    def change_color(self, new_color: str) -> None:
        """
        Изменяет цвет автомобиля.
        Args:
            new_color: Новый цвет автомобиля.
        """
        self.color = new_color
        print(f"Цвет автомобиля изменен на {new_color}")

    @property
    def model(self) -> str:
        """
        Getter для. модели автомобиля.
        """
        return self._model


class Car(Auto):
    """
    Класс легковой автомобиль, наследник класса Auto.
    """

    MAX_WEIGHT: float = 3500.0  # Максимальный вес легкового автомобиля

    def __init__(self, model: str, weight: float, color: str) -> None:
        """
        Конструктор класса Car.
        Args:
            model: Модель автомобиля.
            weight: Вес автомобиля в килограммах.
            color: Цвет автомобиля.
        """
        super().__init__(model, weight, color)
        self.weight = weight

    @Auto.weight.setter  # Используем декоратор от базового класса
    def weight(self, new_weight: float) -> None:
        """
        Setter для веса с валидацией.

        Args:
            new_weight: Новый вес автомобиля.

        Raises:
            ValueError: Если вес превышает допустимый предел.
        """
        if new_weight > Car.MAX_WEIGHT:
            raise ValueError(f"Вес легкового автомобиля не может превышать {Car.MAX_WEIGHT} кг")
        self._weight = new_weight

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта для пользователя (перегрузка).
        """
        return f"Легковой автомобиль: {self.model}, {self.color}, {self.weight} кг"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для разработчика (перегрузка).
        """
        return f"Car(model='{self.model}', weight={self.weight}, color='{self.color}')"


class Truck(Auto):
    """
    Класс грузовой автомобиль. Наследуется от класса Auto.
    """

    MIN_WEIGHT: float = 3500.0  # Минимальный вес грузового автомобиля

    def __init__(self, model: str, weight: float, color: str) -> None:
        """
        Конструктор класса Truck.

        Args:
            model: Модель автомобиля.
            weight: Вес автомобиля в килограммах.
            color: Цвет автомобиля.
        """
        super().__init__(model, weight, color)
        self.weight = weight

    @Auto.weight.setter  # Используем декоратор от базового класса
    def weight(self, new_weight: float) -> None:
        """
        Setter для веса с валидацией.

        Args:
            new_weight: Новый вес автомобиля.

        Raises:
            ValueError: Если вес меньше допустимого предела.
        """
        if new_weight < Truck.MIN_WEIGHT:
            raise ValueError(f"Вес грузового автомобиля должен быть не менее {Truck.MIN_WEIGHT} кг")
        self._weight = new_weight

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта для пользователя (перегрузка).
        """
        return f"Грузовой автомобиль: {self.model}, {self.color}, {self.weight} кг"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для разработчика (перегрузка).
        """
        return f"Truck(model='{self.model}', weight={self.weight}, color='{self.color}')"


# Пример использования
car = Car("Renault Capture", 1800.0, "Green")
print(car)
print(repr(car))

truck = Truck("MAN TGS ", 7000.0, "White")
print(truck)
print(repr(truck))

car.change_color("Blue")
print(car)

car.weight = 2000.0
print(car)


#car1 = Car("Жигули", 4000.0, "Black")  #  вызовет ValueError
#print(car_invalid)
#car1.weight = 4000
truck1 = Truck("Камаз", 2000.0, "Red")  #  вызовет ValueError
print(truck2)

car.weight = 5000.0 # Вызовет ValueError
