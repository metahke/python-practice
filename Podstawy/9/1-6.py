def task1():
    a = ["Hello", "World"]
    b = ["Hello", "Moon"]

    if set(a) & set(b):
        print("Mają!")
    else:
        print("Nie mają!")


def task2():
    import random

    nums = set()

    def rm_even_nums(num):
        if num % 2 != 0:
            return num

    for i in range(15):
        num = random.randrange(5, 121)
        nums.add(num)

    odd_nums = set(filter(rm_even_nums, nums))

    print(odd_nums)


def task3():
    values = {"a": 3, "b": 1, "c": 10, "d": 15, "e": 20}
    reversed_values = {}

    for key in values:
        new_key = values[key]
        new_value = key

        reversed_values[new_key] = new_value

    print(values)
    print(reversed_values)


def task4():
    cities_rainfalls = {}

    while True:
        choice = input("Wprowadź miasto i opady oddzielone spacją: ")

        if choice == "":
            break

        city, rainfall = choice.split(" ")

        if cities_rainfalls.get(city):
            cities_rainfalls[city] += int(rainfall)
            continue

        cities_rainfalls[city] = int(rainfall)

    for city in cities_rainfalls:
        print(f"{city} : {cities_rainfalls[city]}")


def task5():
    bill_items = [
        ['Tom', 'Calamari', 6.00],
        ['Tom', 'American Hot', 11.50],
        ['Tom', 'Chocolate Fudge Cake', 4.45],
        ['Clare', 'Bruschetta Originale', 5.35],
        ['Clare', 'Fiorentina', 10.65],
        ['Clare', 'Tiramisu', 4.90],
        ['Rich', 'Bruschetta Originale', 5.35],
        ['Rich', 'La Reine', 10.65],
        ['Rich', 'Honeycomb Cream Slice', 4.90],
        ['Rosie', 'Garlic Bread', 4.35],
        ['Rosie', 'Veneziana', 9.40],
        ['Rosie', 'Tiramisu', 4.90],
    ]

    bill = {}

    for bill_item in bill_items:

        person, dish, price = bill_item

        if not bill.get(person):
            bill[person] = {}
            bill[person]["potrawy"] = []
            bill[person]["cena"] = 0

        bill[person]["potrawy"].append(dish)
        bill[person]["cena"] += price

    print(bill)


def task6():
    import json

    api_json_data = """{
        "data": [1, 2, "asd", [2, 3, 4, 5]],
        "nested_analysis": {
            "analysis_1": [1, 10, 15, 120.2, "120"],
            "analysis_2": [10, 100, "test", 200, 300]
        },
        "probes": [["probe_1", "probe_2"], "probe_3"]
    }"""

    values = []

    data = json.loads(api_json_data)

    for key in data:

        if isinstance(data[key], list):
            for value in data[key]:

                if isinstance(value, list):
                    for subvalue in value:
                        values.append(subvalue)
                else:
                    values.append(value)

        if isinstance(data[key], dict):
            for subkey in data[key]:
                for value in data[key][subkey]:
                    values.append(value)

    def is_str(value):
        if isinstance(value, str):
            return value

    str_only = list(filter(is_str, values))

    print(str_only)
