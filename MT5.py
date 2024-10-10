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

        """"""login_id = 146825254
            password = "Pcgandu@2002"
            server = "Exness-MT5Real17"""""""
            
        

"""
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
import MetaTrader5, time, os, tradingview
import pandas as pd
from datetime import datetime

class mt5():
    def __init__(self):
        self.mt = MetaTrader5   
        self.td = tradingview.tradingview_main()     
    
    def login(self):
        
        try:
            if not self.mt.initialize():
                print("initialize() failed, error code =", self.mt.last_error())
                quit()

            
            login_id = 176632309
            password = "fwaijP14#"
            server   = "Exness-MT5Trial7"
            
            if self.mt.login(login_id, password, server):
                print("Logged in successfully")
            else:
                print("Login failed, error code =", self.mt.last_error())
                self.mt.shutdown()

        except Exception as e:
            print(f"An error occurred: {e}")

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############            
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        



###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############            
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        

    def acc_info(self):
       
        self.login()
        
        print("terminal info:",self.mt.terminal_info())
        print("account info :",self.mt.account_info())
        print("terminal info:",self.mt.terminal_info())
        print("Total Symbol",self.mt.symbols_total())

        self.shutdown()  

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############                

    def profit(self):
        
        self.login()
        
        try:    
        
            account_info = self.mt.account_info()  
            balance = account_info.balance 
            profit = account_info.profit  
            
            print(f"Balance: {balance}\nProfit: {profit}")                
            
            self.mt.shutdown()
            self.shutdown()
            return f"Balance: {balance}\nProfit: {profit}"
        
        
        except Exception as e:
            print(f"An error occurred: {e}")
            self.shutdown()

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        

    def close_positions(self):
        try:
            self.login()
            time.sleep(2)
            open_positions = self.mt.positions_get()

            # Check if there are any open positions
            if open_positions is None or len(open_positions) == 0:
                print("No open positions to close, error code =", self.mt.last_error())
            else:
                # Loop through all open positions and close them
                for position in open_positions:
                    # Define the trade request to close the position
                    request = {
                        "action": self.mt.TRADE_ACTION_DEAL,
                        "symbol": position.symbol,
                        "volume": position.volume,
                        "position": position.ticket,
                        "type": self.mt.ORDER_TYPE_SELL if position.type == self.mt.POSITION_TYPE_BUY else self.mt.ORDER_TYPE_BUY,  # Opposite type to close
                        "price": self.mt.symbol_info_tick(position.symbol).bid if position.type == self.mt.POSITION_TYPE_BUY else self.mt.symbol_info_tick(position.symbol).ask,
                        "comment": "Position closed",
                        "type_time": self.mt.ORDER_TIME_GTC,  # Good till cancelled
                        "type_filling": self.mt.ORDER_FILLING_IOC,  # Immediate or cancel
                    }

                    # Send the close request
                    result = self.mt.order_send(request)

                    # Check the result of the request
                    if result.retcode != self.mt.TRADE_RETCODE_DONE:
                        print(f"Failed to close position {position.ticket}, error code: {result.retcode}")
                    else:
                        print(f"Position {position.ticket} for {position.symbol} closed successfully.")

            # Shutdown after processing all positions
            self.shutdown()

        except Exception as e:
            print("Error:", e)
            self.shutdown()  # Shutdown in case of any error
            return f"Error: {e}"


    
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
        
        self.login()
        
        symbol = "BTCUSDm"
        timeframe = self.mt.TIMEFRAME_M5  # 5-minute time frame
        lookback_period = 5  # Lookback period for finding swing highs/lows
        bars_to_check = 100  # Number of bars to fetch for analysis
    
        # Get the recent bars
        utc_from = datetime.now()  # Fetch recent data starting from now
        rates = self.mt.copy_rates_from(symbol, timeframe, utc_from, bars_to_check)

        # Convert to DataFrame for easy handling
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')

        # Find the swing high (if the high of the current candle is greater than the highs of the surrounding candles)
        def is_swing_high(df, index, period):
            if index < period or index >= len(df) - period:
                return False
            high = df['high'][index]
            for i in range(1, period + 1):
                if high <= df['high'][index - i] or high <= df['high'][index + i]:
                    return False
            return True

        # Find the swing low (if the low of the current candle is less than the lows of the surrounding candles)
        def is_swing_low(df, index, period):
            if index < period or index >= len(df) - period:
                return False
            low = df['low'][index]
            for i in range(1, period + 1):
                if low >= df['low'][index - i] or low >= df['low'][index + i]:
                    return False
            return True

        # Initialize variables to store the most recent swing high and low
        recent_swing_high = None
        recent_swing_low = None

        # Loop through the data to find the most recent swing high and low
        for i in range(lookback_period, len(df) - lookback_period):
            if is_swing_high(df, i, lookback_period):
                self.recent_swing_high = df['high'][i]
            if is_swing_low(df, i, lookback_period):
                self.recent_swing_low = df['low'][i]
        print(f"Most recent swing high: {self.recent_swing_high}")
        print(f"Most recent swing low : {self.recent_swing_low }")
        return recent_swing_high, recent_swing_low
    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############            
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        

    def temp(self):
        
        low  = self.recent_swing_low
        high = self.recent_swing_high
        
        #print(low, "\n", high)
        
        symbol = "BTCUSDm"
        buy    = self.mt.symbol_info_tick(symbol).ask
        sell   = self.mt.symbol_info_tick(symbol).bid
        
        temp = (buy - low) * 2
        print("Current Price", buy)
        print("Profit", temp) 
        print("Loss", low)

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############            
    def buy_btcusd(self):
                
        """self.swing_high_low()
        time.sleep(3)
        
        high = self.recent_swing_high
        low  = self.recent_swing_low
        
        time.sleep(1)"""
        
        symbol = "BTCUSDm"
        buy    = self.mt.symbol_info_tick(symbol).ask
        sell   = self.mt.symbol_info_tick(symbol).bid

        """print(f'high = {high}')
        print(f'low  = {low }')
        print(f'buy  = {buy }')"""
        
        spread = buy - sell
        print(f"Spread = {spread}")
        
        """sl   = low
        temp = (buy - sl) * 2
        tp   = temp + buy"""
        sl = buy - 80
        tp = buy + 100
        
        print(f'TP = {tp}')
        
        request = {
            'action': self.mt.TRADE_ACTION_DEAL,
            'symbol': symbol,
            "volume": 1.0,
            #'volume': 0.01,
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

            # Ensure that we return the comment at the end of the function
            #return request['comment']
    
    def buy_btc_order(self):
        
        try: 
            
            self.login()
            self.buy_btcusd()
            
            
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
        
        """self.swing_high_low()
        time.sleep(3)    
        
        high = self.recent_swing_high
        low  = self.recent_swing_low"""
                
        symbol = "BTCUSDm"
        buy    = self.mt.symbol_info_tick(symbol).ask
        sell   = self.mt.symbol_info_tick(symbol).bid

        """print(f'high  = {high}')
        print(f'low   = {low }')
        print(f'buy   = {buy }')
        print(f'sell  = {sell }')"""
        
        spread = buy - sell
        print(f"Spread = {spread}")

        """sl   = high
        temp = (sl - sell) *2
        tp   = sell - temp"""
        
        sl = sell + 80
        tp = sell - 100

        print(f'TP = {tp }')
        print(f'SL = {sl }')
        
        request = {
        "action": self.mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        #"volume": 10.0,
        'volume': 1.0,
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
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        

    def shutdown(self):
        
        process_name = "terminal64.exe"
        os.system(f"taskkill /f /im {process_name}")

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
    

#mt5().login()
#mt5().acc_info()


#mt5().buy_btc_order()
#mt5().sell_btc_order()

#mt5().profit()
#time.sleep(10)
#mt5().close_positions()
