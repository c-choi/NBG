# -*- coding:utf-8 -*-
import os
from datetime import datetime
import urllib.request
import sys
import json
client_id = "Qj4DV8bUnyI5tLo2aKtj"
client_secret = "ibhX5OHNME"

today = str(datetime.date(datetime.now()))
cwd = os.getcwd()

print("검색어를 입력해주세요")
search_word = input()
encText = urllib.parse.quote(search_word)
# data = "source=ko&target=en&text=" + encText
# url = "https://openapi.naver.com/v1/language/translate"
url = "https://openapi.naver.com/v1/search/webkr.json?query=" + encText + "&display=20"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request) # , data=data.encode("utf-8")
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
    if not os.path.exists(cwd + "/" + today):
        try:
            os.makedirs(cwd + "/" + today)
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise

    f = open(cwd+ "/" + today + "/" + search_word + "_webkr.txt", 'w')
    f.write(response_body.decode('utf-8'))
    f.close()
    # print(f)
    # json_rt = response_body.decode('utf-8')
    # py_rt = json.loads(json_rt)

else:
    print("Error Code:" + rescode)


