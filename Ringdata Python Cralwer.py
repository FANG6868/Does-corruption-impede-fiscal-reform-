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
import requests

def click_by_time(driver, xpath, maxTime):  # preparation, no special meaning
    t = 0
    while t <= maxTime:
        if driver.find_element(By.XPATH, xpath) != None:
            driver.find_element(By.XPATH, xpath).click()
            break
        time.sleep(1)
        t += 1

xlsx = pd.ExcelFile(r'E:\A+ FangLin\HKU RA\data2.xlsx') #the location of the original file
data = pd.read_excel(xlsx, 'Sheet1') #the name of the sheet
for city in data.City: #index is the name of the colume, the name of the analyst we are looking for
    print(city)
    key = str(city)+' 省直管县'+' 财政'+' 改革'+' 反对'
    chrome_options = Options()
    s = Service(executable_path=r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.ringdata.com/news/advanced/")
    searchingBox = driver.find_element(By.XPATH, '//*[@class="el-input__inner"]')
    searchingBox.send_keys(key + Keys.ENTER)
    time.sleep(2)
    search = driver.find_element(By.XPATH, '//*[@class="el-button el-button--primary el-button--mini"]').click()
    time.sleep(5)

    try:
        infor = driver.find_element(By.XPATH, './/ul[@class="year-list"]').text
    except NoSuchElementException:
        infor = 'no news'
    print(infor)


    excelname = r'E:\A+ FangLin\HKU RA\news.xls'
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Sheet1', cell_overwrite_ok=True)
    workbook.save(excelname)
    count = 0

    time.sleep(1)
    oldwb = xlrd.open_workbook(excelname)
    newwb = copy(oldwb)
    ws = newwb.get_sheet(0)
    ws.write(count, 1, infor)
    newwb.save(excelname)
    count+=1
    driver.quit()
