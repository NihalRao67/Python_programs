'''
Use Beautiful Soup to parse through a html file and find a particular tag.
Then extract the value at the Tag and compute the total sum
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://py4e-data.dr-chuck.net/comments_42.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
tot_sum = 0
#print(tags)
for tag in tags:
    print(tag, tag.contents[0])
    if tag.contents[0] is not None and len(tag.contents[0]) > 0:
        tot_sum += int(tag.contents[0])
        #print(tot_sum)
print(f'Sum = {tot_sum}')        