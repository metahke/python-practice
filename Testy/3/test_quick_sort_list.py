import pytest
from quick_sort_list import quick_sort_list


class TestQuickSortList:
    @staticmethod
    @pytest.mark.parametrize("elements, expected", [
        ([1, 0, -5, 111, 1024, 4096, 3], [-5, 0, 1, 3, 111, 1024, 4096]),
        ([5, 1, 100, 3, -1, 200, 199], [-1, 1, 3, 5, 100, 199, 200]),
        (["zet", "abba", "cool", "baba", "yeti"], ["abba", "baba", "cool", "yeti", "zet"]),
        ([], [])
    ])
    def test_should_return_sorted_num_list(elements, expected):
        result = quick_sort_list(elements)

        assert result == expected

    @staticmethod
    @pytest.mark.parametrize("arg", [
        123, "hello", None, True, False, {}, ()
    ])
    def test_should_return_that_arg_is_invalid(arg):
        expected = "Invalid argument passed to the function."
        result = quick_sort_list(arg)

        assert result == expected
