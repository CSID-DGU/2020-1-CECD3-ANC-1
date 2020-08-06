import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random
import pandas as pd
import pyperclip
from bs4 import BeautifulSoup as bs

def eclass(sid, spw):
    l = []
    driver = webdriver.Chrome("C:\\Users\\yooso\\Downloads\\chromedriver_win32\\chromedriver")
    driver.get("https://eclass.dongguk.edu/Main.do?cmd=viewHome")
    driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/ul/li[1]/a').click()
    driver.find_element_by_name('userDTO.userId').send_keys(sid)
    driver.find_element_by_name('userDTO.password').send_keys(spw)
    driver.find_element_by_xpath('//*[@id="loginForm-member"]/fieldset/p/a').click()
    time.sleep(2)
    driver.get("https://eclass.dongguk.edu/Report.do?cmd=viewReportInfoPageList&boardInfoDTO.boardInfoGubun=report&courseDTO.courseId=S2019U0002001UCSE403101&mainDTO.parentMenuId=menu_00104&mainDTO.menuId=menu_00063")
    soup = bs(driver.page_source, 'html.parser')
    task = soup.find_all("div",{"class":"listContent pb20"})
    for item in task:
        d={}
        title = item.find("h4",{"class":"f14"}).text.replace("\n","").replace("\t","")
        date = item.find("tbody").find("td", {"class":"first"}).text.replace("\n","").replace("\t","")
        date = date.split(" ~ ")
        d["title"]=title
        d["start"]=date[0]
        d["end"]=date[1]
        l.append(d)
    df=pd.DataFrame(l)
    print(df)
    time.sleep(10)
    
eclass('id', 'pw')

