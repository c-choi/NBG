# -*- coding:utf-8 -*-
import os
from datetime import datetime
import urllib.request
from pprint import pprint
import json
import csv
import re

client_id = "Qj4DV8bUnyI5tLo2aKtj"
client_secret = "ibhX5OHNME"

today = str(datetime.date(datetime.now()))
cwd = os.getcwd()

print("검색어를 입력해주세요")
search_word = input()
encText = urllib.parse.quote(search_word)
txt_file = str(search_word + "_shop.txt")
csv_file = str(search_word + "_shop.csv")
file_path = str(cwd + "/" + today + "/" + csv_file)

def search(e, n):
    url = "https://openapi.naver.com/v1/search/shop.json?query=" + e + "&display=100&start=" + n

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)  # , data=data.encode("utf-8")
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        if not os.path.exists(cwd + "/" + today):
            try:
                os.makedirs(cwd + "/" + today)
            except OSError as error:
                if error.errno != errno.EEXIST:
                    raise

        json_rt = response_body.decode('utf-8')
        data = json.loads(json_rt)
        # pprint(data['items'])


        data_parsed = data['items']
        json_link(data_parsed)
        shop_data = open(cwd + "/" + today + "/" + csv_file, 'a', encoding='utf-16')
        csvwriter = csv.writer(shop_data, dialect='excel-tab')
        count = 0
        for shp in data_parsed:
            if count == 0:
                header = shp.keys()
                if n == str(1):
                    csvwriter.writerow(header)
                count += 1
            csvwriter.writerow(shp.values())
        shop_data.close()
        f = open(cwd + "/" + today + "/" + search_word + "/" + txt_file, 'a')
        f.write(json_rt)
        f.close()
    else:
        print("Error Code:" + rescode)



# 링크 추려내기

def json_link(d):
    for j in d:
        links_list = j['link']
        # print(links_list)
        if not os.path.exists(cwd + "/" + today + "/" + search_word):
            try:
                os.makedirs(cwd + "/" + today + "/" + search_word)
            except OSError as error:
                if error.errno != errno.EEXIST:
                    raise
        file_name = str(cwd + "/" + today + "/" + search_word + "/queue.txt")
        g = open(file_name, "a")
        g.write(links_list + "\n")
        g.close()



start = (1, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1000)
for i in start:
    try:
        search(encText, str(i))
    except:
        print("검색 결과가 없습니다")
        quit()
print(search_word + "에 대한 네이버 쇼핑 검색결과 입니다")
os.system("open -a 'Microsoft Excel.app' '%s'" %file_path)