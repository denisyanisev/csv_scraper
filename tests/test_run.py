import pytest
import json
from run import scrape


@pytest.mark.parametrize(
    'command, res',
    [
        (['', 'date'], {'data': [{'date': '2021-11-23'}]}),
        (['', 'date,campaign'], {'data': [{'date': '2021-11-23', 'campaign': 'facebook'}]})
    ],
)
def test_scrape(command, res, mocker):
    mocker.patch(
        'getopt.getopt',
        return_value=command
    )
    mocker.patch(
        'run.fetch_results',
        return_value=res
    )

    url = 'http://test-url'
    assert json.loads(scrape(url)) == res
