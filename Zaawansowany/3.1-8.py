def task1():
    add_fifteen = lambda x: x + 15
    nums_multiply = lambda x, y: x * y

    print(add_fifteen(15), nums_multiply(3, 4))


def task2():
    to_sort = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

    to_sort.sort(key=lambda item: item[1])


def task3():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    squared_nums = list(map(lambda num: num ** 2, nums))
    cubed_nums = list(map(lambda num: num ** 3, nums))

    return squared_nums, cubed_nums


def task4():
    lines = ['10000101011', '111111', '01010101010010', '011001100001', '001010101011']

    # Zamiast count, użyłbym raczej <"11" in line>
    not_includes_neighbor_ones = list(filter(lambda line: not line.count("11"), lines))

    print(len(not_includes_neighbor_ones))


def task5():
    import functools

    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    nums3 = [7, 8, 9]

    print(functools.reduce(lambda sum, num: sum + num, nums1 + nums2 + nums3))


def task6():
    colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]

    connected_colors = list(map(lambda color: f"{color[0]} {color[1]}", colors))

    print(connected_colors)


def task7():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    new_nums = list(map(lambda num: num ** 2 if num % 2 == 0 else num, nums))

    print(new_nums)


def task8():
    orders = [
        ["34587", "Learning Python, Mark Lutz", 4, 40.95],
        ["98762", "Programming Python, Mark Lutz", 5, 56.80], ["77226", "Head First Python, Paul Barry", 3, 32.95],
        ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
    ]

    def calc_invoice_part(order: list) -> tuple:
        id, name, amount, price = order
        whole_price = round(amount * price, 2)

        if whole_price < 100:
            whole_price += 10

        return id, whole_price

    invoice = list(map(
        lambda order: calc_invoice_part(order), orders
    ))

    print(invoice)
