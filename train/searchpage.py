import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
class sadearch:
    def amazon_product_name(self,search_text=""):
        if search_text != "":
            url = f"https://www.techbargains.com/search?search={search_text}"
            headers = ({
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46"})
            r = requests.get(url, headers=headers)
            htmlcontent = r.content
            soup = BeautifulSoup(htmlcontent, 'html.parser')
            divs = soup.find_all('div', {'class': 'col-sm-4 text-center text-sm-left my-2 my-sm-0 pb-2'})
            names = []
            prices = []
            url = []
            img_url = []
            for it in divs:
                img = it.find('img', {'class': 'img-fluid'})
                img_url.append(img['src'])
                names.append(img['alt'])
                page_link = it.find('a')
                url.append(page_link['href'])
                text = img['alt']
                price_pattern = r'\$(\d+(\.\d{1,2})?)'
                match = re.search(price_pattern, text)
                if match:
                    price = match.group(0)
                    prices.append(price)
                else:
                    text = img['alt']
                    percentage_pattern = r'Up to (\d+)%'
                    match = re.search(percentage_pattern, text)
                    if match:
                        percentage = match.group(0)
                        prices.append(percentage)
        mini=min({len(names),len(prices),len(img_url),len(url)})
        df = pd.DataFrame({'name': names[0:mini], 'prices': prices[0:mini], 'url': img_url[0:mini], 'page_link': url[0:mini]})
        return df
# # def flipkart_product_name(self,search_text):
# search_text='laptop'
# if search_text != '':
#     url = f"https://www.flipkart.com/search?q={search_text}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
#     headers = ({
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46"})
#     r = requests.get(url, headers=headers)
#     htmlcontent = r.content
#     soup = BeautifulSoup(htmlcontent, 'html.parser')
#     # if search_text=='camera' or search_text=='laptops':
#     name = []
#     prices = []
#     img_url = []
#     links = []
#     link = soup.find_all('a', {'class': '_1fQZEK'})
#     for i in link:
#         links.append('https://www.flipkart.com' + i['href'])
#         x = i.find('div', {'class': 'CXW8mj'})
#         p = x.find('img', {'class': '_396cs4'})
#         price = i.find('div', {'class': '_30jeq3 _1_WHN1'})
#         name.append(p['alt'])
#         img_url.append(p['src'])
#         prices.append(price.text)
#     df = pd.DataFrame({'name': name, 'prices': prices, 'url': img_url, 'page_link': links})
# print(df)
