import json


def task1():
    # Określ, czy poniższe ścieżki do plików.txt są względne / bezwzględne:
    # - C:\przyklad.txt -> ścieżka bezwzględna
    # - \katalog\przyklad.txt -> ścieżka względna
    # - C:\outer_dir\inner_dir\przyklad.txt -> ścieżka bezwzględna
    # - \outer_dir\innedr_dir\przyklad.txt -> ścieżka względna
    pass


def task2():
    plik = open("przyklad.txt", "r")
    linie = plik.readlines()
    print(linie)

    """
    Błędu stricte nie widzę, może chodzi o brak zamknięcia pliku? Generalnie lepiej byłoby zapewne użyć konstrukcji 'with open... as...', która sama zadba o zamknięcie pliku.
    """


def task3():
    with open("./przyklad.txt", "r") as file:

        lines = file.readlines()

        # Parzyste linijki będą nieparzystymi indeksami na liście
        for i in range(len(lines)):
            if i % 2 != 0:
                print(lines[i])


def task4():
    # Jaka jest różnica między kodowaniem UTF-8 a ASCII? Jaki byłby rezultat odczytania z pliku polskich liter (np. ą, ę, ć) bez zmiany sposobu formatowania danych?

    """
    Kodowanie ASCII nie zawiera w sobie wszystkich liter polskiego alfabetu. Próba odczytania takich znaków specjalnych spowoduje błąd w programie.
    """
    pass


def task5():
    with open("./przyklad.txt", "r", encoding="utf-8") as plik:
        plik.tell()
        plik.seek(43)
        print(plik.read(1))  # ???

        """ Otrzymamy wynik 'o' """


def task6():
    with open("./test.txt", "r", encoding="utf-8") as file:
        text = file.readlines()
        print(text[3])


def task7():
    text_lines = None
    cleared_text_lines = []

    with open("./przyklad7.txt", "r", encoding="utf-8") as file:
        text_lines = file.readlines()

    for line in text_lines:
        words = line.strip().split(" ")
        cleared_words = []

        for i in range(len(words)):
            if i == 0 or words[i] != words[i - 1]:
                cleared_words.append(words[i])

        cleared_text_lines.append(" ".join(cleared_words))

    cleared_text = " \n".join(cleared_text_lines)

    with open("./przyklad7-cleared.txt", "w", encoding="utf-8") as file:
        file.write(cleared_text)


def task8():
    def reverse_key_value(**kwargs):
        reversed_dict = {}

        for item in kwargs.items():
            key, value = item
            reversed_dict[value] = key

        return reversed_dict

    with open("./output.json", "w", encoding="utf-8") as file:
        new_dict = reverse_key_value(klucz1="wartość1", klucz2="wartość2", klucz3="wartość3")

        dict_json = json.dumps(new_dict, indent=4, ensure_ascii=False)

        file.write(dict_json)


def task9():
    packets = {}

    print("Interface Status")
    print("================================================================================")
    print("DN                                                 Description           Speed    MTU  ")
    print("-------------------------------------------------- --------------------  ------  ------")

    with open("./data.json", "r") as file:
        packets = json.loads(file.read())["imdata"]

    for packet in packets:
        attributes = packet["l1PhysIf"]["attributes"]

        dn = attributes["dn"]

        if len(attributes["dn"]) == 41:
            dn += "  "
        elif len(attributes["dn"]) == 42:
            dn += " "

        descr = attributes["descr"] if attributes["descr"] != "" else " " * 28
        speed = attributes["speed"]
        mtu = attributes["mtu"]

        print(dn, descr, speed.center(7), " ", mtu)


if __name__ == "__main__":
    task9()
