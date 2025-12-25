import requests
from bs4 import BeautifulSoup

def get_amazon_price(url):
    # Amazon URL
    # URL = "https://amzn.in/d/hGD2kHi"

    #headers to make the request look like it's from a real browser(just found out this is imp)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }

    # Send request to Amazon
    response = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "lxml")

    # # Extract product title
    # title = soup.find("span", attrs={"id": "productTitle"})
    # if title:
    #     title = title.get_text(strip=True)
    # else:
    #     title = "Title not found"

    # Extract product price
    price = soup.find("span", attrs={"class": "a-price-whole"})
    if not price:  # fallback (some products use different class)
        price = soup.find("span", attrs={"class": "a-offscreen"})
    if price:
        price = price.get_text(strip=True)
    else:
        price = "Price not found"

    return price
# print("Product Title:", title)
# print("Price:", price)
