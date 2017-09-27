from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
from datetime import datetime
import csv

today = str(datetime.date(datetime.now()))
time = str(datetime.timestamp(datetime.now()))
cwd = os.getcwd()
project_name = "NBG" #input()
csv_file = str(today + ".csv")
txt_file = str(today + ".txt")

if not os.path.exists(cwd + "/" + project_name + "/" + today):
    try:
        os.makedirs(cwd + "/" + project_name + "/" + today)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise

for p in range(1, 100):
    if p == 1:
        url = 'https://www.foodmerce.com/product/subMain.do?category=G&subCategory=M0051'
    else:
        url = 'https://www.foodmerce.com/product/subMain.do?category=G&nowPage=' + str(p) + '&subCategory=M0051'
        response = urlopen(url)
        plain_text = response.read()
        soup = BeautifulSoup(plain_text, 'html.parser')
        lists = soup.find("ul", {"class": "commodity"})
        table = lists.find_all('a')
        # print(table)
        g = 1


        for g in range(len(table)):
            if g == 1:
                g+=1
            else:
                data = table[g].text
                # print(data)
                g += 1
                f = open(cwd + "/" + project_name + "/" + today + "/" + txt_file, 'a')
                f.write(data)
                f.close()
                shop_data = open(cwd + "/" + project_name + "/" + csv_file, 'a',
                                 encoding='utf-16')
                csvwriter = csv.writer(shop_data)
                csvwriter.writerow([data])
            print(g)
    p += 1
# print(str(p) + " items found")


#BACKUP
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import os
# from datetime import datetime
# import csv
#
# today = str(datetime.date(datetime.now()))
# time = str(datetime.timestamp(datetime.now()))
# cwd = os.getcwd()
# project_name = "NBG" #input()
# csv_file = str(today + ".csv")
# txt_file = str(today + ".txt")
#
#    # TODO:정적페이지 크롤링 방법 사용
#
# if not os.path.exists(cwd + "/" + project_name + "/" + today):
#     try:
#         os.makedirs(cwd + "/" + project_name + "/" + today)
#     except OSError as error:
#         if error.errno != errno.EEXIST:
#             raise
#
# for p in range(1, 100):
#     if p == 1:
#         url = 'https://www.foodmerce.com/product/subMain.do?category=G&subCategory=M0053'
#     else:
#         url = 'https://www.foodmerce.com/product/subMain.do?category=G&nowPage=' + str(p) + '&subCategory=M0053'
#         response = urlopen(url)
#         plain_text = response.read()
#         soup = BeautifulSoup(plain_text, 'html.parser')
#         lists = soup.find("ul", {"class": "commodity"})
#         table = lists.find_all('a')
#         # print(table)
#         g = 1
#
#
#         for g in range(len(table)):
#             if g == 1:
#                 g+=1
#             else:
#                 data = table[g].text
#                 # print(data)
#                 g += 1
#                 f = open(cwd + "/" + project_name + "/" + today + "/" + txt_file, 'a')
#                 f.write(data)
#                 f.close()
#                 shop_data = open(cwd + "/" + project_name + "/" + csv_file, 'a',
#                                  encoding='utf-16')
#                 csvwriter = csv.writer(shop_data)
#                 csvwriter.writerow([data])
#             print(g)
#     p += 1
# # print(str(p) + " items found")
