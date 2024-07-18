import pytest
from fizz_buzz import fizz_buzz


class TestFizzBuzz:
    @staticmethod
    @pytest.mark.parametrize("num", [
        3, 9, 27, 333, 1002
    ])
    def test_should_return_fizz(num):
        result = "Fizz"

        assert fizz_buzz(num) == result

    @staticmethod
    @pytest.mark.parametrize("num", [
        5, 25, 140, 1055, 55555
    ])
    def test_should_return_buzz(num):
        result = "Buzz"

        assert fizz_buzz(num) == result

    @staticmethod
    @pytest.mark.parametrize("num", [
        15, 90, 270, 1500, 7500
    ])
    def test_should_return_fizzbuzz(num):
        result = "FizzBuzz"

        assert fizz_buzz(num) == result

    @staticmethod
    @pytest.mark.parametrize("num", [
        "hello", None, True, False, [], {}, ()
    ])
    def test_should_return_that_arg_is_invalid(num):
        result = "Invalid argument passed to the function."

        assert fizz_buzz(num) == result
