def task1():
    import re

    # example_txt = "Napisz program, który wczytuje dowolne zdanie. Usuń znaki interpunkcyjne (, . : ; , ! ?)"

    text = input("Wprowadź tekst: ")

    words = re.sub("\W", " ", text).split()

    words.reverse()
    print(" ".join(words))


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

        cleared_words = re.sub("\W", " ", text).split()

        # A.
        print(f"Zdanie zawiera {len(cleared_words)} wyrazów.")

        print("---")

        # B.
        has_upper_text = False

        for txt in cleared_words:
            first_letter = txt[0]

            if first_letter.isupper():
                has_upper_text = True
                print(txt)

        if not has_upper_text:
            print("Żaden z wyrazów nie rozpoczyna się wielką literą.")

        print("---")

        # C.
        words = ["i", "w", "na", "pod", "dla"]

        words_positions = {}

        for word in words:
            words_positions[word] = []

        is_included_in_words = False

        for i in range(len(cleared_words)):
            word = cleared_words[i]

            if word in words:
                is_included_in_words = True
                words_positions[word].append(i)

        if is_included_in_words:
            for word in words_positions:
                if words_positions[word]:
                    print(f"Indeksy słowa '{word}': {words_positions[word]}.")
        else:
            print("Tekst nie zawiera słów:", words)

        print("---")

        # D.
        cleared_words.sort()

        first_word_sentece = cleared_words[0][0].upper()

        reversed_sentence = first_word_sentece + " ".join(cleared_words)[1:].lower()

        print(f'{reversed_sentence}.')

    get_text_info(example_txt)