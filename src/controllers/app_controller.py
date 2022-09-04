import glob
import time

import requests
from selenium import webdriver
from src.managers.youtube_manager import YoutubeManager
from src.helpers.mp4_to_mp3_helper import Mp4toMp3Helper
import os
from bs4 import BeautifulSoup

class AppController:
    def __init__(self,video_url,playlist = False):

        url = video_url
        if playlist:
            fireFoxOptions = webdriver.FirefoxOptions()
            fireFoxOptions.headless = True

            driver = webdriver.Firefox(executable_path=r'geckodriver', options=fireFoxOptions)
            driver.get(url)
            time.sleep(7)

            lol = []
            try:
                title = driver.find_elements("xpath",
                                             "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/ytd-playlist-panel-renderer/div/div[1]/div/div[1]/div[1]/h3[1]/yt-formatted-string/a")[
                    0].text.replace(" ", "_")
            except:
                title = input("input title >")

            x = driver.find_elements(by="xpath",
                                     value="/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/ytd-playlist-panel-renderer/div/div[2]")[0].find_elements("tag name", value="a")
            for links in x:
                lol.append(links.get_attribute("href"))
            driver.close()
            inter = [(x, int(x.split("index=")[1])) for x in list(set(lol))]


            playlist_name = title



        else:
            inter = [(url, 1)]
            try:
                fireFoxOptions = webdriver.FirefoxOptions()
                fireFoxOptions.headless = True

                driver = webdriver.Firefox(executable_path=r'geckodriver', options=fireFoxOptions)
                driver.get(url)
                time.sleep(3)
                playlist_name = driver.find_elements(by="xpath",value='//*[@id="container"]/h1')[0].text
                print(playlist_name)
            except Exception as e:
                print(f"something went wrong with title grabbing, {str(e)}")
                playlist_name = input("input title now >")


        videos = inter

        if not os.path.exists(playlist_name):
            os.mkdir(f"./{playlist_name}/")
            os.mkdir(f"./{playlist_name}/mp4/")
            os.mkdir(f"./{playlist_name}/mp3/")

        for v, index in videos:
            YoutubeManager.download_video(url=v, index=index, output_folder_name=playlist_name)

        for f in glob.glob(f"./{playlist_name}/mp4/*.mp4"):
            Mp4toMp3Helper.convert(input_file_path=f, ouput_dir_name=playlist_name)

        os.rename(f"./{playlist_name}/mp3", f"./{playlist_name}/{playlist_name}")