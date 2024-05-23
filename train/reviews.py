from selenium import webdriver
from selenium.webdriver import chrome 
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
class Extract():
    def review_extract(self,url):
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        driver=webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
        driver.get(url)
        box=driver.find_elements(By.XPATH,'//span[@class="a-size-base review-text"]')
        review=[]
        for i in box:
            review.append(i.text)
        driver.close()
        return review
        


