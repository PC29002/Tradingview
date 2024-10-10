from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.keys import Keys
import time, pickle

class tradingview_main():

    def __init__(self):
        
        pass
        
    def selenium(self):
        
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach",True)
        #option.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=option)
        
    
    def loadcookie(self):
        self.driver.get("https://www.tradingview.com/accounts/signin/")
        
        user_name = "prajchan@gmail.com"
        psw_name  = "aSWL6~<6crm2" 

        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div/div/div[2]/div/div/button").click()
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div/div/div[2]/div/div/div/form/div[1]/span[2]").send_keys(user_name)
        self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div/div/div[2]/div/div/div/form/div[2]/span[2]").send_keys(psw_name)
        #submit = driver.find_element(By.XPATH,"//span[contains(text(),'Sign in')]").click()

        time.sleep(20)

        cookies = self.driver.get_cookies()
        print(cookies)

        pickle.dump(cookies,open('cookies.pkl','wb')) 
    
    def usecookie(self):
        self.driver.get('https://www.tradingview.com/accounts/signin/')

        cookies = pickle.load(open("cookies.pkl", "rb"))

        for cookie in cookies:
            cookie['domain'] = ".tradingview.com"
        
            try:
                self.driver.add_cookie(cookie)
            except Exception as e:
                print(e)
    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############   
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############       
    
    def chart_btcusd(self):
        
        self.driver.get("https://in.tradingview.com/chart/?symbol=BINANCE%3ABTCUSD")
        print("Login Successful")
        print("\n")

        
        time.sleep(5)    

        # 30 Mins Scalping - MACD   
        # Macd
        macd    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div").value_of_css_property("color")
        macdhex = Color.from_string(macd).hex    
        
        #BASE Indicator
        macd_TriangleG    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[7]/div").value_of_css_property("color")
        macd_TrianglehexG = Color.from_string(macd_TriangleG).hex    
        
        macd_TriangleR    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[8]/div").value_of_css_property("color")
        macd_TrianglehexR = Color.from_string(macd_TriangleR).hex  
        
        ##########################################################
        
        # 30 Mins Scalping - EMA   
        # EMA
        EMA    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[5]/div").value_of_css_property("color")
        EMAhex = Color.from_string(EMA).hex    
        
        #BASE Indicator
        EMA_TriangleG    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        EMA_TrianglehexG = Color.from_string(EMA_TriangleG).hex    
        
        EMA_TriangleR    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        EMA_TrianglehexR = Color.from_string(EMA_TriangleR).hex 
        
        
        print("BTCUSD =>")
        print("Signal MACD :",macd_TrianglehexG, macd_TrianglehexR, macdhex)
        print("Signal EMA  :",EMA_TrianglehexG , EMA_TrianglehexR , EMAhex)
        self.col_btcusd = [macd_TrianglehexG, macd_TrianglehexR, macdhex, EMA_TrianglehexG , EMA_TrianglehexR , EMAhex]
                
            
    def color_ident_btc(self):
        
        b = self.col_btcusd
        
        green  = '#00ff00' #    Buy 
        red    = '#ffff00' # Red Sell
        
        if  (b[0] == green and b[2] == red):
            #print("BTC Green")
            unit = "BTC Green"
        
        elif (b[1] == red and b[2] == green):
            #print("BTC Red")
            unit = "BTC Red"

        elif (b[3] == green and b[5] == red):
            #print("BTC Green")
            unit = "BTC Green"
        
        elif(b[4] == red and b[5] == green):
            #print("BTC Red")
            unit = "BTC Red"
        
        else:
            #print("avoid")
            unit = "avoid"
                
        return unit
                
    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
    def run_crypto(self):
        
        try:
            
            print(time.ctime(time.time()))
            self.selenium()
            self.usecookie()

            self.chart_btcusd()
            
            self.driver.quit()
            
            a = self.color_ident_btc()        
            color = [a]
            return color
        
        except Exception as e:
            
            print(e)
            self.driver.quit()


###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############            
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    


