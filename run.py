import pandas as pd
import getopt
from urllib import error
import json
import sys


url = 'https://drive.google.com/file/d/1zLdEcpzCp357s3Rse112Lch9EMUWzMLE/view?output=csv'
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]


def fetch_results(target_url, fields):
    res = {}
    try:
        df = pd.read_csv(target_url, usecols=fields)
        res = df.to_json(orient='records')
        res = {'data': json.loads(res)}

    except (ValueError, error.HTTPError):
        print('Wrong parameters or target url!')
    return res


def scrape(target_url):
    fields = None
    try:
        options, args = getopt.getopt(sys.argv[1:], '', ['fields='])
        if options:
            fields = options[0][1].split(',')
    except getopt.GetoptError:
        print('Wrong parameters! Please use command like --fields date,campaign')
    res = fetch_results(target_url, fields)

    return json.dumps(res)


if __name__ == "__main__":
    print(scrape(url))
