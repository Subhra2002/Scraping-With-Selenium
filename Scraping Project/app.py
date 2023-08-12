from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from openpyxl import load_workbook
import os
import pandas as pd
import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://user:1234@cluster0.mudo9en.mongodb.net/")
db = client.Pulse

def dataStore(name,Father,DateOfBirth):
        cousterdetails = db.cousterdetails
        doc ={"name":name,"father":Father,"DateOfBirth":DateOfBirth}
        cousterdetails.insert_one(doc)



driver = webdriver.Chrome()
driver.get("https://www.nmc.org.in/information-desk/indian-medical-register/")

floder = driver.find_element(by=By.XPATH , value = "/html/body/div[2]/div/div[2]/div/div/div/div/div[5]/div/div[3]/form/div[3]/div")
floder.click()
time.sleep(4)

year = driver.find_element(by=By.XPATH,value= "/html/body/div[2]/div/div[2]/div/div/div/div/div[5]/div/div[3]/form/div[3]/div/div/ul/li[3]" )
year.click()
time.sleep(2)
submit = driver.find_element(by=By.XPATH,value="/html/body/div[2]/div/div[2]/div/div/div/div/div[5]/div/div[3]/form/div[5]/div")
submit.click()
time.sleep(3)
for i in range(1,10):
        view = driver.find_element(by=By.XPATH,value=f"/html/body/div[2]/div/div[2]/div/div/div/div/div[5]/div/b/b/div/table/tbody/tr[{i}]/td[7]/a")
        view.click()
        time.sleep(2)
        # text = driver.find_element(by=By.XPATH,value ='//*[@id="doctorModalBody"]').text
        cross = driver.find_element(by=By.XPATH,value="/html/body/div[2]/div/div[2]/div/div/div/b/b/div/div[2]/div/div/div[1]/button/span")
        cross.click()
        # table = driver.find_element(by=By.XPATH,CLASS_NAME="table table-bordered")
        try:
                name = driver.find_element(by=By.XPATH,value='//*[@id="doctorBiodata"]/tbody/tr[1]/td[2]').text
                Father= driver.find_element(by=By.XPATH,value='//*[@id="doctorBiodata"]/tbody/tr[2]/td[2]').text
                DateOfBirth =driver.find_element(by=By.XPATH,value='//*[@id="doctorBiodata"]/tbody/tr[3]/td[2]').text
        # #         # dateofyear = driver.find_element(by=By.XPATH,value='//*[@id="doctorBiodata"]/tbody/tr[3]/td[4]').text
                # Regno= driver.find_element(by=By.XPATH,value='//*[@id="doctorBiodata"]/tbody/tr[4]/td[2]').text
        # #         StateCounlie = driver.find_element(by=By.XPATH,value='//*[@id="doctorBiodata"]/tbody/tr[5]/td[4]').text
                # universityname = driver.find_element(by=By.XPATH,value='//*[@id="doctorBiodata"]/tbody/tr[7]/td[2]').text
        #         print(name)
        #         print(Father)
        #         print(DateOfBirth)
        # #         # # print(dateofyear)
        #         print(Regno)
        #         # print(StateCounlie)
        #         print(universityname)
                dataStore(name,Father,DateOfBirth)
        except Exception as e:
                print(e)
        i+1
        time.sleep(2)

        # wb.save(book)





