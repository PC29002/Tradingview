"""
# https://www.mql5.com/en/docs/python_metatrader5

EurUsd -> 
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


"""
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
import MetaTrader5, time, os
import pandas as pd

class mt5():
    def __init__(self):
        self.mt = MetaTrader5        
    
    def login(self):
        
        try:
            if not self.mt.initialize():
                print("initialize() failed, error code =", self.mt.last_error())
                quit()

            login_id = 181390836
            password = "Pcgandu@2002"
            server = "Exness-MT5Trial6"

            if self.mt.login(login_id, password, server):
                print("Logged in successfully")
            else:
                print("Login failed, error code =", self.mt.last_error())
                self.mt.shutdown()

        except Exception as e:
            print(f"An error occurred: {e}")

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############            
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        

    def acc_info(self):
       
        self.login()
        
        print("terminal info:",self.mt.terminal_info())
        print("account info :",self.mt.account_info())
        print("terminal info:",self.mt.terminal_info())
        print("Total Symbol",self.mt.symbols_total())

        self.mt.shutdown()    

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############                

    def profit(self):
        
        self.login()
        
        try:    
        
            account_info = self.mt.account_info()  
            balance = account_info.balance 
            profit = account_info.profit  
            
            print(f"Balance: {balance}\nProfit: {profit}")                
            
            self.mt.shutdown()
            return f"Balance: {balance}\nProfit: {profit}"
        
        
        except Exception as e:
            print(f"An error occurred: {e}")

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
    
    def total_order(self):
        
        try: 
            self.login()
        
            orders = self.mt.orders_total()
            if orders>0:
                print("Total orders=",orders)
                return orders
            
            else:
                print("Orders not found")
                return orders

        except Exception as e:
            
            print(f"An Error occured {e}")
            self.shutdown()


###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############                

    def swing_high_low(self):
        
        # Specify the symbol and timeframe
        symbol = "BTCUSDm"
        timeframe = self.mt.TIMEFRAME_M30  # 30-Min timeframe

        # Retrieve historical data
        rates = self.mt.copy_rates_from_pos(symbol, timeframe, 0, 1000)  # 1000 most recent candles

        # Convert to DataFrame for easier manipulation
        data = pd.DataFrame(rates)

        # Convert 'time' to datetime if the column exists
        if 'time' in data.columns:
            data['time'] = pd.to_datetime(data['time'], unit='s')
        else:
            raise KeyError("The 'time' column is missing in the data")

        # Define swing high and low detection function
        def find_swings(data, lookback=5):
            data['swing_high'] = data['high'][(data['high'] > data['high'].shift(1)) &
                                              (data['high'] > data['high'].shift(-1)) &
                                              (data['high'] > data['high'].shift(2)) &
                                              (data['high'] > data['high'].shift(-2))]
            data['swing_low'] = data['low'][(data['low'] < data['low'].shift(1)) &
                                            (data['low'] < data['low'].shift(-1)) &
                                            (data['low'] < data['low'].shift(2)) &
                                            (data['low'] < data['low'].shift(-2))]
            return data

        # Apply swing detection
        swings = find_swings(data)

        # Find the most recent swing high and low
        most_recent_swing_high = swings.dropna(subset=['swing_high']).iloc[-1]
        most_recent_swing_low = swings.dropna(subset=['swing_low']).iloc[-1]

        # Display results
        print("Swing High: ", most_recent_swing_high['swing_high'])
        print("Swing Low:  ", most_recent_swing_low['swing_low'])
        
        self.high = most_recent_swing_high['swing_high']
        self.low  = most_recent_swing_low['swing_low']

    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
    
    def buy_btcusd(self):
        
        symbol = "BTCUSDm"
        buy    = self.mt.symbol_info_tick(symbol).ask
        sell   = self.mt.symbol_info_tick(symbol).bid
        
        spread = buy - sell
        print("Spread: ", spread)
        
        tp = (buy + 200) + spread
        sl = (buy - 160) - spread

        request = {
            'action': self.mt.TRADE_ACTION_DEAL,
            'symbol': symbol,
            'volume': 4.0,
            'price': buy,
            'tp': tp,
            'sl': sl,
            'type': self.mt.ORDER_TYPE_BUY,
            'type_time'   : self.mt.ORDER_TIME_GTC,
            'type_filling': self.mt.ORDER_FILLING_IOC,
            'comment'     : 'Buy Order placed'
        }

        response = self.mt.order_send(request)
        
        if response is None:
            print("Order send failed, response is None")
        
        else:
            response_dict = response._asdict()
            for key, value in response_dict.items():
                print(f"{key}: {value}")
    
        # Optionally return the request details
        # return request["symbol"], request["price"], request["tp"], request["sl"]
    
    def buy_btc_order(self):
        
        try: 
            
            self.login()
            print = self.buy_btcusd()
            
            
            time.sleep(2)
            self.shutdown()
            #return (f"Symbol: {print[0]}, Price: {print[1]}, Take Profit: {print[2]}, Stop Loss: {print[3]}")
        
        except Exception as e:
            print("Check Network or user-details invalid\nMT5 Order Error")
            print(e)    
            self.shutdown()

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        

    def sell_btcusd(self):
        
        #self.swing_high_low()
        
        symbol = "BTCUSDm"
        buy    = self.mt.symbol_info_tick("BTCUSDm").ask
        sell   = self.mt.symbol_info_tick("BTCUSDm").bid
        
        spread = buy - sell
        print("Spread: ", spread)
        
        tp = (sell - 200) - spread
        sl = (sell + 160) + spread
        
        request = {
        "action": self.mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 4.0,
        "type": self.mt.ORDER_TYPE_SELL,
        "price": sell,
        "tp": tp,
        "sl": sl,
        "type_time": self.mt.ORDER_TIME_GTC,
        "type_filling": self.mt.ORDER_FILLING_FOK,
        }
    
        self.mt.order_send(request)._asdict()
        for i in request:
            print(i,":",request[i])
    
    def sell_btc_order(self):
        
        try: 
            self.login()
            time.sleep(2)
            self.sell_btcusd()
            
            time.sleep(4)
            self.shutdown()
        
        except Exception as e:
            print("Check Network or user-details invalid\nMT5 Order Error")
            print(e)
            self.shutdown()

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        

    def buy_xausd(self):
        
        #self.swing_high_low()
        
        symbol = "XAUUSDm"
        buy    = self.mt.symbol_info_tick(symbol).ask
        sell   = self.mt.symbol_info_tick(symbol).bid
        
        spread = buy - sell
        print("Spread: ", spread)
        
        tp = buy + 3
        sl = buy - 1.8  
        
        request = {
        "action": self.mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 0.4,
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
    
    def buy_xau_order(self):
        
        try: 
            self.login()
            time.sleep(2)
            self.sell_btcusd()
            
            time.sleep(4)
            self.shutdown()
        
        except Exception as e:
            print("Check Network or user-details invalid\nMT5 Order Error")
            print(e)
            self.shutdown()
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        


    def sell_xausd(self):
        
        #self.swing_high_low()
        
        symbol = "XAUUSDm"
        buy    = self.mt.symbol_info_tick(symbol).ask
        sell   = self.mt.symbol_info_tick(symbol).bid
        
        spread = buy - sell
        print("Spread: ", spread)
        
        tp = sell - 3
        sl = sell + 1.8  
        
        request = {
        "action": self.mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": 0.4,
        "type": self.mt.ORDER_TYPE_SELL,
        "price": sell,
        "tp": tp,
        "sl": sl,
        "type_time": self.mt.ORDER_TIME_GTC,
        "type_filling": self.mt.ORDER_FILLING_FOK,
        }
    
        self.mt.order_send(request)._asdict()
        for i in request:
            print(i,":",request[i])
    
    def sell_xau_order(self):
        
        try: 
            self.login()
            time.sleep(2)
            self.sell_btcusd()
            
            time.sleep(4)
            self.shutdown()
        
        except Exception as e:
            print("Check Network or user-details invalid\nMT5 Order Error")
            print(e)
            self.shutdown()
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        

    def shutdown(self):
        
        process_name = "terminal64.exe"
        os.system(f"taskkill /f /im {process_name}")

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
    

#mt5().buy_btc_order()
mt5().sell_btc_order()