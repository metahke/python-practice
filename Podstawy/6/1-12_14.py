# Funkcji nie nazywam zgodnie z dobrymi praktykami, ponieważ służą jedynie do prawidłowego rozdzielenia ćwiczeń.

def task1():
    for i in range(10):
        print("Hello, World!")


def task2():
    num = int(input("Podaj liczbę n: "))

    # Można na forze, ale po co skoro mamy taki ładny wzór :-)
    sum_up = int((1 + num) / 2 * num)
    print(sum_up)


def task3():
    nums = []

    for i in range(10):
        num = int(input(f"Podaj liczbę nr. {i + 1}: "))
        nums.append(num)

    for num in nums:
        if num % 2 == 0:
            print(num, end=" ")


def task4():
    day_num = input("Podaj liczbę danego dnia tygodnia: ")

    days = {
        "1": "Poniedziałek",
        "2": "Wtorek",
        "3": "Środa",
        "4": "Czwartek",
        "5": "Piątek",
        "6": "Sobota",
        "7": "Niedziela"
    }

    if day_num in days:
        print(days[day_num])
    else:
        print("Nie ma takiego dnia!")


def task5():
    d = (1, [2, 4], 'tekst', 3 + 5j)

    # a)
    print(d[-1])

    # b)
    print(d[0:2])

    # c)
    print("abc" in d)


def task6():
    a = [3, 1, 5, 7, 9, 2, 6]

    # a) 7
    print(a[3])  # Wybierze element o indeksie równym 3.

    # b) [1, 5, 7]
    print(a[1:4])  # Pokaże elementy zaczynające się od indeksu pierwszego i kończące się na indeksie trzecim.

    # c) [7, 9, 2, 6]
    print(a[3:])  # Pokaże elementy zaczynające się od indeksu trzeciego do samego końca listy.

    # d) [9, 2, 6]
    print(a[-3:])  # Pokaże elementy zaczynające się od indeksu -3 do samego końca listy.

    # e) [3, 1, 5]
    print(a[:3])  # Pokaże elementy od samego początku do indeksu drugiego.

    # f) [7, 9, 2]
    print(a[3:-1])  # Pokaże elementy od indeksu 3 do przedostatniego.

    # g) [3, 5, 9, 6]
    print(a[::2])  # Pokaże co drugi element od indeksu 0 do samego końca listy.

    # h) [2, 9, 7]
    print(a[5:2:-1])  # Pokaże elementy od indeksu piątego, do indeksu trzeciego, idąc do tyłu co jeden element.

    # i) 33
    print(sum(a))  # Wyświetli sumę wszystkich liczb znajdujących się na liście.

    # j) False
    print(8 in a)  # Sprawdzi, czy liczba 8.py znajduje się na liście.

    # k) True
    print(4 not in a)  # Sprawdzi, czy liczba 4 nie znajduje się na liście.


def task7():
    num = int(input("Podaj liczbę, którą zamienimy na wartość bezwzględną: "))
    absolute_value = num if num >= 0 else -1 * num

    print(f"Wartość bezwzględna liczby wynosi: {absolute_value}")


def task8():
    user_weight = int(input("Podaj swoją wagę (kg): "))
    user_height = float(input("Podaj swój wzrost (m): "))

    bmi = user_weight / (user_height ** 2)
    excess_weight_level = None

    print(f"Twoje BMI wynosi: {round(bmi, 2)}")

    if bmi < 18.5:
        print("Masz niedowagę")
    elif 18.5 <= bmi <= 24:
        print("Twoja waga jest prawidłowa")
    elif 24 < bmi <= 26.5:
        print("Posiadasz lekką niedowagę")
    elif bmi <= 35:
        excess_weight_level = 1
    elif bmi <= 40:
        excess_weight_level = 2
    else:
        excess_weight_level = 3

    if excess_weight_level in [1, 2, 3]:
        print(f"Masz nadwagę i otyłość {excess_weight_level} stopnia")


def task9():
    print("Koniunkcja to 'and' (wszystkie założenia muszą zostać spełnione).")
    print("Alternatywa logiczna to 'or' (przynajmniej jedno założenie musi zostać spełnione).")
    print(True and False) # False
    print(True and True)  # True
    print(False or False)  # False
    print(False or True)  # True


def task10():
    import random

    range_left = int(input("Podaj granicę dolnego zakresu liczbowego: "))
    range_right = int(input("Podaj granicę górnego zakresu liczbowego: "))

    if range_left > range_right:
        print("Zakres dolny jest wartością większą od zakresu górnego. Wychodzenie...")
        quit()

    computer_choice = random.randrange(range_left, range_right)
    print(f"Maszyna wylosowała liczbę...")

    user_choice = None
    user_points = range_right - range_left

    while computer_choice != user_choice:
        user_choice = int(input("Odgadnij liczbę: "))

        if user_choice < range_left or user_choice > range_right:
            print("Podano liczbę spoza wybranego zakresu!")
            continue

        if user_choice - computer_choice < 0:
            print("Podałeś za małą liczbę!")
        else:
            print("Podałeś za dużą liczbę!")

        user_points -= 1

    print(f"Gratulacje! Zdobyłeś {user_points} punkty!")


def task11():
    # a)
    for line in range(6):
        print("*" * 7)

    # b)
    columns, lines = 5, 5
    for line in range(lines):
        if line == 0 or line == lines - 1:
            print("*" * columns)
        else:
            print(f"* {''.center(columns - 4)} *")
    # c)
    for i in range(0, 5):
        print(("*" * (2 * i + 1)).center(9))


def task12():
    a_char_position = 97
    z_char_position = 122

    for i in range(z_char_position - a_char_position + 1):
        print(chr(a_char_position + i), chr(z_char_position - i).upper())


def task14():
    plus = [
        ["    *    "],
        ["    *    "],
        ["* * * * *"],
        ["    *    "],
        ["    *    "],
    ]

    for line in plus:
        print(line)
