import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys
import progress

link__ = sys.argv[1]


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="chromedriver",options=chrome_options)
link_list=[] 
ep_list =["01","02"]
class PageTwo:
    def page1(self):
        driver.get(link__)
        time.sleep(3)
        main_div = driver.find_elements(By.TAG_NAME ,"a")
        ep_num = driver.find_elements(By.CLASS_NAME,"sea")
        for num in ep_num:
            ep_list.append(num)
        title=  driver.find_elements(By.CLASS_NAME,"sea")
        if len(main_div) > 0:
            for i in range(2, len(main_div)-1):
                link = main_div[i].get_attribute("href")
                link_list.append(link)
            PageTwo().page2()
    def page2(self):
        with open("file.txt","w") as file:
            file.write("")
        for link in link_list:
            try: 
                driver.get(link)
                time.sleep(3)
                link2 =driver.find_element(By.TAG_NAME, "iframe").get_attribute("src")
                if link2 == "blank:blank":
                    time.sleep(3)
                    link2 =driver.find_element(By.TAG_NAME, "iframe").get_attribute("src")   
                driver.get(link2)
                time.sleep(3)
                link3 = driver.find_element(By.ID, "prime").click()
                time.sleep(3)
                link4 = driver.find_element(By.TAG_NAME, "video").get_attribute("src")
                with open("file.txt","a") as file:
                    file.write(f"{link4} \n")
            except Exception as e:
                print(e)
                print("something huge is wrong")
        PageTwo.page3()

    def page3(self):
        chunk_size = 500
        with open("file.txt" ,"r") as file:
            ll = file.readlines()
            i =0;
            for url in ll:
                r = requests.get(url,stream=True)
                with open(f"ep{ep_list[i]}.mp4","wb") as file:
                    for  chunk in r.iter_content(chunk_size=chunk_size):
                        file.write(chunk)
                i=i+1
PageTwo().page3()