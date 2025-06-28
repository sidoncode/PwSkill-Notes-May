import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone"

response = requests.get(url)

if response.status_code == 200:
    soup1 = BeautifulSoup(response.text,'html.parser')
    products = soup1.find_all('div',class_ = 'thumbnail')

    for product in products:
        title_tag = product.find('a', class_='title')
        name = title_tag.text.strip()
        link = "https://webscraper.io" + title_tag.get('href')

        price = product.find('h4', class_='price').text.strip()
        desc = product.find('p', class_='description').text.strip()

        print(f"Name: {name}")
        print(f"Price: {price}")
        print(f"Description: {desc}")
        print(f"Link: {link}")
        print("-" * 50)
else:
    print("Failed to fetch Website")