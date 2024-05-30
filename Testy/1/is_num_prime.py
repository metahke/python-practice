from Testy.helpers.validate_arg_type import validate_arg_type


@validate_arg_type(int)
def is_num_prime(num):
    dividers = [
        divider for divider in range(1, num + 1)
        if num % divider == 0
    ]

    is_prime = dividers == [1, num]

    return is_prime
