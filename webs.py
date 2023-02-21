# import os
import re
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys   
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
def clean_html(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text) 
f = open("21centry2.csv", "w")   
f.write("Vendodhja,siperfaqja,cmimi\n") 


for page in range(1 , 10,1):
     driver.get("https://www.century21albania.com/properties?display=grid&business_type=rent&page" + str(page))
     elementet = driver.find_elements("xpath", "/html/body/div/section[1]/div/div/div/section/div/div/div/div[2]/div")
     for element in elementet:
          vendodhja = clean_html(element.find_element("xpath", "./div/a[2]/div[2]/h6[2]").get_attribute("innerHTML")).replace(",", ".").strip()
          sip=clean_html(element.find_element("xpath", "./div/a[2]/div[3]/div[1]").get_attribute("innerHTML")).replace("m2", "").strip()
          cmimi=clean_html(element.find_element("xpath", ". /div/a[2]/div[2]/h2").get_attribute("innerHTML")).replace("€", "").replace(",","").strip()
          f.write("{},{},{}\n".format(vendodhja,sip,cmimi)) 
f.close()


driver.close()
