import os
from binance.enums import *

#initialization
#api_key = os.environ.get('API_KEY')
#api_secret = os.environ.get('SECRET_KEY')

testnet_key = os.environ.get('HMAC_KEY')
testnet_secret = os.environ.get('HMAC_SECRET')

client = Client(testnet_key, testnet_secret)