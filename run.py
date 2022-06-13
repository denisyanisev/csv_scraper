import pandas as pd
import getopt
import json
import sys


url = 'https://drive.google.com/file/d/1zLdEcpzCp357s3Rse112Lch9EMUWzMLE/view?output=csv'
url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
fields = ()

try:
    argv = sys.argv[1:]
    options, args = getopt.getopt(sys.argv[1:], '', ['fields='])
    fields = options[0][1].split(',')
except getopt.GetoptError:
    print('Wrong arguments! Please use command like --fields date,campaign')

try:
    df = pd.read_csv(url, usecols=fields)
    res = df.to_json(orient='records')
    res = {'data': json.loads(res)}
    print(res)
except ValueError:
    print('Wrong parameters!')
