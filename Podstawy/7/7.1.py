def task1():
    colours = ['zielony', 'czerwony', 'niebieski', 'czarny', 'fioletowy', 'granatowy', 'niebieski', 'czarny', 'czarny',
               'zielony', 'cytrynowy', 'granatowy', 'niebieski', 'indygo', 'zielony', 'czerwony']

    colours_set = set(colours)

    # A.
    print(f"Na oryginalnej liście zapisanych jest {len(colours)} kolorów.")

    # B.
    print(f"W celu jej stworzenia zostało użytych unikalnych {len(colours_set)} kolorów.")

    # C.
    for colour in colours_set:
        print(colour)

    # D.
    colours_set.add("pomarańczowy")
    print(colours_set)

    # E.
    colours_set.remove("cytrynowy")
    print(colours_set)


def task2():
    import re

    word = input("Wprowadź dowolne zdanie: ")

    cleaned_word = re.sub(r"[^\w\s]", "", word).split(" ")

    # Krotka:
    word_tup = tuple(cleaned_word)

    # A.
    print(len(word_tup))

    # B.
    print(" ".join(word_tup))

    # C. Error, jeśli zdanie ma mniej niż cztery wyrazy
    first_word_tup = word_tup[0]
    fourth_word_tup = word_tup[3]

    print(first_word_tup, fourth_word_tup)

    # Zbiór:
    word_set = set(cleaned_word)

    # A.
    print(len(word_set))

    # B.
    print(" ".join(word_set))

    # C. To jedyne co wymyśliłem
    word_set_range = 0

    # Ponoć można lepiej deklarować, np. zmienna = zmienna = wartość?
    first_word_set = None
    fourth_word_set = None

    for word in word_set:
        if word_set_range == 0:
            first_word_set = word
        elif word_set_range == 3:
            fourth_word_set = word

        word_set_range += 1

    print(first_word_set, fourth_word_set)

    # D.
    comparisons = [first_word_tup == first_word_set, fourth_word_tup == fourth_word_set]
    answer = "{} wyraz w obu podpunktach jest"

    for i in range(2):
        word_num = "Pierwszy" if i == 0 else "Czwarty"
        result = "taki sam" if comparisons[i] else "jest różny"

        print(answer.format(word_num), result)


def task3():
    my_fav_colours = {
        "ametystowy",
        "czarny"
    }

    usr_colours = set(input("Wprowadź kolory oddzielone spacją:\n> ").split(" "))

    if usr_colours == my_fav_colours:
        print("Zbiory kolorów są jednakowe")
    else:
        print(f'W obu zbiorach zawierają się te kolory: {", ".join(my_fav_colours & usr_colours)}')
        print(f"Kolory wybrane tylko przez użytkownika: {', '.join(usr_colours - my_fav_colours)}")
        print(f"Kolory wybrane tylko przez twórcę programu: {', '.join(my_fav_colours - usr_colours)}")


def task4():
    n_num = int(input("Podaj liczbę n: "))

    A = set()
    B = set()

    for num in range(n_num):
        if num % 2 == 0:
            A.add(num)

        if num % 3 == 2:
            B.add(num)

    C = A | B
    D = A & B
    E = A - B
    F = B ^ A

    sets = {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "E": E,
        "F": F
    }

    for set_name in sets:
        print("Nazwa zbioru:", set_name)
        print("Ilość elementów:", len(sets[set_name]))
        print("Zawarte elementy:", sets[set_name])
        print("")

    if len(B - A) == 0:
        print("Zbiór B zawiera się w zbiorze A")
    else:
        print("Zbiór B nie zawiera się w zbiorze A")
