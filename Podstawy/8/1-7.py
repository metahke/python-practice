def task1():
    for i in range(1, 5):
        print(i * "*")

    for i in range(5, 0, -1):
        print(i * "*")


def task2():
    def check_if_palindrome(word):
        is_palindrome = 'jest' if word.lower() == word.lower()[::-1] else 'nie jest'

        print(f"Podany wyraz {is_palindrome} palindromem!")

    check_if_palindrome("Janusz")
    check_if_palindrome("kajak")


def task3():
    names = ["Adam", "Stanisław", "Joanna", "Kornelia", "Kacper"]

    for i in range(len(names)):
        for m in range(i + 1, len(names)):
            print(f"{names[i]} - {names[m]}")


def task4():
    for i in range(1000, 10000):
        print(i)


def task5():
    zamowienia = {
        "Klient_1335": {
            "nazwa_potrawy": "rosół",
            "ocena": 5,
            "rachunek": 20.0
        },
        "Klient_222": {
            "nazwa_deseru": "lody waniliowe",
            "rachunek": 5.0
        }
    }

    for client in zamowienia:
        parameters = list(zamowienia[client].keys())

        print("--- Podsumowanie zamówienia ---")
        print(f"{client}:")

        for parameter in parameters:
            print(f"{parameter}: {zamowienia[client][parameter]}")

        print("---\n")


def task6():
    def num_frequency(num=None):
        if num is None or isinstance(num, str):
            print("Nie wybrano liczby!")
            quit()

        unique_digits = list(set(map(int, str(num))))
        all_digits = list(map(int, str(num)))

        for digit in unique_digits:
            print(f"{digit}: {all_digits.count(digit)}")

        print("---")

    # num_frequency(155773)
    # num_frequency(5)
    # num_frequency(1234559)


def task7():
    num = int(input("Wprowadź liczbę: "))

    fibonacci_nums = [0, 1]
    penultimate_num = fibonacci_nums[0]
    last_num = fibonacci_nums[1]

    for i in range(1, num + 1):

        current_num = penultimate_num + last_num

        if num == 1 or current_num > num:
            break

        fibonacci_nums.append(current_num)
        penultimate_num = last_num
        last_num = current_num

    print(fibonacci_nums)
