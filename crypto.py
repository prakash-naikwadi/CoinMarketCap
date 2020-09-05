import requests
import json


def crypto_info():
    api_requests = requests.get(
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=2000&convert=USD"
        "&CMC_PRO_API_KEY "
        "=2d0daef8-fd08-44e0-8b87-20b0f3618c1b")
    api = json.loads(api_requests.content)

    # Creating portfolio

    # requires name of coin , price , no of coins i have bought

    print("--------------------------------------------------------")
    print("--------------------------------------------------------")

    # XRP = Ripple

    coins = [
        {
            "symbol": "BTC",
            "amount_bought": 2,
            "price_per_coin": 3200
        },
        {
            "symbol": "ETH",
            "amount_bought": 100,
            "price_per_coin": 100
        },
        {
            "symbol": "XRP",
            "amount_bought": 10,
            "price_per_coin": 100
        },
        {
            "symbol": "EOS",
            "amount_bought": 15,
            "price_per_coin": 100
        },
        {
            "symbol": "QCX",
            "amount_bought": 150,
            "price_per_coin": 100
        }
    ]

    total = 0
    temp = {}
    for i in range(0, 1000):
        if coins[-1] == temp:
            break
        for coin in coins:
            if api["data"][i]["symbol"] == coin["symbol"]:
                total_paid = coin["price_per_coin"] * coin["amount_bought"]
                current_value = coin["amount_bought"] * api["data"][i]["quote"]["USD"]["price"]
                p_l_per_coin = api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                p_l_total = p_l_per_coin * coin["amount_bought"]
                total = total + p_l_total

                print(api["data"][i]["name"] + "--" + api["data"][i]["symbol"])
                print("Price - {0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
                print("Number Of Coins Owned - ", coin["amount_bought"])
                print("Total Paid Price - ", total_paid)
                print("Current Value - ", "{0:.2f}".format(current_value))
                print("P/L per coin - ", "{0:.2f}".format(p_l_per_coin))
                print("P/L Total - ", "{0:.2f}".format(p_l_total))

                print("--------------------------------------------------------")
                temp = coin

    print("Total - ", "{0:.2f}".format(total))
