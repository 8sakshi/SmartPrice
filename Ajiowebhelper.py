import requests
from bs4 import BeautifulSoup

url = "https://www.ajio.com/nike-women-court-royal-2-nn-lace-up-sneakers/p/469038217_white?user=old&"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/117.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Product
title = soup.find("title")
product_name = title .get_text(strip=True)\
    if title  \
    else "Not found"

# Price
price = soup.find("div", class_="prod-sp")
price = price.get_text(strip=True) \
    if price\
    else "Not found"

print("Product Name :", product_name)
print("Price:", price)
