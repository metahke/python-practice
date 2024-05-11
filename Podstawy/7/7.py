def task1():
    nums = [4, 6, 8, 24, 12, 2]

    def get_max_num_index(numbers):
        max_num = max(nums)
        max_num_index = nums.index(max_num)

        return max_num_index

    print(get_max_num_index(nums))

    # :D Nie za bardzo widzę po co używać tutaj enumerate...


def task2():
    """
    Parametr funkcji jest tym, co zostaje zdefiniowane w nawiasach podczas tworzenia funkcji, natomiast argumentem jest to, co dodamy do nawiasów podczas wywoływania danej funkcji.

    'Default arguments' są zależne od parametrów funkcji, do których została przypisana konkretna wartość, np. 'num=1'. Jeśli nie przekażemy danego argumentu do funkcji, wówczas przyjmie on domyślnie zadeklarowaną wartość.

    'Keyword arguments' z kolei są argumentami przekazywanymi do funkcji, które podczas deklarowania mają zdefiniowaną nazwę parametru, pod który mają zostać podpięte. Pozwala to na wpisanie argumentów funkcji w różnej kolejności i poprawia czytelność kodu.
    """


def task3():
    def fizz_buzz(num):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            return num


def task4():
    def nums_multiply(*args):
        nums_multiplication = 1

        for num in args:
            if not isinstance(num, int):
                continue

            nums_multiplication *= num

        return nums_multiplication


def task5():
    def get_even_odd_nums_chain(**nums):
        even_nums, odd_nums = nums.values()
        even_odd_nums_chain = []

        shortest_list = even_nums if len(even_nums) < len(odd_nums) else odd_nums

        longest_list = even_nums if len(even_nums) > len(odd_nums) else odd_nums

        for i in range(len(shortest_list)):
            even_odd_nums_chain.append(shortest_list[i])
            even_odd_nums_chain.append(longest_list[i])

        even_odd_nums_chain.extend(longest_list[len(shortest_list):])

        print(even_odd_nums_chain)

    print(get_even_odd_nums_chain(even_nums=[2, 8, 24, 66, 88, 100, 122], odd_nums=[1, 7, 13, 19]))


def task6():
    nums = [1, 5, 23, 45, 67, 101, 126, 179, 1001, 1999]

    def get_two_digit_nums(nums_list):

        two_digit_nums = []

        for num in nums_list:
            if len(str(num)) == 2:
                two_digit_nums.append(num)

        return two_digit_nums

    print(get_two_digit_nums(nums))


def task7():
    def insert_start_fuel_level():
        return int(input("Wprowadź wartość paliwa między 5 000, a 30 000 litrów: "))

    def is_start_fuel_level_valid(level):
        return 5000 < level < 30000

    def insert_astronauts_num():
        return int(
            input("Wprowadź liczbę astronautów na pokładzie, która jest liczbą dodatnią i nie większą od 7: "))

    def is_astronauts_num_valid(astronauts_num):
        return 0 < astronauts_num <= 7

    def measure_distance(fuel_level, astronauts, distance):
        while fuel_level >= 0:
            print(f'Przebyto: {distance} kilometrów.')
            print(f'Posiadamy {fuel_level} litrów paliwa.')

            distance += 100
            fuel_level -= 300 + 100 * astronauts

        if distance < 2000:
            print("--- Statek kosmiczny nie dotarł do orbity ---")
        else:
            print("--- Statek kosmiczny dotarł do orbity ---")

        quit()

    def main():
        start_fuel_level = insert_start_fuel_level()

        while not is_start_fuel_level_valid(start_fuel_level):
            start_fuel_level = insert_start_fuel_level()

        astronauts_num = insert_astronauts_num()

        while not is_astronauts_num_valid(astronauts_num):
            astronauts_num = insert_astronauts_num()

        measure_distance(fuel_level=start_fuel_level, astronauts=astronauts_num, distance=0)

    main()
