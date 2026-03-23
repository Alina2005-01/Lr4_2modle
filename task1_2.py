class Employee:
    """
    Базовый класс для сотрудников.

    Атрибуты:
        _first_name (str): Имя сотрудника (непубличный).
        _last_name (str): Фамилия сотрудника (непубличный).
        _salary (float): Зарплата сотрудника (непубличный).

    Методы:
        __init__(first_name, last_name, salary): Конструктор.
        __str__(): Строковое представление для пользователя.
        __repr__(): Строковое представление для отладки.
        get_full_name(): Возвращает полное имя.
        calculate_bonus(): Возвращает сумму бонуса (10% от зарплаты).
    """

    def __init__(self, first_name: str, last_name: str, salary: float) -> None:
        """
        Инициализация сотрудника.

        :param first_name: Имя сотрудника.
        :param last_name: Фамилия сотрудника.
        :param salary: Зарплата сотрудника.
        """
        # Атрибуты сделаны непубличными для инкапсуляции.
        # Прямой доступ к ним извне не рекомендуется,
        # чтобы избежать несогласованного состояния объекта.
        self._first_name = first_name
        self._last_name = last_name
        self._salary = salary

    def __str__(self) -> str:
        """
        Возвращает удобочитаемое строковое представление сотрудника.

        :return: Строка вида "Имя Фамилия, зарплата: ...".
        """
        return f"{self._first_name} {self._last_name}, зарплата: {self._salary:.2f}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление для отладки.

        :return: Строка вида "Employee('Имя', 'Фамилия', зарплата)".
        """
        return f"Employee('{self._first_name}', '{self._last_name}', {self._salary})"

    def get_full_name(self) -> str:
        """
        Возвращает полное имя сотрудника.

        :return: Строка с именем и фамилией.
        """
        return f"{self._first_name} {self._last_name}"

    def calculate_bonus(self) -> float:
        """
        Рассчитывает бонус сотрудника (10% от зарплаты).

        :return: Сумма бонуса.
        """
        return self._salary * 0.1


class Manager(Employee):
    """
    Дочерний класс для менеджера, наследующий Employee.

    Добавляет атрибут отдела и изменяет расчёт бонуса.

    Атрибуты:
        _department (str): Отдел, которым руководит менеджер (непубличный).

    Методы:
        __init__(first_name, last_name, salary, department): Конструктор,
            расширяющий базовый.
        __str__(): Переопределённое строковое представление с указанием отдела.
        __repr__(): Переопределённое представление для отладки.
        calculate_bonus(): Переопределённый расчёт бонуса (15% + фикс. премия).
        get_department(): Возвращает название отдела.
    """

    def __init__(self, first_name: str, last_name: str, salary: float, department: str) -> None:
        """
        Инициализация менеджера.

        :param first_name: Имя менеджера.
        :param last_name: Фамилия менеджера.
        :param salary: Зарплата менеджера.
        :param department: Отдел, которым руководит менеджер.
        """
        # Вызываем конструктор базового класса для инициализации общих атрибутов.
        super().__init__(first_name, last_name, salary)
        # Добавляем атрибут отдела (непубличный для защиты от прямого изменения).
        self._department = department

    def __str__(self) -> str:
        """
        Возвращает строковое представление менеджера с указанием отдела.

        :return: Строка вида "Имя Фамилия, отдел: ..., зарплата: ...".
        """
        return f"{self._first_name} {self._last_name}, отдел: {self._department}, зарплата: {self._salary:.2f}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление для отладки.

        :return: Строка вида "Manager('Имя', 'Фамилия', зарплата, 'отдел')".
        """
        return f"Manager('{self._first_name}', '{self._last_name}', {self._salary}, '{self._department}')"

    def calculate_bonus(self) -> float:
        """
        Переопределённый расчёт бонуса для менеджера.

        Обоснование: у менеджеров бонус выше, он составляет 15% от зарплаты
        плюс дополнительная фиксированная премия за руководство отделом.

        :return: Сумма бонуса.
        """
        # 15% от зарплаты + 5000 фиксированной премии
        return self._salary * 0.15 + 5000.0

    def get_department(self) -> str:
        """
        Возвращает название отдела, которым руководит менеджер.

        :return: Название отдела.
        """
        return self._department


if __name__ == "__main__":
    # Создаём сотрудника и менеджера
    emp = Employee("Иван", "Петров", 50000.0)
    mgr = Manager("Анна", "Сидорова", 80000.0, "Маркетинг")

    # Демонстрация работы методов
    print("=== Сотрудник ===")
    print(f"__str__: {emp}")
    print(f"__repr__: {repr(emp)}")
    print(f"Полное имя: {emp.get_full_name()}")
    print(f"Бонус: {emp.calculate_bonus():.2f}")

    print("\n=== Менеджер ===")
    print(f"__str__: {mgr}")
    print(f"__repr__: {repr(mgr)}")
    print(f"Полное имя (унаследованный метод): {mgr.get_full_name()}")
    print(f"Бонус (переопределённый метод): {mgr.calculate_bonus():.2f}")
    print(f"Отдел: {mgr.get_department()}")