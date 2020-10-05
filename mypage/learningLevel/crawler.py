import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random
import pandas as pd
import pyperclip
from bs4 import BeautifulSoup as bs

def eclass(sid, spw, ccode):
    l = []
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome("C:/Users/yooso/Desktop/유소영/동국대 4-2/종합설계/2020-1-CECD3-ANC-1/mypage/learningLevel/static/chromedriver", chrome_options=options)
    driver.get("https://eclass.dongguk.edu/Main.do?cmd=viewHome")
    driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/ul/li[1]/a').click()
    driver.find_element_by_name('userDTO.userId').send_keys(sid)
    driver.find_element_by_name('userDTO.password').send_keys(spw)
    driver.find_element_by_xpath('//*[@id="loginForm-member"]/fieldset/p/a').click()
    time.sleep(2)
    driver.get("https://eclass.dongguk.edu/Main.do?cmd=moveMenu&mainDTO.parentMenuId=menu_00026&mainDTO.menuId=menu_00031")
    soup = bs(driver.page_source, 'html.parser')
    classes = soup.find_all("tr")
    for i in classes:
        try:
            name = i.find("a").text
            code = i.select_one("td:nth-of-type(2)").text
            link = i.find('a')['href']
            sidx = link.find("(")
            eidx = link.find(")")
            link = link[sidx+2:eidx-1]
            if code == ccode:
                break
        except:
            print("")
    go = "https://eclass.dongguk.edu/Report.do?cmd=viewReportInfoPageList&boardInfoDTO.boardInfoGubun=report&courseDTO.courseId="+link+"&mainDTO.parentMenuId=menu_00104&mainDTO.menuId=menu_00063"
    driver.get(go)
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
    return l, name
    