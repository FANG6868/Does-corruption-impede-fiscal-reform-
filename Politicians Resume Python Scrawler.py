from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from xlutils.copy import copy
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import os
import xlwt
import xlrd
import sys

def click_by_time(driver, xpath, maxTime):  # preparation, no special meaning
    t = 0
    while t <= maxTime:
        if driver.find_element(By.XPATH, xpath) != None:
            driver.find_element(By.XPATH, xpath).click()
            break
        time.sleep(1)
        t += 1

xlsx = pd.ExcelFile(r'E:\A+ FangLin\Essay\Corruption\Text Files\Politicians Resume\officersCV.xlsx') #the location of the original file
data = pd.read_excel(xlsx, 'Sheet1') #the name of the sheet
for indexs in data.name: #index is the name of the colume, the name of the analyst we are looking for
    print(indexs)
    for position in data.shuji: #company is the name of the colume, the name of the company of the analyst
        print(position)
    key = str(position)+ str(indexs)
    chrome_options = Options()
    s = Service(executable_path=r'chromedriver.exe')
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.baidu.com/")

    searchingBox = driver.find_element(By.ID, 'kw')
    searchingBox.send_keys(key + Keys.ENTER)
    time.sleep(2)
    pattern = '百度百科' #find the websites related to linkedin
    titles = driver.find_elements(By.CLASS_NAME, 'bk_polysemy_1Ef6j')
    for title in titles:
        result = title.find_element(By.TAG_NAME, 'a')
        if '百度百科' in result.text:
            spans = title.find_elements(By.TAG_NAME, 'a')
            for span in spans:
                href = span.get_attribute('href')
                if 'related' not in str(href) and 'translate' not in str(href):
                    with open(r'E:\A+ FangLin\Essay\Corruption\Text Files\Politicians Resume\test_test.txt', 'a+', encoding="utf-8") as f:
                        f.write(str(href))
                        f.write('\n')
    time.sleep(1)
    driver.quit()
############################################
f = open(r'E:\A+ FangLin\Essay\Corruption\Text Files\Politicians Resume\test_test.txt','r')
urls = f.readlines()

excelname = r'E:\A+ FangLin\Essay\Corruption\Text Files\Politicians Resume\CV.xls' #open a new Excel and name it 'linkedin'
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('Sheet1',cell_overwrite_ok=True)
workbook.save(excelname)
count = 0

for url in urls:
    print(url)
    chrome_options = Options()
    s = Service(executable_path=r'chromedriver.exe')
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    time.sleep(8)

    try:
        name = driver.find_element(By.XPATH, './/dd[@class="lemmaWgt-lemmaTitle-title J-lemma-title"]').text
    except NoSuchElementException:
        name = 'no name'
    try:
        CV1 = driver.find_element(By.XPATH, './/div[@data-pid="1"]').text
    except NoSuchElementException:
        CV1 = 'no CV'
    try:
        CV2 = driver.find_element(By.XPATH, './/div[@data-pid="2"]').text
    except NoSuchElementException:
        CV2 = 'no CV'
    try:
        CV3 = driver.find_element(By.XPATH, './/div[@data-pid="3"]').text
    except NoSuchElementException:
        CV3 = 'no CV'
    try:
        CV4 = driver.find_element(By.XPATH, './/div[@data-pid="4"]').text
    except NoSuchElementException:
        CV4 = 'no CV'
    try:
        CV5 = driver.find_element(By.XPATH, './/div[@data-pid="5"]').text
    except NoSuchElementException:
        CV5 = 'no CV'
    try:
        CV6 = driver.find_element(By.XPATH, './/div[@data-pid="6"]').text
    except NoSuchElementException:
        CV6 = 'no CV'
    try:
        CV7 = driver.find_element(By.XPATH, './/div[@data-pid="7"]').text
    except NoSuchElementException:
        CV7 = 'no CV'
    try:
        CV8 = driver.find_element(By.XPATH, './/div[@data-pid="8"]').text
    except NoSuchElementException:
        CV8 = 'no CV'
    try:
        CV9 = driver.find_element(By.XPATH, './/div[@data-pid="9"]').text
    except NoSuchElementException:
        CV9 = 'no CV'
    try:
        CV10 = driver.find_element(By.XPATH, './/div[@data-pid="10"]').text
    except NoSuchElementException:
        CV10 = 'no CV'

    try:
        CV11 = driver.find_element(By.XPATH, './/div[@data-pid="11"]').text
    except NoSuchElementException:
        CV11 = 'no CV'
    try:
        CV12 = driver.find_element(By.XPATH, './/div[@data-pid="12"]').text
    except NoSuchElementException:
        CV12 = 'no CV'
    try:
        CV13 = driver.find_element(By.XPATH, './/div[@data-pid="13"]').text
    except NoSuchElementException:
        CV13 = 'no CV'
    try:
        CV14 = driver.find_element(By.XPATH, './/div[@data-pid="14"]').text
    except NoSuchElementException:
        CV14 = 'no CV'
    try:
        CV15 = driver.find_element(By.XPATH, './/div[@data-pid="15"]').text
    except NoSuchElementException:
        CV15 = 'no CV'
    try:
        CV16 = driver.find_element(By.XPATH, './/div[@data-pid="16"]').text
    except NoSuchElementException:
        CV16 = 'no CV'
    try:
        CV17 = driver.find_element(By.XPATH, './/div[@data-pid="17"]').text
    except NoSuchElementException:
        CV17 = 'no CV'
    try:
        CV18 = driver.find_element(By.XPATH, './/div[@data-pid="18"]').text
    except NoSuchElementException:
        CV18 = 'no CV'
    try:
        CV19 = driver.find_element(By.XPATH, './/div[@data-pid="19"]').text
    except NoSuchElementException:
        CV19 = 'no CV'
    try:
        CV20 = driver.find_element(By.XPATH, './/div[@data-pid="20"]').text
    except NoSuchElementException:
        CV20 = 'no CV'

    try:
        CV21 = driver.find_element(By.XPATH, './/div[@data-pid="21"]').text
    except NoSuchElementException:
        CV21 = 'no CV'
    try:
        CV22 = driver.find_element(By.XPATH, './/div[@data-pid="22"]').text
    except NoSuchElementException:
        CV22 = 'no CV'
    try:
        CV23 = driver.find_element(By.XPATH, './/div[@data-pid="23"]').text
    except NoSuchElementException:
        CV23 = 'no CV'
    try:
        CV24 = driver.find_element(By.XPATH, './/div[@data-pid="24"]').text
    except NoSuchElementException:
        CV24 = 'no CV'
    try:
        CV25 = driver.find_element(By.XPATH, './/div[@data-pid="25"]').text
    except NoSuchElementException:
        CV25 = 'no CV'
    try:
        CV26 = driver.find_element(By.XPATH, './/div[@data-pid="26"]').text
    except NoSuchElementException:
        CV26 = 'no CV'
    try:
        CV27 = driver.find_element(By.XPATH, './/div[@data-pid="27"]').text
    except NoSuchElementException:
        CV27 = 'no CV'
    try:
        CV28 = driver.find_element(By.XPATH, './/div[@data-pid="28"]').text
    except NoSuchElementException:
        CV28 = 'no CV'
    try:
        CV29 = driver.find_element(By.XPATH, './/div[@data-pid="29"]').text
    except NoSuchElementException:
        CV29 = 'no CV'
    try:
        CV30 = driver.find_element(By.XPATH, './/div[@data-pid="30"]').text
    except NoSuchElementException:
        CV30 = 'no CV'

    try:
        CV31 = driver.find_element(By.XPATH, './/div[@data-pid="31"]').text
    except NoSuchElementException:
        CV31 = 'no CV'
    try:
        CV32 = driver.find_element(By.XPATH, './/div[@data-pid="32"]').text
    except NoSuchElementException:
        CV32 = 'no CV'
    try:
        CV33 = driver.find_element(By.XPATH, './/div[@data-pid="33"]').text
    except NoSuchElementException:
        CV33 = 'no CV'
    try:
        CV34 = driver.find_element(By.XPATH, './/div[@data-pid="34"]').text
    except NoSuchElementException:
        CV34 = 'no CV'
    try:
        CV35 = driver.find_element(By.XPATH, './/div[@data-pid="35"]').text
    except NoSuchElementException:
        CV35 = 'no CV'
    time.sleep(5)

    oldwb = xlrd.open_workbook(excelname)
    newwb = copy(oldwb)
    ws = newwb.get_sheet(0)
    ws.write(count, 0, name)
    ws.write(count, 1, url)
    ws.write(count, 2, CV1)
    ws.write(count, 3, CV2)
    ws.write(count, 4, CV3)
    ws.write(count, 5, CV4)
    ws.write(count, 6, CV5)
    ws.write(count, 7, CV6)
    ws.write(count, 8, CV7)
    ws.write(count, 9, CV8)
    ws.write(count, 10, CV9)
    ws.write(count, 11, CV10)
    ws.write(count, 12, CV11)
    ws.write(count, 13, CV12)
    ws.write(count, 14, CV13)
    ws.write(count, 15, CV14)
    ws.write(count, 16, CV15)
    ws.write(count, 17, CV16)
    ws.write(count, 18, CV17)
    ws.write(count, 19, CV18)
    ws.write(count, 20, CV19)
    ws.write(count, 21, CV20)
    ws.write(count, 22, CV21)
    ws.write(count, 23, CV22)
    ws.write(count, 24, CV23)
    ws.write(count, 25, CV24)
    ws.write(count, 26, CV25)
    ws.write(count, 27, CV26)
    ws.write(count, 28, CV27)
    ws.write(count, 29, CV28)
    ws.write(count, 30, CV29)
    ws.write(count, 31, CV30)
    ws.write(count, 32, CV31)
    ws.write(count, 33, CV32)
    ws.write(count, 34, CV33)
    ws.write(count, 35, CV34)
    ws.write(count, 36, CV35)


    newwb.save(excelname)
    count+=1
    driver.quit()
