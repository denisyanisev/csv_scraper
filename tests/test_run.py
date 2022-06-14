import pytest

from contextlib import contextmanager
from run import parse_args


@contextmanager
def does_not_raise():
    yield


@pytest.mark.parametrize(
    'command,res,expected_raise',
    [
        (
                ([('--fields', 'date,campaign')], []), ['date', 'campaign'], does_not_raise()
        ),
        (
                ([], []), [], pytest.raises(ValueError)
        ),
    ]
)
def test_parse_args(command, res, expected_raise, mocker):
    mocker.patch(
        'getopt.getopt',
        return_value=command
    )
    with expected_raise:
        res1 = parse_args()
        assert res1 == res
