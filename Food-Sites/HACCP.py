from selenium import webdriver
from selenium.webdriver.support.ui  import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pprint import pprint

comp_name = input("회사명을 입력해주세요: ")
keyword = input("검색어를 입력해주세요: ")
url = 'http://www.foodsafetykorea.go.kr/portal/specialinfo/searchInfoHaccpCompany.do?menu_grp=MENU_NEW04&menu_no=2816'

driver = webdriver.Chrome('/Users/cloudy/anaconda/lib/python3.6/site-packages/selenium/chromedriver')
driver.get(url)

driver.implicitly_wait(1)
button = '//*[@id="wrap"]/main/section/div[2]/div[1]/div/fieldset/ul/li[5]/a'
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="listFrame"]/tr[1]/td[1]')))

if comp_name != "":
    Select(driver.find_element_by_xpath('//*[@id="search_type"]')).select_by_visible_text('업체명')
    driver.find_element_by_xpath('//*[@id="search_keyword"]').send_keys(comp_name)
else:
    Select(driver.find_element_by_xpath('//*[@id="search_type"]')).select_by_visible_text('품목')
    driver.find_element_by_xpath('//*[@id="search_keyword"]').send_keys(keyword)


try:
    driver.find_element_by_xpath(button).click()
except:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="listFrame"]/tr[1]/td[1]')))
    driver.find_element_by_xpath(button).click()

driver.implicitly_wait(5)
WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[1]')))

data = EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]'))
if data:
    Select(driver.find_element_by_xpath('//*[@id="show_cnt"]')).select_by_visible_text('50개씩')


def run(p):
    if p != 2:
        driver.find_element_by_xpath('//*[@id="wrap"]/main/section/div[2]/div[2]/div/ul/li[' + str(p) + ']').click()

        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[1]')))

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find("table", {"id": "board"})
        # header = table.find("thead")
        # headrow = header.find_all("th")
        tbody = table.find("tbody", {"id": "listFrame"})
        tablerow = tbody.find_all("tr")

        data = []

        for t in tablerow:
            td = t.find_all("td")
            row = []
            for r in td:
                row.append(r.text)
            data.append(row)
            print(row[2])

# 업체 전체 정보
# if data:
#     pprint(data)
# else:
#     print("no result")
#     driver.quit()

#TODO: 항목 개수 센 뒤 양이 적으면 루프 중지
for p in range(2, 10):
    if data:
        run(p)
    else:
        print("no more result")

