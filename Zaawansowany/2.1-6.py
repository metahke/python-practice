def task1():
    def log_func_info(func):
        def wrapper(*args, **kwargs):
            print("Func name:", func.__name__)
            print("Args:", args)
            print("Kwargs:", kwargs)

        return wrapper

    @log_func_info
    def example_func(*args, **kwargs):
        print("I am a function")

    example_func(1, 2, 3, name="Jadwiga", city="Brączków")


def task2():
    def asterisk_decorator(func):
        def wrapper(*args, **kwargs):
            print("*" * 7)
            func(*args, **kwargs)
            print("*" * 7)

        return wrapper

    class AsteriskDecorator:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print("*" * 7)
            self.func(*args, **kwargs)
            print("*" * 7)

    # @AsteriskDecorator
    @asterisk_decorator
    def print_info(name, age):
        print(f"Nazywam się {name} i mam {age} lat.")

    print_info("Rally", 31)


def task3():
    from collections import defaultdict

    def count(func):
        # Właściwie to, jak to działa? Jak to jest, że dekorator wie, ile razy te funkcje zostały wywołane?
        func_execution_times = defaultdict(int)

        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

            func_name = func.__name__

            func_execution_times[func_name] += 1

            print(f"Funkcję {func_name} wywołano już {func_execution_times[func_name]} razy.")

        return wrapper

    @count
    def func1():
        pass

    @count
    def func2():
        pass

    func1()
    func1()
    func2()
    func1()


def task4():
    def validate_arg_type(arg_type):
        def check(func):
            def validate_args(arg):
                if not isinstance(arg, arg_type):
                    raise ValueError("Do funkcji przekazano nieprawidłowy typ zmiennej.")

                func(arg)

            return validate_args

        return check

    @validate_arg_type(str)
    def name_info(name):
        print("Imię:", name)

    name_info("hello")
    name_info(123)


def task5():
    import time

    def timethis(func):
        def wrapper(*args, **kwargs):
            time_before = time.time()

            func(*args, **kwargs)

            time_after = time.time()

            func_exec_time = time_after - time_before

            return f"Czas wykonywania funkcji wynosi: {func_exec_time}"

        return wrapper

    @timethis
    def sum_nums(*args):
        return sum(args)

    print(sum_nums(1, 2, 3))


def task6():
    from abc import ABC, abstractmethod
    from dataclasses import dataclass
    import datetime

    # @property
    # @staticmethod
    # @classmethod
    class Person:
        def __init__(self, name, age):
            self.name = name,
            self.age = age

        """
        Dekorator property pozwala nam na stworzenie metody, która jest powiązana z polem klasy o jej nazwie.
        Podczas wywołania danego pola, metoda powiązana zostaje automatycznie wywołana.
        """

        @property
        def name_length(self):
            return len(self.name)

        """
        Dekorator staticmethod pozwala nam na oznaczanie metod klasy, które nie korzystają z elementów danej klasy.
        Zapewniają lepszą organizację kodu i informację dla innych programistów z czym mają do czynienia.
        """

        @staticmethod
        def get_current_time():
            print("Aktualny czas to:", datetime.datetime.now())

        """
        Dekorator classmethod działa tak, jak staticmetod, z tymże jego pierwszym argumentem jest klasa, w której operuje (cls). Pozwala na modyfikowanie pól i metod danej klasy.
        Jest użyteczny, gdy chcemy operować na klasie, jako na całości, a nie na osobnych obiektach, np. wykorzystać metodę zwieńczoną dekoratorem classmethod w celu utworzenia obiektu w jakiś inny sposób.
        W przeciwieństwie do dekoratora staticmethod ma dostęp do właściwości klasy i "self".
        """

        @classmethod
        def fromBirthYear(cls, name, birth_year):
            return cls(name, datetime.date.today().year - birth_year)

    # @abstractmethod
    class Character(ABC):
        def __init__(self, name):
            self.name = name

        """
        Dekorator abstractmethod pozwala nam na stworzenie klasy, która będzie klasą bazową niewykorzystywaną w kodzie jako tako.
        Ta klasa bazowa poprzez zdefiniowane dekoratory abstractmethod informuje, jake metody muszą być zawarte w  klasach dziedziczących.
        Jeśli klasy dziedziczące nie będą posiadały zaimplementowanych metod oznaczonych dekoratorem abstractmethod, wówczas otrzymamy błąd.
        """

        @abstractmethod
        def skill(self, skill):
            pass

    class Wizard(Character):
        def __init__(self, name):
            super().__init__(name)

        """
        def skill(self, skill):
            print(f"Nazywam się {self.name} i moją umiejętnością jest: {skill}")
        """
        # TypeError:
        # Can't instantiate abstract class Wizard with abstract method skill

    # @dataclass
    """
    Dekorator dataclass ozwala nam na "szybsze" tworzenie klas. Automatycznie zarządza metodami i tworzy je,
    np. __init__, czy __repr__, przez co nie musimy się skupiać na ich implementacji.
    """

    @dataclass
    class Animal:
        species: str
        legs: int

    # Main

    person1 = Person("Janusz", 20)
    print(person1.age)
    person2 = Person.fromBirthYear("Jacek", 2001)
    print(person2.age)
    person1.get_current_time()

    # wizard1 = Wizard("Jermosz")

    dog = Animal(species="pies", legs=4)
    print(dog)
