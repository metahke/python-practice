import math, random
from datetime import datetime


def task1():
    class Student:
        def __init__(self, name, age, profession):
            self.name = name
            self.age = age
            self.profession = profession

        def info(self):
            print(f"Nazywam się {self.name} i mam {self.age} lat. Uczę się na kierunku {self.profession}.")

    student1 = Student("Janusz", 40, "informatyk")
    student1.info()


def task2():
    class Vehicle:
        def __init__(self, max_speed, mileage):
            self.max_speed = max_speed
            self.mileage = mileage

        def increase_mileage(self, value):
            self.mileage += value

    car = Vehicle(200, 350000)

    print(car.mileage)
    car.increase_mileage(450)
    print(car.mileage)


def task3():
    class Rectangle:
        def __init__(self, side_a, side_b):
            self.side_a = side_a
            self.side_b = side_b

        def calc_area(self):
            return self.side_a * self.side_b

        def calc_perimeter(self):
            return 2 * (self.side_b + self.side_b)

    figure1 = Rectangle(2, 5)
    print(figure1.calc_area())
    print(figure1.calc_perimeter())


def task4():
    class BankAccount:
        # 1.
        def __init__(self, account_number, owner_name, bank_balance):
            self.number = account_number
            self.owner = owner_name
            self.balance = bank_balance

        # 2.
        def count_commission(self, amount):
            return math.floor(amount / 100) * 2

        def charge_commission(self, commission):
            self.balance -= commission

        def deposit(self, amount):
            commission = self.count_commission(amount)

            self.balance += amount
            self.charge_commission(commission)

        # 3.
        def withdraw(self, amount):
            if amount > self.balance:
                print("Brak wystarczających środków!")
                return

            self.balance -= amount

        # 4.
        def change_ownership(self, new_owner):
            self.owner = new_owner

        # 5.
        def get_account_details(self):
            details = [
                f"Numer konta: {self.number}",
                f"Nazwa właściciela: {self.owner}",
                f"Stan konta: {self.balance}"
            ]

            return details

        def display(self):
            formatted_details = "\n".join(self.get_account_details())

            print(formatted_details)

    account1 = BankAccount("1234", "Janusz", 2000)


def task5():
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    figures = ["Hearts", "Spades", "Clubs", "Diamonds"]
    cards = []

    class Deck:
        def __init__(self, cards):
            self.cards = cards

        def shuffle(self):
            random.shuffle(self.cards)

        def deal(self):
            card = cards.pop()
            return f"{card.value} - {card.figure}"

    class Card:
        def __init__(self, value, figure):
            self.value = value
            self.figure = figure

    for figure in figures:
        for value in values:
            card = Card(value, figure)
            cards.append(card)

    deck = Deck(cards)
    deck.deal()


def task6():
    class Manager:
        def __init__(self):
            self.orders = {}

        def add(self, order, amount=1):
            if self.orders.get(order):
                self.orders[order] += amount
                return

            self.orders[order] = amount

        def sell(self, order_id):
            for order in self.orders:

                if order.id == order_id:
                    if self.orders[order] == 0:
                        print("Brak przedmiotu na stanie!")
                        return

                    self.orders[order] -= 1
                    print("Przedmiot sprzedany pomyślnie!")

    class Order:
        def __init__(self, id, name, price):
            self.id = id
            self.name = name
            self.price = price

    pluszak = Order(121, "Miś Amisz", 100)
    owad = Order(3301, "Cykada", 7)

    zamowienia = Manager()
    zamowienia.add(pluszak, 10)
    zamowienia.add(owad, 1)
    print(zamowienia.orders)
    zamowienia.sell(3301)
    print(zamowienia.orders)
    zamowienia.sell(3301)
    print(zamowienia.orders)


def task7():
    import datetime

    class Note:
        def __init__(self, author, content):
            self.author = author
            self.content = content
            self.time = datetime.datetime.now().strftime("%H %M")

    class Notebook:
        def __init__(self):
            self.notes = []

        def add(self, note):
            self.notes.append(note)

        def create(self, author, content):
            new_note = Note(author, content)
            self.add(new_note)

        def status(self):
            notes_amount = len(self.notes)

            print(f"> Ilość zapisanych notatek: {notes_amount}")

        def display(self):

            if len(self.notes) == 0:
                print("--- Brak notatek ---")
                return

            print("--- Twoje notatki ---")

            for i in range(len(self.notes)):
                note = self.notes[i]

                print(f"{i + 1}. {note.author}: {note.content} o godzinie {note.time}")

            print("---")

    nb = Notebook()
    note1 = Note("Jadwiga", "Kupić wodę")
    note2 = Note("Angelika", "Posprzątać kuchnię")

    nb.status()
    nb.display()
    nb.create("Jamrosz", "Pomalować ścianę")
    nb.add(note1)
    nb.add(note2)
    nb.display()
    nb.status()


def task8():
    first_case = {
        'name': 'first_case',
        'created_task': '2021-10-26T19:48:12+00:00',
        'end_task': None
    }

    second_case = {
        'name': 'second_case',
        'created_task': '2021-09-26T19:48:12+00:00',
        'end_task': '2021-10-26T19:48:12+00:00'
    }

    class Case:
        def __init__(self, case):

            self.name = case["name"]
            self.created_task = case["created_task"]
            self.end_task = case["end_task"]

        def retrieve_seconds(self):
            # Można również przemienić od razu na format ISO: datetime.fromisoformat(self...)
            date_pattern = "%Y-%m-%dT%H:%M:%S+00:00"

            created_date = datetime.strptime(self.created_task, date_pattern)

            end_date = 0
            if self.end_task is None:
                end_date = datetime.today()
            else:
                end_date = datetime.strptime(self.end_task, date_pattern)

            total_seconds = (end_date - created_date).total_seconds()

            return total_seconds

    # case1 = Case(first_case)
    # case2 = Case(second_case)


if __name__ == "__main__":
    task2()
