def task13():
    dictionary = {}

    def menu():
        menu_options = [
            "1. Dodaj słowo wraz z definicją",
            "2. Znajdź definicję słowa",
            "3. Usuń słowo wraz z definicją z słownika",
            "4. Zakończ program"
        ]

        print("\n".join(menu_options))

    def program():
        menu()
        user_choice = input("> ")

        print("")
        match user_choice:
            case "1":
                word = input("Wpisz słowo: ")
                description = input("Wpisz definicję: ")
                dictionary[word] = description
                print("--- Słowo i definicja zostały dodane ---",)

            case "2":
                word = input("Wprowadź poszukiwane słowo: ")

                if word in dictionary:
                    print(f"--- Definicja słowa {word} ---")
                    print(dictionary[word])
                else:
                    print("--- Nie ma takiego słowa w słowniku! ---")

            case "3":
                word = input("Wprowadź słowo do usunięcia: ")

                if word in dictionary:
                    dictionary.pop(word)
                    print("--- Słowo zostało usunięte ---")
                else:
                    print("--- Nie ma takiego słowa w słowniku! ---")

            case "4":
                quit()

            case _:
                print("--- Nieprawidłowy wybór! ---")
        print("")

        # Zakładam, że to zapętlenie może być problemem, np. przy setnym prawidłowym wykonaniu -
        # pierwsza odpalona funkcja "program" nadal będzie wówczas aktywna.
        # Ponoć lepiej jest wrzucić to do "while True:",
        # która będzie się wykonywała, aż do wybrania przez użytkownika wartości "4" (quit()).
        # A może jest jeszcze jakieś inne podejście?
        program()

    program()