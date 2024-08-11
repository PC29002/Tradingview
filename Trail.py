"""
//telebot single msg

import telebot

token = "6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI"
bot = telebot.TeleBot(token)

bot.send_message(-1002242173955,"Hello")

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############            
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    

// screen-shot selenium

from selenium import webself.bot
from selenium.webself.bot.chrome.service import Service
from selenium.webself.bot.common.by import By
from selenium.webself.bot.common.keys import Keys
from selenium.webself.bot.support.color import Color
import time

# Set up Chrome options
option = webself.bot.ChromeOptions()
option.add_experimental_option("detach", True)
# option.add_argument("--headless")
# Set up Chrome self.bot
self.bot = webself.bot.Chrome(service=Service('E:\\VS code\\Projects\\Seleium\\Selenium 3 Elements\\chromeself.bot.exe'), options=option)

def screen_short():    

    # Navigate to Google
    self.bot.get("https://www.google.com/")
    time.sleep(2)

    # Perform search operation
    self.bot.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea").send_keys("car")
    time.sleep(3)
    self.bot.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea").send_keys(Keys.RETURN)

    #take screenshot
    import time

    # Get the current time in the format HH-MM-SS
    timestamp = time.strftime('%H - %M - %S')

    # Save the screenshot with the timestamp in the filename
    self.bot.get_screenshot_as_file(f'C:/Users/Admin/Pictures/Screenshots/TradingView Screenshots/Chart-Name_{timestamp}.png')

    # Quit the self.bot
    self.bot.quit()

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############            
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    

// telebot msg using commands

import telebot

# Replace 'YOUR_API_TOKEN' with your actual Telegram bot token
API_TOKEN = '6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI'

bot = telebot.TeleBot(API_TOKEN)

# Handles the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot! How can I assist you?")

# Or you can use long polling if you prefer
#bot.infinity_polling()

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############            
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    

import telebot,MT5,time

class trail():
    
    def __init__(self):
        # Replace 'YOUR_API_TOKEN' with your actual Telegram bot token
        API_TOKEN = '6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI'
        self.bot = telebot.TeleBot(API_TOKEN)
        self.mt = mt.mt5()

    def run(self):
        # Handles the /start command
        @self.bot.message_handler(commands=['profit'])
        def send_welcome(message):

            #profit = self.mt.profit()
            profit = 521
            self.bot.send_message(-1002242173955,profit)
        
        self.bot.polling()
    
       
    def buy_btcusd(self):
        
        symbol = "BTCUSDm"
        buy    = self.mt.symbol_info_tick("BTCUSDm").ask
        sell   = self.mt.symbol_info_tick("BTCUSDm").bid
        
        spread = buy - sell
        print("Spread: ", spread)
        
        tp     =  (buy + 200) + spread
        sl     =  (buy - 132) - spread
        
        print("Take Profit:",buy-tp)
        print("Stop Loss:  ",buy-sl)
    
        request = {
        "action": self.mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 0.01,
        "type": self.mt.ORDER_TYPE_BUY,
        "price": buy,
        "tp": tp,
        "sl": sl,
        "type_time": self.mt.ORDER_TIME_GTC,
        "type_filling": self.mt.ORDER_FILLING_FOK,
        }
    
        self.mt.order_send(request)._asdict()
        for i in request:
            print(i,":",request[i])
    
    def buy_btc_order(self):
        try: 
            self.login()
            self.buy_btcusd()
            
            time.sleep(4)
            self.shutdown()
        except Exception as e:
            print("Check Network or user-details invalid\nMT5 Order Error")
            print(e)    



###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############            
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    


import MetaTrader5 as mt5
import pandas as pd
import os

# Initialize the MetaTrader 5 connection
try:
    mt.initialize()
        
    if not mt.initialize():
        print("initialize() failed, error code =",mt.last_error())
        quit()
        
    Loginn    =  176015435
    Password  =  "Pcgandu@2002"
    Server    =  "Exness-MT5Trial7"
        
    mt.login(Loginn, Password, Server)
except Exception as e:
        print(f"An error occurred: {e}")

def buy_btcusd():
        
        symbol = "BTCUSDm"
        buy    = mt.symbol_info_tick("BTCUSDm").ask #64116
        sell   = mt.symbol_info_tick("BTCUSDm").bid
        
        spread = buy - sell
        print("Spread: ", spread)   
        
        tp     =  buy + 200
        sl     =  buy - 160
        
        print("Take Profit:",buy-tp)
        print("Stop Loss:  ",buy-sl)
    
        request = {
        "action": mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 10,
        "type": mt.ORDER_TYPE_BUY,
        "price": buy,
        "tp": tp,
        "sl": sl,
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_FOK,
        }
    
        mt.order_send(request)._asdict()
        for i in request:
            print(i,":",request[i])
    

def shutdown():
        
        process_name = "terminal64.exe"
        os.system(f"taskkill /f /im {process_name}")


buy_btcusd()

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############            
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    


# https://www.mql5.com/en/docs/python_metatrader5

EurUsd
10 || 6.7

Xness

Login:    116560476 
Name:     PC2902 
Password: fwaijP14# 
Server:   Exness-MT5Trial6 
Balance:  500


FP Markets
Login    : 7043101
Password : fwaijP14#



import MetaTrader5, time

class mt5():
    def __init__(self):
        self.mt = MetaTrader5        
    
    def login(self):
        try:
            self.mt.initialize()
        
            if not self.mt.initialize():
                print("initialize() failed, error code =",self.mt.last_error())
                quit()
        
            Loginn    =  181390836
            Name      =  "Standard" 
            Password  =  "Pcgandu@2002"
            Server    =  "Exness-MT5Trial6"
        
            self.mt.login(Loginn, Password, Server)
        
        except Exception as e:
            print(f"An error occurred: {e}")
        
    def buy_btcusd(self):
        
        symbol = "BTCUSDm"
        buy    = self.mt.symbol_info_tick("BTCUSDm").ask
        sell   = self.mt.symbol_info_tick("BTCUSDm").bid
        
        spread = buy - sell
        print("Spread: ", spread)
        
        tp     =  (buy + 200)
        sl     =  (buy - 132) - spread
        
        print("Take Profit:",buy-tp)
        print("Stop Loss:  ",buy-sl)
    
        request = {
        "action": self.mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume":1.0,
        "type": self.mt.ORDER_TYPE_BUY,
        "price": buy,
        "tp": tp,
        "sl": sl,
        "type_time": self.mt.ORDER_TIME_GTC,
        "type_filling": self.mt.ORDER_FILLING_FOK,
        }
    
        self.mt.order_send(request)
        
        for i in request:
            print(i,":",request[i])
    
    def buy_btc_order(self):
        try: 
            self.login()
            self.buy_btcusd()
            
        except Exception as e:
            print("Check Network or user-details invalid\nMT5 Order Error")
            print(e)    


m = mt5()
m.buy_btc_order()


""" 
class empty():
    
    def color(self):
        
        # EMA + SuperTrend + SuperTrend Cross
        EMA_Trianglehex1     = "#ff0000" #0 #ff0000
        EMA_Trianglehex2     = "#00ff00"
        SuperTrend_Crosshex  = "#ff0000"
        SuperTrendhex        = "#ff0000" #3
        
        # EMA + Macd + RSi Candle
        EMA_Trianglehex3     = "#00ff00" #4 #00ff00
        EMA_Trianglehex4     = "#ff0000"
        MACD_Normalhex       = "#ff0000" #6
        
        self.col_btcusd = [EMA_Trianglehex1, EMA_Trianglehex2, SuperTrend_Crosshex, SuperTrendhex, EMA_Trianglehex3, EMA_Trianglehex4, MACD_Normalhex]
        
    def color_ident_btc(self):
        
        #1 EMA + SuperTrend + SuperTrend Cross
        b = self.col_btcusd
        if (b[0] == b[3] == "#ff0000") or (b[0] == b[3] == "#ff0000"):
            unit = "BTC Green"
            #print(unit)

        elif (b[1] == b[3] == "#00ff00") or (b[1] == b[3] == "#00ff00"):
            unit = "BTC Red"
            #print(unit)

        elif (b[0] == b[2] == "#ff0000") or (b[0] == b[2] == "#ff0000"):
            unit = "BTC Green"
            #print(unit)

        elif (b[1] == b[2] == "#00ff00") or (b[1] == b[2] == "#00ff00"):
            unit = "BTC Red"
            #print(unit)
        
        else:        
            unit = "avoid"
            #print(unit)
        
        #2 EMA + Macd + RSi Candle
        b = self.col_btcusd
        if (b[4] == b[6] == "#ff0000"):
            unit1 = "BTC Green"
            #print(unit1)

        elif (b[4] == b[6] == "#00ff00"):
            unit1 = "BTC Red"
            #print(unit1)
        else:
            unit1 = "avoid"
            #print(unit1)

        
        # ('BTC Green', 'BTC Green') = output: BTC Green
        # ('BTC Red', 'BTC Red')     = output: BTC Red

        # ('avoid', 'avoid')         = output: avoid
        # ('BTC Red', 'BTC Green')   = output: avoid
        # ('BTC Green', 'BTC Red')   = output: avoid
        
        if unit == unit1:
            return unit
        
        elif unit == "BTC Red" and unit1 == "avoid":
            return "BTC Red"
        
        elif unit == "avoid" and unit1 == "BTC Red":
            return "BTC Red"
        
        elif unit == "BTC Green" and unit1 == "avoid":
            return "BTC Green"
        
        elif unit == "avoid" and unit1 == "BTC Green":
            return "BTC Green"
        
        else:
            return "avoid"
                

z = empty()
z.color()
us = [z.color_ident_btc()]

for i in us:
    #print(i)
    if i != "avoid":
        print(i)
        if i == "BTC Green":
                
            print("BTC Green Bought")
                
        elif i == "BTC Red":
                    
            print("BTC Red Bought")
                
        else:
            pass