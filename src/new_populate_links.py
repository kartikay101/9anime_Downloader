from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import logging
import os
import platform
import time
import sys

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
#browser.get('https://www.9anime.to')

#getting download details
myfile=open(filepath+"/res/details.dat")
animeurl=myfile.readline()
start=int(myfile.readline())
end=int(myfile.readline())
qual=int(myfile.readline())

def get_token(anime_url):
    return animeurl.split("/")[-1][:-1]

def setup():
    token='[data-id="'+get_token(animeurl)+'"]'
    print(token)
    todwnld=[x for x in range(start,end+1)]
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
        if(ep_head.find_elements_by_css_selector(token)):
            rapid_ephead=ep_head
            break

    #get list of all episodes
    eplist=rapid_ephead.find_elements_by_tag_name('li')
    d=dict()
    for li in eplist:
        db=li.find_element_by_tag_name('a').get_attribute('data-base')
        link=li.find_element_by_tag_name('a').get_attribute('href')
        d[db]=link

    #set the episodes to be downloaded
    todwnldlist=dict()
    for x in todwnld:
        no=str(x)
        if no in d.keys():
            todwnldlist[no]=d[no]
        else:
            print("Episode",no,"not in the list of available episodes")
    print(todwnldlist)
    get_actual_links(todwnldlist,'480p')
#get actual download links
def get_actual_links(ep_links,quality):

    for ep_no in ep_links.keys():
        browser.get(ep_links[ep_no])
        click_here=browser.find_element_by_class_name("cover")
        click_here.click()
        #wait for iframe to download
        time.sleep(4)
        #switch to the new loaded iframe
        iframe=browser.find_elements_by_tag_name("iframe")[0]
        browser.switch_to_frame(iframe)
        # TODO: Find better alternate
        videoplayer=browser.find_elements_by_id('home-video')

setup()
#quit after visit
browser.quit()
