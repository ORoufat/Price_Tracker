from bs4 import BeautifulSoup
import requests, lxml

URL = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8"
HEADER = {
    "Accept-Language": "en-GB",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/97.0.4692.99 Safari/537.36",
}

res = requests.get(URL, headers=HEADER)
dump = res.text
soup = BeautifulSoup(dump, "lxml")
mask = soup.find("span", class_="apexPriceToPay")
price = mask.find("span", class_="a-offscreen").getText().strip("$")
print(price)

