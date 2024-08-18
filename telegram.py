# url   : https://core.telegram.org/bots/api
# id    : -1002242173955
# token : 6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI
# Steps : botfather > /start /mybots

"""
//for chat_it :::

import telebot
import tradingview
import time
import MT5

class TeleMain:
    def __init__(self):
        self.tr = tradingview.tradingview_main()
        token = "6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI"
        self.bot = telebot.TeleBot(token)
        self.mt = MT5.mt5()
        self.start_uscap()

    def get_chat_id(self):
        @self.bot.message_handler(func=lambda message: True)
        def handle_all_messages(message):
            # Print chat ID
            chat_id = message.chat.id
            print("Chat ID:", chat_id)
            
            # Print message ID
            print("Message ID:", message.message_id)
            
            # You can add your message handling logic here
            # For example, send a response to the user
            self.bot.reply_to(message, "Received your message.")
        
        self.bot.polling()

a = TeleMain()

// id of a particular channel
 @username_to_id_bot
"""

########################

import MT5, schedule, time, tradingview, telebot 
from datetime import datetime, timedelta


class TeleMain:
    
    def __init__(self):
        
        self.tr = tradingview.tradingview_main()
        token = "6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI"
        self.bot = telebot.TeleBot(token)
        self.mt = MT5.mt5()
        self.running = False
    
    def ist_to_utc(self):
        # Get the current IST time
        ist_time_str = datetime.now().strftime('%H:%M:%S')
    
        # Define the IST time zone offset (+5:30 hours from UTC)
        ist_offset = timedelta(hours=5, minutes=30)

        # Parse the input string to a datetime object
        ist_time = datetime.strptime(ist_time_str, '%H:%M:%S')

        # Subtract the IST offset to get UTC time
        utc_time = ist_time - ist_offset

        # Format the UTC time as a string
        utc_time_str = utc_time.strftime('%H:%M:%S')

        # Return the UTC time as a formatted string
        return f"IST Time: {ist_time_str} -> UTC Time: {utc_time_str}"
    
    
    def run_us(self):
        
        print("\nBot has started")
        us = self.tr.run_uscap()
        timeinfo = self.ist_to_utc()
        
        if not 'avoid' in us:
            self.bot.send_message(-1002242173955,us)
            self.bot.send_message(-1002242173955,timeinfo)
            print(us, timeinfo)
            
        time.sleep(40)
        if 'BTC Green' in us:
                self.mt.buy_btc_order()
                #print("self.bot.send_message(-1002242173955,us)")
            
        elif 'BTC Red' in us:
                self.mt.sell_btc_order()
                #print("self.bot.send_message(-1002242173955,us)")
                    
        else:
            print("Avoid")
        
    def temp(self):
        
        self.bot.send_message(-1002242173955," BTC Red")
    
    def start(self):
        
        self.running = True
        
        try:
        
            self.bot.infinity_polling()
        
        except Exception as e:
            
            print(f"An error occurred: {e}")

    def stop(self):
        
        time.sleep(5)
        
        print("\nStopping the bot...\n")
        
        self.running = False
        self.bot.stop_polling()
        
        time.sleep(20)
    
    def get_chat_id(self):
        
        @self.bot.message_handler(func=lambda message: True)
        def handle_all_messages(message):
            # Print chat ID
            chat_id = message.chat.id
            print("Chat ID:", chat_id)
            
            # Print message ID
            print("Message ID:", message.message_id)
            self.bot.reply_to(message, "Received your message.")
        
        self.bot.polling()
    


class TeleMain_schedule():
    
    def __init__(self):
        
        self.teleschedule = TeleMain()
    
    def schedule_bot_us(self):
        
        try:
    
            self.teleschedule.run_us()
            self.teleschedule.stop()
    
        except Exception as e:
        
            print(f"An error occurred: {e}")
            #telebot.TeleBot("6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI").send_message(-1002242173955,e)
            self.teleschedule.stop()
    
    # Scheduling for 12:00 AM to 11:30 PM, Monday to Friday
    def schedule_us(self):
    
        for hour in range(24):  # from 00:00 to 23:00
    
            for minute in [4, 34]:  # every 30 minutes
            
                time_str = f"{hour:02d}:{minute:02d}"
            
                # Scheduling tasks
            
                schedule.every().monday.at(time_str).do(self.schedule_bot_us)

                schedule.every().tuesday.at(time_str).do(self.schedule_bot_us)
            
                schedule.every().wednesday.at(time_str).do(self.schedule_bot_us)
            
                schedule.every().thursday.at(time_str).do(self.schedule_bot_us)
            
                schedule.every().friday.at(time_str).do(self.schedule_bot_us)
                
                schedule.every().saturday.at(time_str).do(self.schedule_bot_us)
                
                schedule.every().sunday.at(time_str).do(self.schedule_bot_us)
    
    def run(self):
        
        print(time.ctime(time.time()))
        self.schedule_us()
        
        while True:
            
            schedule.run_pending()
            time.sleep(1)


class tele_main_commands():
    
    def __init__(self):
        
        self.teleschedule = TeleMain()
    
    def check_profit(self):
        @self.teleschedule.bot.message_handler(commands=['profit'])
        def send_profit(message):
            profit = self.teleschedule.mt.profit()
            self.teleschedule.bot.send_message(-1002242173955, profit)
            #self.bot.send_message(-1002242173955, profit)   
            
            self.teleschedule.mt.shutdown()

    def get_total_order(self):
        
        @self.teleschedule.bot.message_handler(commands=['gorder'])
        def send_order(message):
            order = self.teleschedule.mt.total_order()
            self.teleschedule.bot.send_message(-1002242173955, order)
            #self.bot.send_message(-1002242173955, order)          
            
            self.teleschedule.mt.shutdown()
    
    def command_info(self):
        
        @self.teleschedule.bot.message_handler(commands=['help'])
        def send_help(message):
            
            help = ['profit -> Receives Total Profit Amount', 'gorder -> Gets Current no of Orders']
            for i in help:
                self.teleschedule.bot.send_message(-1002242173955,i)
                print(i)
    
    def start_run(self):
        
        try:
            
            self.check_profit() 
            self.get_total_order()
        
        except Exception as e:
            
            print(f"The Error: {e}")

        self.teleschedule.bot.infinity_polling()    
    
###############################     ###############################     ###############################     ###############################     ###############################     ###############################
###############################     ###############################     ###############################     ###############################     ###############################     ###############################
###############################     ###############################     ###############################     ###############################     ###############################     ###############################

#TeleMain().temp()
#TeleMain().run_us()

import threading 

a = TeleMain_schedule()
b = tele_main_commands()

thread_a = threading.Thread(target= a.run)
thread_b = threading.Thread(target= b.start_run)

thread_a.start()
thread_b.start()

thread_a.join()
thread_b.join()















    


    
    



    




