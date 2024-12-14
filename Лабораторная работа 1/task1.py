class Glass:
    """
    класс описывает параметры стакана

    """
    def __init__(self, total_vol: int, filled_vol: int):
        """ Инициализация экземпляра класса. """
        self.total_vol = None
        self.filled_vol = None
        self.ini_total_vol(total_vol)
        self.ini_filled_vol(filled_vol)

    def ini_total_vol(self, total_vol: int):
        """
        метод проверяет на соответствие типу int и значению > 0
        :param total_vol: общий обьем стакана в милилитрах

        :return: общий обьем стакана
        """
        if total_vol < 0:
            raise  ValueError("Недопустимое значение, меньше 0")
        if not isinstance(total_vol, int):
            raise TypeError('ошибка типа')
        self.total_vol=total_vol
    def ini_filled_vol(self, filled_vol: int):
        """
        Метод проверяет на соответствие типу int и значению > 0
        :param filled_vol: исхоное наполнение стакана в милилитрах
        :return: исходное наполнение стакана
        """
        if filled_vol < 0:
            raise  ValueError("Недопустимое значение, меньше 0")
        if not isinstance(filled_vol, int):
            raise TypeError('Ошибка типа, должно быть целое положительное число')
        self.filled_vol = filled_vol
    def add_vol(self, add):
        """
        добавление жидкости в стакан
        :param add: обьем долитой жидкости в милилитрах
        если значение привысит обьем, то выдаст сообщение
        :return: текущее наполнение стакана
        """
        self.filled_vol += add
        if self.filled_vol > self.total_vol:
            raise ValueError("Перелив")
        return(self.filled_vol)
class Cat:
    def __init__(self, name: str, weight: float):
        self.name = None
        self.weight = 0
        self.init_name(name)
        self.init_weight(weight)
    def init_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Ошибка типа')
        self.name = name
    def init_weight(self, weight: float):
        if not isinstance(weight, float):
            raise TypeError('Должна быть строка')
        self.weight = weight
        if weight < 0:
            raise ValueError('Отрицательное значение')
        self.weight = weight

class Interface:
    '''
    класс описывает состояние сетевого интерфейса
    '''
    def __init__(self, sysname: str, status: bool):
        """
        инициализация экземпляра
        """
        self.sysname = 'eth'
        self.status = None
        self.init_sysname(sysname)
        self.change_status(status)
    def init_sysname(self, sysname: str):
        '''
        метод задания имени интерфейса
        :param sysname: по умолчанию системное имя eth, в экземплярем
        задается его номер и добавляется к системному имени
        :return:  строковое значение с имененм интерфейса, например eth10
        '''
        if isinstance(sysname, int):
            sysname=str(sysname)
        if not isinstance(sysname, str):
            raise TypeError('Должна быть строка или число изночающее номер интерфейса')
        self.sysname = self.sysname + sysname
    def change_status(self, status: bool):
        '''
        метод описывает состояние интерфейса вкл или выкл
        :param status: принимает булевый тип
        :return: возвращает строку с описанием состояния интерфейса  Up или Down
        '''
        if not isinstance(status, bool):
            raise TypeError('допустимые значения true, false, 1, 0')
        if status == True:
            self.status = "Up"
        else:
            self.status = "Down"

if __name__ == "__main__":
    glass1 = Glass(100, 60)
    print (glass1.total_vol)
    print (glass1.filled_vol)
    print(glass1.add_vol(40))
    cat1 = Cat("Vasja", 3.44)
    print(cat1.weight)
    int = Interface(1, True)
    print(int.sysname)
    print(int.status)
