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

import MT5, schedule, time, tradingview, telebot, os

class TeleMain:
    
    def __init__(self):
        
        self.tr = tradingview.tradingview_main()
        token = "6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI"
        self.bot = telebot.TeleBot(token)
        self.mt = MT5.mt5()
        self.running = False 
    
    def run_crypto(self):
        
        print("\nBot has started")
        us = self.tr.run_crypto()        
                        
        for i in us:
            if i != "avoid":
                self.bot.send_message(-1002242173955,i)
                #self.bot.send_message(5626388450, i)
                print(i)
                    
        #time.sleep(20)
        if 'BTC Green' in us:
                self.mt.buy_btc_order()
            
        elif 'BTC Red' in us:
                self.mt.sell_btc_order()
                    
        else:
            pass
        
    def temp(self):
        
        self.bot.send_message(-1002242173955," END OF TEST RUN")
    
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
    
    def schedule_bot_crypto(self):
        
        try:
    
            self.teleschedule.run_crypto()
            self.teleschedule.stop()
    
        except Exception as e:
        
            print(f"An error occurred: {e}")
            telebot.TeleBot("6769710324:AAEzopLaKNaWvxQ31Uk5UtAQG4f4v4ImfhI").send_message(5626388450,e)
            self.teleschedule.stop()
    
    def schedule_crypto(self):
        
        for hour in range(24):
            for minute in [4, 34]:
        
                time_str = f"{hour:02d}:{minute:02d}"
                schedule.every().monday.at(time_str).do(self.schedule_bot_crypto)
                schedule.every().tuesday.at(time_str).do(self.schedule_bot_crypto)
                schedule.every().wednesday.at(time_str).do(self.schedule_bot_crypto)
                schedule.every().thursday.at(time_str).do(self.schedule_bot_crypto)
                schedule.every().friday.at(time_str).do(self.schedule_bot_crypto)
                schedule.every().saturday.at(time_str).do(self.schedule_bot_crypto)
                schedule.every().sunday.at(time_str).do(self.schedule_bot_crypto)
    
    def run(self):
        
        print(time.ctime(time.time()))
        self.schedule_crypto()  
        
        while True:
            schedule.run_pending()
            time.sleep(1)

class tele_main_commands:
    
    def __init__(self):
        self.teleschedule = TeleMain()
    
    def command_info(self):
        
        @self.teleschedule.bot.message_handler(commands=['help'])
        def send_help(message):
            help_messages = [
                'pro -> Receives Total Profit Amount',
                'gord -> Gets Current no of Orders',
                'cord -> Close all Opened Positions'
            ]
            for i in help_messages:
                #self.teleschedule.bot.send_message(5626388450, i) 
                self.teleschedule.bot.send_message(-1002242173955, i)
                print(i)
    
    def check_profit(self):
        @self.teleschedule.bot.message_handler(commands=['pro'])
        def send_profit(message):
            
            profit = self.teleschedule.mt.profit()
            self.teleschedule.bot.send_message(-1002242173955, profit)
            #self.teleschedule.bot.send_message(5626388450, profit)
            
            self.teleschedule.mt.shutdown()

    def get_total_order(self):
        
        @self.teleschedule.bot.message_handler(commands=['gord'])
        def send_order(message):
            
            order = self.teleschedule.mt.total_order()
            self.teleschedule.bot.send_message(-1002242173955, order)
            #self.teleschedule.bot.send_message(5626388450, order)          
            
            self.teleschedule.mt.shutdown()
    
    def close_positions(self):
        @self.teleschedule.bot.message_handler(commands=['cord'])
        def send_positions(message):
            
            position = self.teleschedule.mt.close_positions()
            self.teleschedule.bot.send_message(-1002242173955, position)
            #self.teleschedule.bot.send_message(5626388450, position)          
            
            self.teleschedule.mt.shutdown()
    
    def stop_script(self):
        @self.teleschedule.bot.message_handler(commands=['sspr'])
        def stop_script(message):
            
            #self.teleschedule.bot.send_message(-1002242173955,"Stopping the script")
            self.teleschedule.bot.send_message(5626388450, "Stopping the script")          
            print("Stopping the script")
            os._exit(0)
            
    
    def start_run(self):
        
        try:
            
            self.command_info()
            self.check_profit() 
            self.get_total_order()
            self.close_positions()
            self.stop_script()
            
        
        except Exception as e:
            
            print(f"The Error: {e}")

        self.teleschedule.bot.infinity_polling()    
    
###############################     ###############################     ###############################     ###############################     ###############################     ###############################
###############################     ###############################     ###############################     ###############################     ###############################     ###############################
###############################     ###############################     ###############################     ###############################     ###############################     ###############################

#TeleMain().temp()
#TeleMain().run_us()
#TeleMain().run_crypto()

"""import threading

def run():
    a = TeleMain_schedule()
    b = tele_main_commands()

    thread_a = threading.Thread(target=a.run)
    thread_b = threading.Thread(target=b.start_run)

    thread_a.start()
    thread_b.start()

    try:
        thread_a.join()
        thread_b.join()
    
    except Exception as e:
        print(f"Error joining threads: {e}")"""
        
#TeleMain().run_crypto()





