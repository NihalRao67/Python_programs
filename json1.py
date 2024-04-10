'''
Use python to read json documents and extract values from keys.
'''

import urllib.request, urllib.parse, urllib.error
import json
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_2003674.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()


info = json.loads(data)
tot_sum = 0
lst = info['comments']
#print(lst)

for val in lst:
    tot_sum += val['count']

print(f'Sum = {tot_sum}')