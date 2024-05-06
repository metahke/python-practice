def task1():
    albums = {'The Sensual World': 'Kate Bush', 'Shaday': 'Ofra Haza', 'Achtung Baby': 'U2', 'Aion': 'Dead Can Dance',
              'Invisible Touch': 'Genesis'}

    albums_names = albums.keys()
    print(albums_names)

    usr_album = input("Podaj nazwę albumu: ")

    if usr_album in albums_names:
        print(f'Wykonawcą albumu "{usr_album}" jest "{albums[usr_album]}"')
    else:
        print("Brak danych")


def task2():
    albums = {'The Sensual World': 'Kate Bush', 'Shaday': 'Ofra Haza', 'Achtung Baby': 'U2', 'Aion': 'Dead Can Dance', 'Invisible Touch': 'Genesis'}

    def menu():
        options = [
            "1. Sprawdź zapisane albumy",
            "2. Wyszukaj album",
            "3. Dodaj album",
            "4. Usuń album",
            "5. Wyjdź",
        ]

        print("\n".join(options))
        print("")

    def get_usr_choice():
        return input("Wybierz opcję (1-5): ")

    def execute_usr_choice(choice):
        match choice:
            case "1":
                display_albums()
            case "2":
                search_album()
            case "3":
                add_album()
            case "4":
                delete_album()
            case "5":
                quit()
            case _:
                print("--- Nieprawidłowy wybór! ---")

        print("")

    def display_albums():
        print(albums)

    def input_album_name():
        return input("Podaj nazwę albumu: ")

    def search_album():
        album = input_album_name()
        albums_names = albums.keys()

        if album in albums_names:
            print(f'> Wykonawcą albumu "{album}" jest "{albums[album]}".')
        else:
            print("--- Brak danych ---")

    def add_album():
        album = input_album_name()
        performer = input("Wprowadź wykonawcę: ")
        albums[album] = performer

        print(f"--- Album {album} dodany ---")

    def delete_album():
        album = input_album_name()
        albums.pop(album)

        print(f"--- Album {album} usunięty ---")

    while True:
        menu()
        choice = get_usr_choice()
        execute_usr_choice(choice)


def task3():
    import re

    text = "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this, and nothing more."

    words = re.sub("[^a-zA-Z ]", "", text).split(" ")
    words_occurence = {}

    for word in words:
        words_occurence[word] = words.count(word)

    print(words_occurence)


def task4():
    import copy

    birds = {'kos': 'Turdus merula', 'wilga': 'Oriolus oriolus', 'rudzik': 'Erithacus rubecula',
             'kukulka': 'Cuculus canorus', 'pleszka': 'Phoenicurus phoenicurus', 'bogatka': 'Parus major',
             'drozd': 'Turdus philomelos', 'zieba': 'Fringilla coelebs', 'dzwoniec': 'Chloris chloris',
             'szczygiel': 'Carduelis carduelis', 'szpak': 'Sturnus vulgaris', 'kopciuszek': 'Phoenicurus ochruros'}

    text = "W polowie maja, juz przed wschodem slonca, o trzeciej zaczyna spiewac drozd, po nim rudzik, a chwile pozniej kos. Pol godziny pozniej odzywa sie kukulka. Zaraz po niej budzi sie bogatka. Wraz ze wschodem slonca, o czwartej godzinie, swoj koncert rozpoczynaja pleszka i zieba. Dwadziescia minut pozniej i wilga akcentuje swoja obecnosc wysoko w koronach drzew. Jeszcze pozniej swoje trzy grosze dodaje szpak, a tuz po nim kopciuszek. Najwiekszymi spiochami w tej ferajnie okazuja sie byc dzwoniec i szczygiel."

    text_latin_addon = copy.copy(text)

    for bird in birds:
        text_latin_addon = text_latin_addon.replace(bird, f"{bird} ({birds[bird]})")

    print(text_latin_addon)


def task5():
    nums = {}

    max_range = int(input("Podaj liczbę n (n > 1): "))

    if max_range <= 1:
        print("Nieprawidłowy zakres!")
        quit()

    for num in range(1, max_range + 1):
        nums[num] = num ** 2

    print(nums)


def task6():
    answer = "Kluczami w słowniku mogą być jedynie elementy, które są 'immutable', czyli niezmienne, stałe. Dlatego też kluczem w słowniku nie może być inny słownik lub lista."
    
    print(answer)


def task7():
    import re

    dict_1_str = input("Wprowadź pierwszy słownik: ")
    dict_2_str = input("Wprowadź drugi słownik: ")

    dict_result = {}

    def str_to_dict(dictionary_str):
        dicionary = {}

        key_value_list = re.sub("[{}]", "", dictionary_str).split(", ")

        for key_value in key_value_list:
            key, value = key_value.split(": ")

            dicionary[int(key)] = value.replace("'", "")

        return dicionary

    dict_1 = str_to_dict(dict_1_str)
    dict_2 = str_to_dict(dict_2_str)

    print(dict_1 | dict_2)


def task8():
    data = {"V": "S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX": "S005", "X": "S009", "XI": "S007"}

    values = list(data.values())
    unrepeatable_values = []

    for value in values:
        if values.count(value) == 1:
            unrepeatable_values.append(value)

    print(unrepeatable_values)
