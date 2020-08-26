Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
a = input ("enterComment: ")
text = a         #u''
#th = u'[ก-๙]+'   #th = u'[\u0E01-\u0E2E]+' # หรือใช้โค้ด th = u'[ก-ฮ]+'
en = u'[a-z,A-Z,  , \d ,-,*,.,~,),(,//,:,=,&,,+,?, \s,--,​]+'

b = re.sub(en,"",text)
#b = th

#match = re.search(th,text,  re.U) # re.U เป็นคำสั่งใช้ Regular expression ใน unicode
#print(match.group())
print(b)


import requests
url = "https://api.aiforthai.in.th/ssense"
 
text = a
params = {'text':text}
 
headers = {
    'Apikey': "d33sBwGGDwjNkuQ88jJrf3tBsQWDkaoX"
    }
 
response = requests.get(url, headers=headers, params=params)
 
print(response.json())

