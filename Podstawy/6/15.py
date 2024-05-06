def task15():
    people = {}
    pesels = ["90090515836", "92071314764", "81100216357", "80072909146", "90080517451"]
    person_info = {
        "imie": "Jakieś imię",
        "nazwisko": "Jakieś nazwisko",
        "wiek": "jakiś wiek",
        "kolor_oczu": "jakiś kolor oczu"
    }

    for pesel in pesels:
        people[pesel] = person_info

        # A.
        people[pesel]["imie_matki"] = "Jakieś imię matki"

    # B.
    for pesel in pesels:
        if pesel[-1] == "1": people.pop(pesel)
    # C.
    for pesel in people:
        imie, nazwisko, wiek, kolor_oczu, imie_matki = people[pesel].values()
        print(f"""Cechy osoby o PESELu {pesel} to:
            - Imię: {imie}
            - Nazwisko: {nazwisko}
            - Wiek: {wiek}
            - Kolor oczu: {kolor_oczu}
            - Imię matki: {imie_matki}
        """)
