import requests 
from bs4 import BeautifulSoup


# Step 1: Send a GET request to the website
url = "http://quotes.toscrape.com"
response = requests.get(url)

# Step 2: Parse the HTML with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find all quotes and authors
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

# Step 4: Display the scraped data
for quote, author in zip(quotes, authors):
    print(f"{quote.text} — {author.text}")
    