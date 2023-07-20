import os
from dotenv import load_dotenv
load_dotenv

PROXY = os.getenv("PROXY")
proxies = {
    "http": PROXY,
    "https": PROXY
}
import requests
from bs4 import BeautifulSoup

# create function to start scrape the quotes from the websites: 
def scrape_quotes(url):
    r = requests.get(url, proxies=proxies)
    soup = BeautifulSoup(r.text, features="html.parser")
    quotes_container = soup.find("div", class_ = "quotes")
    quotes = quotes_container.find_all("div",class_="quoteText")


if __name__ == "__main__":
    url = ""
    res = scrape_quotes(url)
    print(res)