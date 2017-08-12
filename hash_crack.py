#! usr/bin/env python3
# -*-coding-*-:utf-8
import requests
from lxml import etree


print("在线hash破解")
print("author_by:Aasron\n")
url = "http://www.objectif-securite.ch/ophcrack.php"
headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Encoding":"gzip,deflate",
           "Content-Type":"application/x-www-form-urlencoded",
           "Referer":"http://www.objectif-securite.ch/ophcrack.php",
           "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Host" : "www.objectif-securite.ch",
           "Referer" : "http://www.objectif-securite.ch/ophcrack.php",
           "Upgrade-Insecure-Requests" : "1",
           "Connection": "close"
           }
hash_data = {'hash':input('please enter your hash:')}
hash_req = requests.post(url=url,data=hash_data,headers=headers).text
#print(hash_req)
key_html = etree.HTML(hash_req)
#print(key_html)
crack_result = key_html.xpath("//td[2]/b/text()")
for c in crack_result:
    print('PassWord:',c)
