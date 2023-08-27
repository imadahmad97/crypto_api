import requests
from bs4 import BeautifulSoup as bs

btc_url = 'https://www.coindesk.com/price/bitcoin/'
eth_url = 'https://www.coindesk.com/price/ethereum/'
doge_url = 'https://www.coindesk.com/price/dogecoin/'
lts_url = 'https://www.coindesk.com/price/dogecoin/'


r = requests.get(url)

soup = bs(r.content, "html.parser")

price = soup.find("span", {"class":"currency-pricestyles__Price-sc-1rux8hj-0 eEpEzP"})

print(price.text)