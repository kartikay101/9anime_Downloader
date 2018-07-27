# @Author: Kartikay Shandil <kartikay101>
# @Date:   2018-07-21T18:44:16+05:30
# @Last modified by:   hunter
# @Last modified time: 2018-07-27T17:01:27+05:30



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
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("--disable-notifications")
browser = webdriver.Chrome(driverpath,chrome_options=options)
browser.get('https://www.9anime.to')

def input_link_clean(inp_link):

    cnt=0
    res=''
    for char in inp_link:
        if char=='/':
            cnt+=1
        if cnt==5:
            break
        res+=char
    return res

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
    time.sleep(4)

    iframe=browser.find_elements_by_tag_name("iframe")[0]
    browser.switch_to_frame(iframe)


    final_link='this goes to browser'
    elems = browser.find_elements_by_xpath("//a")
    quality_links=[]
    for elem in elems:
        dwnld_link=elem.get_attribute("href")
        #print("All download links"+dwnld_link)
        quality_links.append(dwnld_link)
        final_link=dwnld_link #in case even 360p does not exist

    flag=True
    while quality>=1 and flag:
        val=get_quality(quality)
        for link in quality_links:
            if val in link:
                final_link=link
                flag=False
        quality-=1

    return final_link

def download_links(final_link):

    browser.get(final_link)
    video=browser.find_element_by_tag_name('video')

    filepath=os.path.realpath(__file__)
    filepath=filepath.replace('/src/populate_links.py','/res/links.txt')

    file=open(filepath,"a")
    file.write(video.get_attribute('src')+"\n")
    file.close()



filepath=os.path.realpath(__file__)
filepath=filepath.replace('/src/populate_links.py','/res/data.txt')

reader=open(filepath,'r')

#getting required details
animeurl=reader.readline()
animeurl=input_link_clean(animeurl)
video_quality=int(reader.readline())
ep_start=int(reader.readline())
ep_end=int(reader.readline())

ep_start-=1; #array starts at 0

print("\nVisiting the Given Link.\nThis may take Time, please be patient\n")

browser.get(animeurl)

click_here=browser.find_element_by_class_name("cover")
click_here.click()

main_window=browser.window_handles[0]  # closing the annoying ads
new_window=browser.window_handles[1]
browser.switch_to_window(new_window)
browser.close()
browser.switch_to_window(main_window)

cntr=0;
all_links=[]
elems = browser.find_elements_by_xpath("//a[@href]")
for elem in elems:
    ep_link=elem.get_attribute("href")
    #print(ep_link)
    if animeurl in ep_link:
        all_links.append(ep_link)
        cntr=cntr+1

for i in range(ep_start,ep_end):
    print("Fetching Episode"+str(i+1))
    download_links(get_rapid_link(all_links[i],video_quality))
    print("Link Fetched")

print("Starting download now")
browser.quit() # closing the browser
