import os
from binance.client import Client
# - Create a tkinter UI
# - Allow user input
# - Binance is so weirdly confusing when buying and selling crypto so I am trying to change that
api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('SECRET_KEY')
#testing interaction with the exchange
client = Client(api_key, api_secret, testnet=True)
client.API_URL = 'https://testnet.binance.vision/api'

#validate buy but don't send to exchange
def buy():
    #amount = input("type the quantity you would like to buy: ")
    #coin = int(input("type the coin symbol: "))

    order = client.create_test_order(
        symbol='BNBBTC',
        side=Client.SIDE_BUY,
        type=Client.ORDER_TYPE_MARKET,
        quantity=100)

def sell():
    pass
