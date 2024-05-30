import pytest
from is_num_prime import is_num_prime


class TestIsNumPrime:
    @staticmethod
    @pytest.mark.parametrize("num", [
        2, 3, 7, 11, 53, 401, 1103
    ])
    def test_should_return_that_num_is_prime(num):
        expected = True
        result = is_num_prime(num)

        assert result == expected

    @staticmethod
    @pytest.mark.parametrize("num", [
        -10, -2, 8, 24, 134, 777, 1036
    ])
    def test_should_return_that_num_is_not_prime(num):
        expected = False
        result = is_num_prime(num)

        assert result == expected

    @staticmethod
    @pytest.mark.parametrize("num", [
        "hello", None, True, False, [], {}, ()
    ])
    def test_should_return_that_arg_is_invalid(num):
        expected = "Invalid argument passed to the function."
        result = is_num_prime(num)

        assert result == expected
