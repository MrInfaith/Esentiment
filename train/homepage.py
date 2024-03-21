import requests
from bs4 import BeautifulSoup
import pandas as pd
class home:
    def snapdeal(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        r = requests.get(url='https://www.snapdeal.com/', headers=headers)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        divs = soup.find_all('div', {'class': 'trendingProd product-relative dp-widget-link col-xs-5 favDp'})
        links = []
        imgs = []
        for i in divs:
            link = i.find('a', {'class': 'product-card dp-widget-link'})
            links.append(link['href'])
            div_img = link.find('div', {'class': 'product-img'})
            img = div_img.find('img', {'class': 'lazy-load'})
            imgs.append(img['data-src'])
        df=pd.DataFrame({'url':imgs,'link':links})
        return df
#     # def flipkart_deal(self):
# url = "https://www.flipkart.com"
# headers = ({
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46"})
# r = requests.get(url, headers=headers)
# htmlcontent = r.content
# soup = BeautifulSoup(htmlcontent, 'html.parser')
# images = soup.find_all('img', {'class': '_396cs4'})
# img_names=soup.find_all('div',{'class':'_3LU4EM'})
# images_url = []
# names = []
# for image in images:
#     images_url.append(image['src'])
#     names.append(image['alt'].split('(')[0])
# img_url = images_url[10:]
# names = names[10:]
# df=pd.DataFrame({'name':names,'url':img_url})
# print(df)