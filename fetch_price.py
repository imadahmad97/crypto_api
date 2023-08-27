import requests
from bs4 import BeautifulSoup as bs

def get_crypto_prices():
    btc_url = 'https://www.coindesk.com/price/bitcoin/'
    eth_url = 'https://www.coindesk.com/price/ethereum/'
    doge_url = 'https://www.coindesk.com/price/dogecoin/'
    ltc_url = 'https://www.coindesk.com/price/litecoin/'

    btc_req = requests.get(btc_url)
    eth_req = requests.get(eth_url)
    doge_req = requests.get(doge_url)
    ltc_req = requests.get(ltc_url)

    btc_soup = bs(btc_req.content, "html.parser")
    eth_soup = bs(eth_req.content, "html.parser")
    doge_soup = bs(doge_req.content, "html.parser")
    ltc_soup = bs(ltc_req.content, "html.parser")

    btc_price = btc_soup.find("span", {"class": "currency-pricestyles__Price-sc-1rux8hj-0 eEpEzP"}).text
    eth_price = eth_soup.find("span", {"class": "currency-pricestyles__Price-sc-1rux8hj-0 eEpEzP"}).text
    doge_price = doge_soup.find("span", {"class": "currency-pricestyles__Price-sc-1rux8hj-0 jxzQXk"}).text
    ltc_price = ltc_soup.find("span", {"class": "currency-pricestyles__Price-sc-1rux8hj-0 eEpEzP"}).text

    return {
        "BTC": btc_price,
        "ETH": eth_price,
        "DOGE": doge_price,
        "LTC": ltc_price
    }
