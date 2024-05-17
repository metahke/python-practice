import re


def task1():
    text1 = "Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts and visual mockups."
    text2 = "Sameznakiicyfry777"

    def contains_non_word_chars(word):
        return bool(re.findall("\W", word))

    print(contains_non_word_chars(text1))
    print(contains_non_word_chars(text2))


def task2():
    text1 = "Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts and visual mockups."
    text2 = "bameznakiicyfry777"

    def starts_with_b_or_0(text):
        pattern = r"^b|0"
        match = re.search(pattern, text)

        is_valid = "zaczyna" if match else "nie zaczyna"

        print(f"Podany ciąg {is_valid} się od cyfry lub litery 'b'")

    starts_with_b_or_0(text1)
    starts_with_b_or_0(text2)


def task3():
    text1 = "Lorem ipsum is placeholder text commonly used in the graphic, print, and publishing industries for previewing layouts and visual mockups."
    text2 = "bameznakiicyfry_aa777"

    pattern = r"[a-z]+_[a-z]+"

    def contains_pattern(text, text_pattern):
        return bool(re.search(text_pattern, text))

    print(contains_pattern(text1, pattern))
    print(contains_pattern(text2, pattern))


def task4():
    text = "Słowo słowo zdanie fajne zdanie. Co powiess mi na to cossss i zwykles tak"
    pattern = r"\w{1,}s{2}"

    print(re.findall(pattern, text))


def task5():
    text = [
        "unique New York",
        "Regular Expressions",
        "ALOHA",
        "Python should match"
    ]

    pattern = r"[\w]{6,}"

    print([
        word for word in text
        if re.match(pattern, word)
           and "a" not in word.lower()
    ])


def task6():
    html_elements = [
        "<span>Yowza! That/\’s a great regular expression.</span>",
        "<p>Learn about regular expressions here.</p> <p>You\'re going to love them!</p>",
        "I'm not HTML!!",
        "<p>Incomplete HTML"
    ]

    pattern = r"<[a-z]+>.*?<\/[a-z]+>"

    for element in html_elements:
        print(f"> {element}")

        if re.search(pattern, element):
            print("Prawidłowy element HTML!\n---")
        else:
            print("Nieprawidłowy element HTML!\n---")


def task7():
    mail = "username@companyname.com"

    def get_company_name_from_mail(email):
        pattern = r"@([a-z]{1,})."
        company_name = re.search(pattern, email).group(1)

        return company_name

    print(get_company_name_from_mail(mail))


def task8():
    text = "2 cats and 3 dogs 4real"
    pattern = r"\D"  # any non digit

    nums_words = [
        word for word in text.split()
        if not re.search(pattern, word)
    ]

    print(nums_words)


def task9():
    # Prawidłowa liczba zmiennoprzecinkowa, lecz nie w kontekście Pythona, a w stosunku do zadania!

    def check_float_num():
        num = input("Podaj liczbę!: ")
        pattern = r"(\d{1,},\d{1,})|(^\d+$)|(-\d+$)"

        match = re.match(pattern, num)

        is_float = "prawidłowa" if match else "nieprawidłowa"

        print(f"{num} to {is_float} liczba zmiennoprzecinkowa!")

    check_float_num()


def task10():
    """
    Jest wiele różnych podejść. Przy pomocy Regexa możemy utworzyć kilka konkretnych szablonów, np.
    \d{4}-\d{2}-\d{2}|\d{4}.\d{2}.\d{2}|\d{2}\/\d{2}\/\d{2}|\d{4}-\w{1,}-\d{2} (HEHE!)
    lub osobiście preferowałbym, np. coś tego pokroju:
    """
    data_from_file = "2019-03-11: 23.5, 19/03/12: 12.7, 2019.03.13: 11.1, 2019-marzec-14: 14.3"

    pattern = r"(.*?):"
    dates = []

    for item in data_from_file.split(", "):
        date = re.search(pattern, item).group(1)
        dates.append(date)

    print(dates)

    """
    ALBO! JESZCZE LEPIEJ! Można przerzucić ten plik do słownika (upewniając się co do formatu itp)
    i wyłapać z niego same klucze :-)
    """


def task11():
    str_list = [
        "#ab4",
        "#AB4B72",
        "#ab43",
        "#aaaaaaaaa",
        "#ahl"
    ]

    pattern = r"(#\w{3})$|(#\w{6})$"

    for string in str_list:
        is_hex = "jest" if re.match(pattern, string) else "nie jest"

        print(f"String {string} {is_hex} zapisem koloru w systemie HEX")
