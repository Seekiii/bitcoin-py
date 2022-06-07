import requests
import json

currency = "EUR" # USD / EUR / BAM

req = requests.get(f"https://www.coinbase.com/api/v2/assets/prices/bitcoin?base={currency}").json()

price = "{:.2f}".format(float(req['data']['prices']['latest_price']['amount']['amount']))

print(f"BitCoin price: {price} [{currency}]")