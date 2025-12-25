import requests
from bs4 import BeautifulSoup
import lxml

def get_flipkart_price(url):
    # Product URL
    # URL = "https://www.flipkart.com/lakm-9-5-cc-cream-foundation/p/itm49820099a5c31?pid=FNDEVYMY53JCQZU7&lid=LSTFNDEVYMY53JCQZU73AGDJF&marketplace=FLIPKART&q=lakme+cc+cream&store=g9b%2Fffi%2Fdzu%2Fgru&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=en_p8fwq7LGC_hXFVOUEAHtn7t94D-aBKe4LfF414Sh2jZJLjTHG6PmJQvpSNairdZisusPsbUaj4pICrLB1PErWfUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=sp&ppn=sp&ssid=u4r4pev7q80000001761839230506&qH=d8510c80ed04316a"

    # headers
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en;q=0.9"
    }

    # Send request
    response = requests.get(url, headers=headers)

    # Parse HTML
    soup = BeautifulSoup(response.text, "lxml")

    # Extract product price
    price = soup.find("div", class_="Nx9bqj")
    if price:
        price = price.get_text(strip=True)
    else:
        price = "Price not found"

    return price

# print("Product Title:", title)
# print("Price:", price)
