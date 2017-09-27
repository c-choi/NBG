from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
import os
from datetime import datetime
import csv
from multiprocessing import Pool

today = str(datetime.date(datetime.now()))
time = str(datetime.timestamp(datetime.now()))
cwd = os.getcwd()
project_name = "NBG" #input()
keyword = input("검색어를 입력해주세요.\n")
csv_file = str(keyword + ".csv")
txt_file = str(today + ".txt")

if not os.path.exists(cwd + "/" + project_name + "/" + today):
    try:
        os.makedirs(cwd + "/" + project_name + "/" + today)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise

def multi_crawl(url):
    pool = Pool(8)
    results = pool.map(crawl, url)
    print(results)


def get_urls():
    searchList = []
    for g in range(1, 10):
        page_num = '&page=' + str(g)
        if g == 1:
            url = 'http://foodb2b.kr/search/?query=' + urllib.parse.quote(keyword)
            searchList.append(url)
        else:
            url = 'http://foodb2b.kr/search/?query=' + urllib.parse.quote(keyword) + page_num
            searchList.append(url)
    # print(searchList)
    multi_crawl(searchList)


def crawl(url):
    response = urlopen(url)
    plain_text = response.read()
    soup = BeautifulSoup(plain_text, 'html.parser')
    lists = soup.find_all("div", {"class": "company-panel"})
    csv_data = []
    for p in range(len(lists)):
        title = lists[p].find("h4").text.strip()
        item = lists[p].find_all("p")
        # link = list[p].find_all("a")
        data = [title]
        for j in range(len(item)):
            if j != 0:
                a = item[j].text.strip()
                data.append(a)
        # print(data)
        csv_data.append(data)
    # print(csv_data)
    write_csv(csv_data)



def write_csv(data):
    f = open(cwd + "/" + project_name + "/" + today + "/" + csv_file, 'a', encoding='utf-16')
    csvwriter = csv.writer(f)
    for i in range(len(data)):
        for j in range(len(data[i])):
            row = data[i][j]
            print([row])
            csvwriter.writerow([row])
        csvwriter.writerow('\n')

get_urls()