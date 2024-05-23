import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from train.rotateproxy import available
proxy=available()
search_text=input('enter the search_text')

if search_text != '':
    url = f"https://www.flipkart.com/search?q={search_text}&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=4e707e80-1029-4f53-b7e5-ea150af1b751"

    headers = ({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46"})
    for i in proxy:
       html_content = scrape_with_proxy(url, i)
       if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        name = []
        prices = []
        img_url = []
        links = []
        link = soup.find_all('a', {'class': '_1fQZEK'})
        for i in link:
            links.append('https://www.flipkart.com' + i['href'])
            x = i.find('div', {'class': 'CXW8mj'})
            p = x.find('img', {'class': '_396cs4'})
            price = i.find('div', {'class': '_30jeq3 _1_WHN1'})
            name.append(p['alt'])
            img_url.append(p['src'])
            prices.append(price.text)
        df = pd.DataFrame({'name': name, 'prices': prices, 'url': img_url, 'page_link': links})
        if df.empty()==True:
           continue
        else:
            break
print(df)
def scrape_with_proxy(url, proxy):
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy})
        if response.status_code == 200:
            return response.content
        else:
            print("Failed to fetch URL:", url)
            return None
    except Exception as e:
        print("Error:", e)
        return None

        
