def task1():
    import re

    # example_txt = "Napisz program, który wczytuje dowolne zdanie. Usuń znaki interpunkcyjne (, . : ; , ! ?)"

    txt = input("Wprowadź tekst: ")

    almost_cleared_txt_list = re.sub("[^\w\s]", "", txt).split(" ")
    cleared_txt_list = []

    for txt in almost_cleared_txt_list:
        if txt != '':
            cleared_txt_list.append(txt)

    cleared_txt_list.reverse()
    reversed_txt = " ".join(cleared_txt_list)

    print(reversed_txt)


def task2():
    import random

    wynik = [12, 1, 45, 76, 50, 23]

    # Użyłbym metody map()
    def return_correct_result(result):

        poprawny_wynik = []

        for num in result:

            if not 0 < num < 50:
                print(f"Błędna wartość: {num}. Wprowadzono poprawki.")
                num = random.randrange(1, 50)

            poprawny_wynik.append(num)

        return poprawny_wynik

    print(return_correct_result(wynik))


def task3():
    lista1 = ["abc", "def", "ghi", "jkl"]
    lista2 = [1, 2, 3, 4, 5]
    lista3 = ["xyz", 1, '2']

    # A.
    print(lista1, lista2, lista3)

    # B.
    print(lista1[0], lista1[3])

    # C.
    lista2[1] = lista3[1]
    print(lista2)

    # D.
    lista3[2] = input("Trzeci element listy 3 będzie równy: ")
    print(lista3)

    # E.
    lista1.append('słowo')
    print(lista1)

    # F.
    lista1.pop(2)
    print(lista1)

    # G.
    print(len(lista3))

    # H.
    lista1.extend(lista3)
    print(lista1)


def task4():
    names = input("Wprowadź imiona znajomych oddzielone spacjami: ").split(" ")

    for name in names:
        print(f"Hello amigo o imieniu {name}. Co tam słychać? Ja muszę lecieć, trzymaj się.")


def task5():
    import re

    example_txt = "Napisz program pod podłogą, który wczytuje dowolne na zdanie. Usuń dla niego dla znaki interpunkcyjne (, . : ; , ! ?)"

    def get_text_info(text):
        almost_cleared_txt_list = re.sub("[^\w\s]", "", text).split(" ")
        cleared_txt_list = []

        for txt in almost_cleared_txt_list:
            if txt != '':
                cleared_txt_list.append(txt)

        # A.
        print(f"Zdanie zawiera {len(cleared_txt_list)} wyrazów.")

        print("---")

        # B.
        has_upper_text = False

        for txt in cleared_txt_list:
            first_letter = txt[0]

            if first_letter.isupper():
                has_upper_text = True
                print(txt)

        if not has_upper_text:
            print("Żaden z wyrazów nie rozpoczyna się wielką literą.")

        print("---")

        # C.
        words_list = ["i", "w", "na", "pod", "dla"]

        words_dict = {
            "i": [],
            "w": [],
            "na": [],
            "pod": [],
            "dla": [],
        }

        # Posłuży do sprawdzenia, czy jakiekolwiek ze słów z listy znajduje się w tekście
        is_included_in_words_list = False

        # Przejdzie przez każde ze słów tekstu i sprawdzi, czy znajduje się na liście.
        # Jeśli tak, wówczas doda jego indeks do słownika i zmieni wartość powyższej zmiennej
        for i in range(len(cleared_txt_list)):
            word = cleared_txt_list[i]

            if word in words_list:
                is_included_in_words_list = True
                words_dict[word].append(i)

        # Jeśli któreś ze słów listy zawiera się w tekście, wówczas wylistuje jego indeksy. Jeśli żadnego nie ma,
        # wówczas program wyda odpowiednią informację
        if is_included_in_words_list:
            for word in words_dict:
                if words_dict[word]:
                    print(f"Indeksy słowa '{word}': {words_dict[word]}.")
        else:
            print("Tekst nie zawiera słów:", words_list)

        print("---")

        # D. Nie uwzględni wielkości liter, ale to by wymagało znacznie większego skomplikowania (zamienić wszystkie wyrazy na zaczynające się z małych liter, ustawić w odpowiedniej kolejności, a później jakoś podmienić). Jak to zrobić inaczej?
        cleared_txt_list.sort()
        print(" ".join(cleared_txt_list))

    get_text_info(example_txt)
