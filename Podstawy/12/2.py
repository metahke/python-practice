class Depot:
    def __init__(self, name):
        self.name = name
        self.type = "Zwykła zajezdnia"
        self.vehicles = []

    def __str__(self):
        info = [
            f"Nazwa zajezdni: {self.name}",
            f"Typ: {self.type}",
            "Podlegające pojazdy:"
        ]

        for vehicle in self.vehicles:
            info.append(f"-\n{vehicle}")

        return "---\n" + "\n".join(info)

    def add(self, vehicle):
        self.vehicles.append(vehicle)


class BusDepot(Depot):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Zajezdnia autobusowa"

    def __str__(self):
        total_fuel_consumption = 0

        for vehicle in self.vehicles:
            total_fuel_consumption += vehicle.fuel_consumption

        return super().__str__() + f"\n-\nŁączne zużycie paliwa w bieżącym miesiącu: {total_fuel_consumption} litrów"


class TramDepot(Depot):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Zajezdnia tramwajowa"

    def __str__(self):
        total_wagons_num = 0

        for vehicle in self.vehicles:
            total_wagons_num += vehicle.wagons

        return super().__str__() + f"\n-\nŁączna liczba wagonów tramwajowych: {total_wagons_num}"


class Vehicle:
    def __init__(self, max_speed, number, depot):
        self.max_speed = max_speed
        self.number = number
        self.depot = depot.name

    def __str__(self):
        info = [
            f"Numer: {self.number}",
            f"Szybkość maksymalna: {self.max_speed}",
            f"Zajezdnia: {self.depot}"
        ]

        return "\n".join(info)


class Bus(Vehicle):
    def __init__(self, max_speed, number, depot, fuel_consumption):
        super().__init__(max_speed, number, depot)
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return super().__str__() + f"\nZużycie paliwa w bieżącym miesiącu: {self.fuel_consumption} litrów"


class Tram(Vehicle):
    def __init__(self, max_speed, number, depot, wagons):
        super().__init__(max_speed, number, depot)

        if not 0 < wagons <= 3:
            print("Nieprawidłowa ilość wagonów! Zmieniono na liczbę 0.")
            wagons = 0

        self.wagons = wagons

    def __str__(self):
        return super().__str__() + f"\nLiczba wagonów: {self.wagons}"


def main():
    zajezdnia_autobusowa = BusDepot("Grodzka")
    zajezdnia_tramwajowa = TramDepot("Mickiewicza")

    autobus = Bus(200, 111, zajezdnia_autobusowa, 1000)
    tramwaj1 = Tram(240, 23, zajezdnia_tramwajowa, 3)
    tramwaj2 = Tram(220, 24, zajezdnia_tramwajowa, 1)

    zajezdnia_autobusowa.add(autobus)
    zajezdnia_tramwajowa.add(tramwaj1)
    zajezdnia_tramwajowa.add(tramwaj2)

    print(zajezdnia_autobusowa)
    print(zajezdnia_tramwajowa)


if __name__ == "__main__":
    main()
