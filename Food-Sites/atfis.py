from bs4 import BeautifulSoup
from selenium import webdriver

comp_name = input("회사명을 입력해주세요: ")
keyword = input("검색어를 입력해주세요: ")

url = 'https://www.atfis.or.kr/business/M002040000/list.do?searchTopIndustry=ALL&searchKeyIndicators=S' \
      '&searchKeyIndicators=E&searchKeyIndicators=N&businessOpen=001&_businessOpen=on&businessOpen=002' \
      '&_businessOpen=on&businessOpen=003&_businessOpen=on&businessOpen=004&_businessOpen=on&businessOpen=005' \
      '&_businessOpen=on&_businessOpen=on&sortOrderBy=S_DESC&searchMinYear=2016&searchMaxYear=2016&recordCount=100' \
      '&searchBusinessNm=' + str(comp_name) + '&searchProductItem=' + str(keyword) \
      + '&x=0&y=0'

driver = webdriver.Chrome('/Users/cloudy/anaconda/lib/python3.6/site-packages/selenium/chromedriver')
driver.get(url)
driver.implicitly_wait(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
lists = soup.find_all("table", {"class": "table_view2"})
try:
    tbody = lists[0].find("tbody")
    tablerow = tbody.find_all("tr")

    sbody = lists[1].find("tbody")
    stablerow = sbody.find_all("tr")

    data = []

    for t, s in zip(tablerow, stablerow):
        td = t.find_all("td")
        row = []
        for r in td:
            row.append(r.text.strip())
        data.append(row)

        # for s in stablerow:
        sd = s.find_all("td")
        srow = []
        for y in sd:
            srow.append(y.text.strip())
        data.append(srow)
        print(row[2] + ', 매출액: ' + srow[0] + ', 영업이익: ' + srow[1] + ', 순이익: ' + srow[2])
except:
    print("검색 결과가 없습니다.")
# data = lists[0].find_all("td", {"class": "ellipsis"})
# dic = {}
# for i in range(len(data)):
#     text = data[i].text.strip()
#     # try:
#     #     dic[title].append(text)
#     # except:
#     #     dic[title] = text
#     print(text)
# print("-" * 100)

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint