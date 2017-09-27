# -*- coding:utf-8 -*-
import os
from datetime import datetime
import urllib.request
from pprint import pprint
import json

client_id = "Qj4DV8bUnyI5tLo2aKtj"
client_secret = "ibhX5OHNME"

today = str(datetime.date(datetime.now()))
cwd = os.getcwd()

print("검색어를 입력해주세요")
search_word = input()
encText = urllib.parse.quote(search_word)


def search(num):
    media = select[int(num)]
    kor = select[int(str(1) + str(num))]

    url = "https://openapi.naver.com/v1/search/" + media + ".json?query=" + encText + "&display=20"

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

        f = open(cwd + "/" + today + "/" + search_word + "_" + media + ".txt", 'w')
        json_rt = response_body.decode('utf-8')
        data = json.loads(json_rt)
        pprint(data['items'])
        f.write(json_rt)
        f.close()
        json_link(data['items'])
        # print(data['items'][1]['link'])
    else:
        print("Error Code:" + rescode)

    print(search_word + "에 대한 " + kor + " 검색결과 입니다")


# 링크 추려내기

def json_link(d):
    for j in d:
        links_list = j['link']
        print(links_list)
        if not os.path.exists(cwd + "/" + search_word):
            try:
                os.makedirs(cwd + "/" + search_word)
            except OSError as error:
                if error.errno != errno.EEXIST:
                    raise
        file_name = str(cwd + "/" + search_word + "/queue.txt")
        g = open(file_name, "a")
        g.write(links_list + "\n")
        g.close()
        # os.system("link_crawler.py")

        # TODO: 링크 속 본문에서 원하는 단어 발견 후 종합하기



print("검색매체를 선택해주세요. \n  \n 1. 웹문서 \n 2. 뉴스 \n 3. 전문자료 \n 4. 지식in \n 5. 백과사전 \n 6. 쇼핑")
select = {
    1: "webkr",
    2: "news",
    3: "doc",
    4: "kin",
    5: "encyc",
    6: "shop",
    9: "all",
    11: "웹문서",
    12: "뉴스",
    13: "전문자료",
    14: "지식in",
    15: "백과사전",
    16: "쇼핑",
    19: "전체검색"
}
num = int(input())

if num == int(9):
    for i in range(1, 6):
        search(i)
        i += 1
else:
    search(num)
