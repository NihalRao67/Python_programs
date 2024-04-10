import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = 'https://py4e-data.dr-chuck.net/comments_42.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
    
count_lst = tree.findall('comments/comment')
tot_sum = 0
for lst in count_lst:
    tot_sum += int(lst.find('count').text)    

print(f'Sum = {tot_sum}')