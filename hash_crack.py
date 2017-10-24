#! usr/bin/env python3
# -*-coding-*-:utf-8
import requests
import json
import time


print("HASH破解(利用第三方接口,方便本地查询)")
print("Author_by:Aasron\n")
url = "http://www.objectif-securite.ch/demo.php/crack"
headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Encoding":"gzip,deflate",
           "Content-Type":"application/json",
           "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Host" : "www.objectif-securite.ch"
           }
hash_value = json.dumps({"value":input("Input Your Windows Hash:")})
start_time = time.time()
hash_msg = requests.post(url=url,data=hash_value,headers=headers).content.decode('utf-8')
end_time = time.time()
hash_password = json.loads(hash_msg)
#print("正在破解密码中，请稍等.....")
if "Invalid input" in hash_password['msg']:
        print("HASH长度错误,请重新输入")
else:
    print("正在破解密码中,请稍等.....")
    time.sleep(1)
    print("破解成功:"+hash_password['msg'])
    print("耗时:"+str(end_time-start_time)+"秒")
