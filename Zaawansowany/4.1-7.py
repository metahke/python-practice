def task1():
    def get_few_nums_gen():
        for num in range(7):
            yield num

    get_few_nums_gen = get_few_nums_gen()

    print(next(get_few_nums_gen))
    print(get_few_nums_gen.__next__())

    for num in get_few_nums_gen:
        if num > 5:
            get_few_nums_gen.throw(ValueError, "Wartość 5 przekroczona!")

        print(num)

    # Otrzymujemy "ValueError: Wartość 5 przekroczona!"


def task2():
    def generate_prime_nums():
        first_prime_num = 2
        current_prime_num = first_prime_num

        while True:
            num_dividers = [
                num_divider for num_divider in range(1, current_prime_num + 1)
                if current_prime_num % num_divider == 0
            ]

            if num_dividers == [1, current_prime_num]:
                yield current_prime_num

            current_prime_num += 1

    prime_nums_generator = generate_prime_nums()

    for prime_num in prime_nums_generator:
        print(prime_num)


def task3():
    examp = (i for i in range(10))
    print(examp)

    """
    Powyższy kod utworzy generator, którego zadaniem jest listowanie liczb całkowitych z zakresu <0-9>.
    Listowanie możemy uruchomić, np. poprzez pętlę for oraz print:
    
    for num in examp:
        print(num)

    Jeśli chcemy odczytywać kolejne liczby całkowite, to zamiast tworzyć generator (nawiasy),
    możemy utworzyć listę składaną (nawiasy kwadratowe, np. [print(i) for i in range(10)]
    """


def task4():
    def fibonacci_nums():
        previous_num = 0
        current_num = 1

        while True:
            yield previous_num
            previous_num, current_num = current_num, previous_num + current_num

    fibonnacci_nums_gen = fibonacci_nums()

    for fibonacci_num in fibonnacci_nums_gen:
        print(fibonacci_num)


def task5():
    numbers = [1, -10, 2, 5, 10, -5, -20, 0, -30]

    filtered_numbers = [
        num for num in numbers
        if num <= 0
    ]

    print(filtered_numbers)


def task6():
    text = "The quick brown fox jumps over the lazy dog is an English-language pangram—a sentence that contains all of the letters of the English alphabet"

    text_words_len_without_word_the = [
        len(word) for word in text.split()
        if word.lower() != "the"
    ]

    print(text_words_len_without_word_the)


def task7():
    three_d = [
        [[1, 2, 3, 4], [0, -1, -2, -3, -4, -5, -6]],
        [[1, 10, 15, 12, 20, 20, 20], [-15, -13, 14, 20, -1]]
    ]

    filtered_lists_bigger_than_5 = [
        deepest_list for second_list in three_d
        for deepest_list in second_list
        if len(deepest_list) > 4
    ]

    print(filtered_lists_bigger_than_5)
