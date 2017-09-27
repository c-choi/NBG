# -*- coding:utf-8 -*-
import os
from datetime import datetime
import urllib.request
from pprint import pprint
import json
import csv
import openpyxl

client_id = "Qj4DV8bUnyI5tLo2aKtj"
client_secret = "ibhX5OHNME"

today = str(datetime.date(datetime.now()))
cwd = os.getcwd()

wb = openpyxl.Workbook()
ws = wb.active

print("프로젝트명을 입력해주세요")
project_name = "NBG" #input()
print("NBG")

print("검색어를 입력해주세요")
search_word = input()
encText = urllib.parse.quote(search_word)
txt_file = str(search_word + ".txt")
csv_file = str(search_word + ".csv")
xlsx_file = str(search_word + ".xlsx")
file_path = str(cwd + "/" + project_name + "/" + today + "/" + xlsx_file)

def search(e, n):
    url = "https://openapi.naver.com/v1/search/shop.json?query=" + e + "&display=100&start=" + n

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)  # , data=data.encode("utf-8")
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        if not os.path.exists(cwd + "/" + project_name + "/" + today + "/" + search_word):
            try:
                os.makedirs(cwd + "/" + project_name + "/" + today + "/" + search_word)
            except OSError as error:
                if error.errno != errno.EEXIST:
                    raise


        json_rt = response_body.decode('utf-8')
        data = json.loads(json_rt)
        pprint(data['items'])


        data_parsed = data['items']
        json_link(data_parsed)
        shop_data = open(cwd + "/" + project_name + "/" + today + "/" + search_word + "/" + csv_file, 'a', encoding='utf-16')
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
        # f = open(cwd + "/" + project_name + "/" + today + "/" + txt_file, 'a')
        # f.write(json_rt)
        # f.close()
    else:
        print("Error Code:" + rescode)



# 링크 추려내기

def json_link(d):
    for j in d:
        links_list = j['link']
        # print(links_list)
        if not os.path.exists(cwd + "/" + project_name + "/" + today + "/" + search_word):
            try:
                os.makedirs(cwd + "/" + project_name + "/" + today + "/" + search_word)
            except OSError as error:
                if error.errno != errno.EEXIST:
                    raise
        file_name = str(cwd + "/" + project_name + "/" + today + "/" + search_word + "/queue.txt")
        g = open(file_name, "a")
        g.write(links_list + "\n")
        g.close()



start = (1, 101, 201, 301, 401, 501, 601, 701, 801, 901, 1000)
for i in start:
    search(encText, str(i))
print(search_word + "에 대한 네이버 쇼핑 검색결과 입니다")

shop_csv = open(cwd + "/" + project_name + "/" + today + "/" + search_word + "/" + csv_file, 'r', encoding='utf-16')
reader = csv.reader(shop_csv, dialect='excel-tab')
for row in reader:
    ws.append(row)
wb.save(cwd + "/" + project_name + "/" + today + "/" + search_word + '.xlsx')
os.system("open -a 'Microsoft Excel.app' '%s'" %file_path)