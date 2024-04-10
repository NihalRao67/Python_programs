'''
Use beautiful soup to retrive URLs from a user defined position and to a depth defined by the user.
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = int(input('Enter count:'))
position = int(input('Enter position:'))
url_input = 'http://py4e-data.dr-chuck.net/known_by_Johnnie.html'
cnt = 0
while cnt <= count:
 if cnt == 0:
     new_url = url_input
 else:    
     new_url = tags[position - 1].get('href', None)  
 print(f'Retrieving: f{new_url}')
 html = urllib.request.urlopen(new_url, context=ctx).read()
 soup = BeautifulSoup(html, 'html.parser')
 tags = soup('a')
    
 cnt += 1   
