from selenium import webdriver
from selenium.webdriver import chrome 
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
class Search():
    def amazon_product(self,product_name):
        if product_name!="":
            options=webdriver.ChromeOptions()
            options.add_experimental_option("detach",True)
            driver=webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
            driver.get('https://www.amazon.in/')
            box=driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
            box.send_keys(product_name)
            box.send_keys(Keys.ENTER)
            url=[]
            images=[]
            # link to go to page
            box=driver.find_elements(By.XPATH,"//a[@class='a-link-normal s-no-outline']")
            for i in box:
                link=i.get_attribute('href')
                url.append(link)
            # link of product images
            img=driver.find_elements(By.XPATH,"//img[@class='s-image']")
            for i in img:
                images.append(i.get_attribute('src'))
            # prices of the product
            prices=[]
            price=driver.find_elements(By.XPATH,"//span[@class='a-price-whole']")
            for i in price:
                prices.append(i.text)
            images=images[0:6]
            url=url[0:6]
            prices=prices[3:9]
            #name of the product
            names=[]
            name=driver.find_elements(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
            for i in name:
                names.append(i.text)
            names=names[0:6]
            df=pd.DataFrame({'name': names ,'price':prices,'page':url,'img':images})
            driver.close()
            return df
 
                




