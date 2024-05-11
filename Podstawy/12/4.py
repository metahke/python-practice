class Menu:

    def show():
        choices = [
            "1. Dodaj notatkę",
            "2. Dodaj wizytówkę (Card)",
            "3. Wyświetl wszystkie notatki",
            "4. Wyświetl wszystkie wizytówki",
            "5. Wyjdź"
        ]

        print("\n".join(choices))

    def get_choice():
        return input("Podaj wybór: ")


class Manager:

    def __init__(self):
        self.notes_submanager = NotesSubManager()
        self.cards_submanager = CardsSubManager()

    def show_menu(self):
        Menu.show()

    def insert_name(self):
        return input("Wprowadź nazwę: ")

    def add_note(self, note):
        self.notes_submanager.add(note)

    def add_card(self, card):
        self.cards_submanager.add(card)

    def show_notes(self):
        self.notes_submanager.show()

    def show_cards(self):
        self.cards_submanager.show()

    def execute(self):
        choice = Menu.get_choice()

        match choice:
            case "1":
                note_name = self.insert_name()
                self.add_note(note_name)
            case "2":
                card_name = self.insert_name()
                self.add_card(card_name)
                print()
            case "3":
                self.show_notes()
            case "4":
                self.show_cards()
            case "5":
                print("Wychodzenie...")
                quit()
            case _:
                print("Nieprawidłowy wybór!")

    def start(self):
        self.show_menu()
        self.execute()


class SubManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show(self):
        print("---\nZapisane:")
        for i in range(len(self.items)):
            print(f"{i + 1}. {self.items[i]}")
        print("---")


class NotesSubManager(SubManager):
    def __init__(self):
        super().__init__()


class CardsSubManager(SubManager):
    def __init__(self):
        super().__init__()


def main():
    manager = Manager()
    while True:
        manager.start()


if __name__ == "__main__":
    main()
