import requests
import json
import pyttsx3 
import time
class coindesk:
    def __init__(self):
        self.engine = pyttsx3.init()
    def get_btc_price(self):
        try:
            res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            data = json.loads(res.text)
            btc_price = (data['bpi']['USD']['rate'])
            btc_price = int(float(btc_price.replace(",","")))
            self.engine.say("bitcoin price is {}".format(btc_price))
            print("bitcoin price is {}".format(btc_price))
            self.engine.runAndWait()
        except:
            print("ERROR")
bot = coindesk()
while True:
    bot.get_btc_price()
    print("waiting 24 hours....")
    time.sleep(24*60*60)