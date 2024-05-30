class TryingToAddDifferentTypesError(Exception):
    def __str__(self):
        return "Błąd! Próbujesz dodać do siebie różne typy!"


class ElementWithoutLenMethodError(Exception):
    def __str__(self):
        return "Błąd! Argument funkcji nie posiada właściwości len()!"


def example1():
    for i in range(3):
        try:
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))

            print(x, '/', y, '=', x / y)
        except ValueError:
            print("W wartościach input wprowadzono wartości inne, niż liczby. Pomijanie...")
        except ZeroDivisionError:
            print("Druga liczba, którą wprowadzono, to liczba 0. Nie można dzielić przez zero! Pomijanie...")


def example2(L):
    print("\n\nExample 2")
    sum = 0  # Nieużywany kod
    sumOfPairs = []

    try:
        len(L)
    except TypeError:
        try:
            raise ElementWithoutLenMethodError
        except ElementWithoutLenMethodError as e:
            print(e)

    for i in range(len(L)):
        try:
            sumOfPairs.append(L[i] + L[i + 1])
        except IndexError:
            print("Wykroczono poza długość danego elementu! Pomijanie...")
        except TypeError:
            try:
                raise TryingToAddDifferentTypesError
            except TryingToAddDifferentTypesError as e:
                print(e)

    print("sumOfPairs = ", sumOfPairs)


def printUpperFile(fileName):
    try:
        file = open(fileName, "r")
    except FileNotFoundError:
        print("Nie znaleziono podanego pliku. Wychodzenie...")
    except OSError:
        print("Wpisano nieprawidłową wartość dla nazwy pliku! Wychodzenie...")
    else:
        for line in file:
            print(line.upper())
        file.close()


def main():
    # example1()
    L = [10, 3, 5, 6, 9, 3]

    # example2(1234)
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])

    try:
        example3([10, 3, 5, 6])
    except NameError:
        print("Wpisano niepoprawną nazwę. Sprawdź swój kod! Pomijanie...")

    printUpperFile(123)
    printUpperFile("doesNotExistYest.txt")
    printUpperFile("./Dessssktop/misspelled.txt")


if __name__ == "__main__":
    main()
