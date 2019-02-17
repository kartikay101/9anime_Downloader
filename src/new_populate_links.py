from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import logging
import os
import platform
import time
import sys

def get_token(anime_url):
    return animeurl.split("/")[-1]
#getting driver
filepath=os.path.realpath(__file__).replace("/src/new_populate_links.py","")
driverpath=filepath+"/driver/chromedriver"

#running chrome headless
options = Options()
#options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("--disable-notifications")

#visiting the website
browser = webdriver.Chrome(driverpath,chrome_options=options)
browser.get('https://www.9anime.to')

#getting download details
myfile=open(filepath+"/res/details.dat")
animeurl=myfile.readline()
start=int(myfile.readline())
end=int(myfile.readline())
qual=int(myfile.readline())
token=get_token(animeurl)

#visiting the website
browser.get(animeurl)

#checking if RapidVideo server exists for the given anime
server=browser.find_elements_by_class_name("tab")
exists=False
for i in server:
    if i.text=='RapidVideo':
        i.click()
        exists=True
        break
if not exists:
    browser.quit()
    sys.exit("The server for RapidVideo does not exist,\
    \nWe cannot download this anime")

#getting all the episodes
ep_heads=browser.find_elements_by_css_selector(".episodes.range.active")
#selecting links from RapidVideo only
rapid_ephead=ep_heads[0]
for ep_head in ep_heads:
    print(ep_head.find_element_by_tag_name("li").get_attribute("data-id"))
print(rapid_ephead.get_attribute("innerHTML"))
#quit after visit
browser.quit()
