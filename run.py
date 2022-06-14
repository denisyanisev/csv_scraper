import getopt
import json
import logging
import sys
from urllib import error

import pandas as pd

logger = logging.getLogger(__name__)

source_url = 'https://drive.google.com/file/d/1zLdEcpzCp357s3Rse112Lch9EMUWzMLE/view?output=csv'
url = 'https://drive.google.com/uc?id=' + source_url.split('/')[-2]


def parse_args():
    options, args = getopt.getopt(sys.argv[1:], '', ['fields='])
    if not options:
        raise ValueError
    fields = options[0][1].split(',')
    return fields


def fetch_csv(file, fields):
    df = pd.read_csv(file, usecols=fields)
    res = df.to_json(orient='records')
    res = {'data': json.loads(res)}
    return res


def main():
    # Parse and check script options and args
    try:
        fields = parse_args()
        if not fields:
            raise ValueError
    except (ValueError, getopt.GetoptError):
        logger.error('Wrong parameters! Please use command like --fields date,campaign')
        sys.exit(2)

    # Fetch csv file and parse it to json with pandas
    try:
        res = fetch_csv(url, fields)
    except (ValueError, error.HTTPError) as e:
        logger.error('Wrong parameters or bad csv file!')
        logger.error(f'Error: {e}')
        sys.exit(2)

    print(json.dumps(res))


if __name__ == '__main__':
    main()
