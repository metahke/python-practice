# uses pytest-mock
# uses freezegun

from freezegun import freeze_time
import pytest
from calc_diff_app import calc_diff


class TestCalcDiffFunc:

    @staticmethod
    @pytest.mark.parametrize("case, expected", [
        ({
             'start_time': '2024-05-23T07:49:57+00:00',
             'end_time': '2024-05-29T13:24:13+00:00'
         }, 538456.0),
        ({
             'start_time': '2024-05-03T06:33:56+00:00',
             'end_time': None
         }, 2271017.0)
    ])
    @freeze_time('2024-05-29 13:24:13')
    def test_should_return_correct_time_diff_in_seconds(case, expected):
        result = calc_diff(case)

        assert result == expected
