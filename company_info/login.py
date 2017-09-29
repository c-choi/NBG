from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

# driver = webdriver.Firefox()
# driver = webdriver.PhantomJS('/Users/cloudy/anaconda/bin/phantomjs')
driver = webdriver.Chrome('/Users/cloudy/anaconda/lib/python3.6/site-packages/selenium/chromedriver')
driver.implicitly_wait(3)
driver.get('https://sminfo.mss.go.kr/')
original = driver.current_window_handle
original_name = original.title()
window_num = len(driver.window_handles)

driver.find_element_by_name('login_id').send_keys('cchoi1989')
driver.find_element_by_name('login_password').send_keys("CcPs4141")
driver.find_element_by_xpath('//*[@id="content"]/div[1]/form/fieldset/div/input').click()

for i in range(1, window_num + 1):
    try:
        driver.switch_to.window(driver.window_handles[i])
        current_window = driver.window_handles[i]
        print(current_window.upper() + " " + original_name.upper())
        if current_window.upper() != original_name.upper():
            driver.close()
    except:
        i = 1

driver.switch_to.window(original)

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)
menu = driver.find_element_by_xpath('//*[@id="header"]/div/div[1]/ul/li[1]/div/a/img')
actions.move_to_element(menu).perform()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#header > div > div.menu > ul > li.m1 > div > a')))
driver.find_element_by_xpath('//*[@id="header"]/div/div[1]/ul/li[1]/ul/li[1]/a').click()

driver.implicitly_wait(3)
cpname = input('회사명을 입력해주세요\n')
# cpname = "네모아이이지"
driver.find_element_by_xpath('//*[@id="searchTxt"]').send_keys(cpname)
driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/fieldset/div[2]/p/input').click()


#
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
#
# cptitle = soup.find_all('strong')
#
# # html = soup.find_all("strong")
# count = len(cptitle)
# # pattern = "('(주)'|'주식회사'|'')" + cpname + "('(주)'|'주식회사'|'')"
# for i in range(count):
#     # print(cptitle[i].text)
#     titlen = cptitle[i].text
#     # TODO: 회사명칭 찾아내는 방법 찾기
#     if re.compile(pattern, titlen):
#         print(titlen)
#         driver.find_element(cptitle[i]).click()
#         collect_text()
#     else:
#         # print(cptitle[i].text)
#         i += 1
#
#         #// *[ @ id = "container"] / div / div / div[2] / div[3] / p / a[1] 2page
#         #// *[ @ id = "container"] / div / div / div[2] / div[3] / p / a[2] 3page
#
#     # elif '(주)' + cpname in cptitle[i].text:
#     #     print(cptitle[i].text)
#     #     driver.find_element(cptitle[i]).click()
#     # elif cpname + '(주)' in cptitle[i].text:
#     #     print(cptitle[i].text)
#     #     driver.find_element(cptitle[i]).click()
#
# def collect_text():
#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')
#
#     basic_info = soup.find_all('headers')
#     print(basic_info)