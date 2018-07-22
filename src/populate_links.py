# @Author: Kartikay Shandil <kartikay101>
# @Date:   2018-07-21T18:44:16+05:30
# @Last modified by:   hunter
# @Last modified time: 2018-07-22T20:15:48+05:30



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import logging
import os
import time

filepath=os.path.realpath(__file__)
driverpath=filepath.replace("/src/populate_links.py","/driver/chromedriver")


options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
browser = webdriver.Chrome(driverpath,chrome_options=options)
browser.get('https://www.9anime.to')


def get_quality(video_quality):

    if video_quality==1:
        video_quality='360p'
    elif video_quality==2:
        video_quality='480p'
    elif video_quality==3 :
        video_quality='720p'
    elif video_quality==4:
        video_quality='1080p'
    return video_quality

def get_rapid_link(animeurl,quality):

    browser.get(animeurl)
    click_here=browser.find_element_by_class_name("cover")
    click_here.click()
    #waiting for iframe to load
    time.sleep(1)

    iframe=browser.find_elements_by_tag_name("iframe")[0]
    browser.switch_to_frame(iframe)


    final_link='this goes to browser'
    elems = browser.find_elements_by_xpath("//a")

    for elem in elems:
        dwnld_link=elem.get_attribute("href")
        final_link=dwnld_link #in case even 360p does not exist
        if not get_quality(video_quality) in dwnld_link:
            video_quality-=1
        else:
            final_link=dwnld_link
            break
    print(final_link)
    return final_link

def download_links(final_link):

    browser.get(final_link)
    video=browser.find_element_by_tag_name('video')

    filepath=os.path.realpath(__file__)
    filepath=filepath.replace('/src/populate_links.py','/res/links.txt')

    file=open(filepath,"a")
    file.write(video.get_attribute('src')+"\n")
    file.close()

animeurl=raw_input("Please Enter the URL of the Starting Episode :\n")
ep_cnt=raw_input("Enter The Number of Episodes To Download (Including Starting Episode) :\n")
video_quality=input("video quality")
ep_start=input("starting ep number")
ep_end=input("ending ep number")

ep_start-=1; #array starts at 0

browser.get(animeurl)

click_here=browser.find_element_by_class_name("cover")
click_here.click()
cntr=0;
all_links=[]
elems = browser.find_elements_by_xpath("//a[@href]")
for elem in elems:
    ep_link=elem.get_attribute("href")
    if animeurl in ep_link:
        all_links.append(ep_link)
        cntr=cntr+1

for i in range(ep_start,ep_end):
    print(all_links[cntr])
    download_links(get_rapid_link(all_links[i],video_quality))

browser.close()
