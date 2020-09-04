import requests
import json

api_requests = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/"
                            "listings/latest?start=1&limit=2&convert=USD&CMC_PRO_API_KEY=2d0daef8-fd08-44e0-8b87"
                            "-20b0f3618c1b")
api = json.loads(api_requests.content)
print(api)
