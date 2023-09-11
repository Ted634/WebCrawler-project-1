# -*- coding: utf-8 -*-
"""
Created on Sat May 27 21:58:59 2023

@author: user
"""

#%% 爬取交通部觀光局觀光統計網站

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://stat.taiwan.net.tw/outboundSearch')

sleep(1)
# elem = driver.find_element(By.ID, 'staticWay')
# print(elem.text)
selectYear = driver.find_element(By.CLASS_NAME, 'form-label.pl-0').click()
# selectYear = driver.find_elements(By.CLASS_NAME, 'form-label.pl-0')[1].click()
# print(selectYear)
select_Time = Select(driver.find_element(By.ID, 'year'))
select_startYear = select_Time.select_by_visible_text(u'102(2013)')

selectCountry0 = driver.find_element(By.ID, 'groupCountry0').click()
selectCountry1 = driver.find_element(By.ID, 'groupCountry1').click()
selectCountry2 = driver.find_element(By.ID, 'groupCountry2').click()
selectCountry3 = driver.find_element(By.ID, 'groupCountry3').click()
selectCountry4 = driver.find_element(By.ID, 'groupCountry4').click()
selectCountry5 = driver.find_element(By.ID, 'groupCountry5').click()

submit = driver.find_element(By.CLASS_NAME, 'btn.btn-danger').click()

# element = WebDriverWait(driver,5).until(
#     expected_conditions.presence_of_element_located((By.CLASS_NAME,'col-md-12'))
#     )
sleep(2)

text_list = []
title_list = []
year_list = []

soup = BeautifulSoup(driver.page_source, 'lxml')

table_title = soup.select('th.numeric')
for title in table_title:
    # print(title.text)
    title_list.append(title.text)

table_year = soup.select('th.td-center')
for year in table_year:
    # print(year.text)
    year_list.append(year.text)

table_text = soup.select('td.numeric')
for t in table_text:
    # print(t.text)
    text_list.append(t.text.replace(',', ''))

# print(title_list)
# print(year_list)
# print(text_list)

asia = text_list[::7]
# print(asia)

africa = text_list[1::7]
# print(africa)

americas = text_list[2::7]
# print(americas)

oceania = text_list[3::7]
# print(oceania)

europe = text_list[4::7]
# print(europe)

unknow = text_list[5::7]
# print(unknow)

total = text_list[6::7]
# print(total)

final_text = [year_list, asia, africa, americas, oceania, europe, unknow, total]
# print(final_text)

data = {}
for title, text in zip(title_list, final_text):
    data[title] = text
# print(data)

data_df = pd.DataFrame(data)
# print(data_df)

data_df.to_csv("TravelDestination_102_111.csv",encoding="utf-8-sig",index=False, header=True)

driver.quit()