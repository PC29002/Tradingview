from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
import time
import pickle

class tradingview_main():


    def selenium(self):
        
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach",True)
        #option.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service('E:\\VS code\\Projects\\Seleium\\Selenium 3 Elements\\chromedriver.exe'), options=option)

    
    def loadcookie(self):
        self.driver.get("https://www.tradingview.com/accounts/signin/")
        user_name = "prajchan@gmail.com"
        psw_name  = "aSWL6~<6crm2" 

        self.driver.find_element(By.XPATH,"//span[@class='ellipsis-container-bYDQcOkp'][normalize-space()='Email']").click()
        self.driver.find_element(By.XPATH,"//input[@id='id_username']").send_keys(user_name)
        self.driver.find_element(By.XPATH,"//input[@id='id_password']").send_keys(psw_name)
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
   
    def chart_btcusd(self):
        
        self.driver.get("https://in.tradingview.com/chart/?symbol=BINANCE%3ABTCUSD")
        print("Login Successful")
        print("\n")

        # EFmus
        time.sleep(5)    

        # 1 EMA Triangle and SuperTrend Cross
        #BASE Indicator
        EMA_Triangle1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        EMA_Trianglehex1 = Color.from_string(EMA_Triangle1).hex    
        
        EMA_Triangle2    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        EMA_Trianglehex2 = Color.from_string(EMA_Triangle2).hex    

        #SuperTrend Cross
        SuperTrend_Cross    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[5]/div").value_of_css_property("color")
        SuperTrend_Crosshex = Color.from_string(SuperTrend_Cross).hex    
        
        # SuperTrend 
        SuperTrend    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div").value_of_css_property("color")
        SuperTrendhex = Color.from_string(SuperTrend).hex    
        
        # 2 RSI Candle and MACD Normal With EMA Triangle 
        #BASE Indicator
        EMA_Triangle3    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        EMA_Trianglehex3 = Color.from_string(EMA_Triangle3).hex
        
        EMA_Triangle4    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        EMA_Trianglehex4 = Color.from_string(EMA_Triangle4).hex    

        #MACD Normal
        MACD_Normal    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[5]/div").value_of_css_property("color")
        MACD_Normalhex = Color.from_string(MACD_Normal).hex    
        
        
        print("BTCUSD =>")
        print("Signal  :", EMA_Trianglehex1, EMA_Trianglehex2, SuperTrend_Crosshex, SuperTrendhex, EMA_Trianglehex3, EMA_Trianglehex4, MACD_Normalhex)
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
        
        # ('BTC Red', 'avoid')       = output: BTC Red
        # ('avoid', 'BTC Red')       = output: BTC Red
        # ('BTC Green', 'avoid')     = output: BTC Green
        # ('avoid', 'BTC Green')     = output: BTC Green
        
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
    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
    
    def chart_gold(self):
        
        self.driver.get("https://in.tradingview.com/chart/?symbol=FPMARKETS%3ABTCUSD")
        print("\n")
        
        # EFmus
        time.sleep(5)    

        # 1 EMA Triangle and SuperTrend Cross
        #BASE Indicator
        EMA_Triangle    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        EMA_Trianglehex = Color.from_string(EMA_Triangle).hex    

        #SuperTrend Cross
        SuperTrend_Cross    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[5]/div").value_of_css_property("color")
        SuperTrend_Crosshex = Color.from_string(SuperTrend_Cross).hex    
        
        # SuperTrend 
        SuperTrend    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[6]/div").value_of_css_property("color")
        SuperTrendhex = Color.from_string(SuperTrend).hex    
        
        # 2 RSI Candle and MACD Normal With EMA Triangle 
        #BASE Indicator
        EMA_Triangle2    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        EMA_Trianglehex2 = Color.from_string(EMA_Triangle2).hex    

        #MACD Normal
        MACD_Normal    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[5]/div").value_of_css_property("color")
        MACD_Normalhex = Color.from_string(MACD_Normal).hex    
        
        print("Gold =>")
        print("Signal  :", EMA_Trianglehex, SuperTrend_Crosshex, SuperTrendhex, EMA_Trianglehex2, MACD_Normalhex)
        self.col_gold = [EMA_Trianglehex, SuperTrend_Crosshex, SuperTrendhex, EMA_Trianglehex2, MACD_Normalhex]
        
    
    def color_ident_gold(self):
        
        # 1 EMA Triangle and SuperTrend Cross
        b = self.col_gold
        if (b[0] == b[1] == "#ff0000") or (b[0] == b[2] == "#ff0000"):
            unit = "Gold Green"
            #print(unit)

        elif (b[0] == b[1] == "#00ff00") or (b[0] == b[2] == "#00ff00"):
            unit = "Gold Red"
            #print(unit)

        else:        
            unit = "avoid"
            #print(unit)
        
        # 2 RSI Candle and MACD Normal With EMA Triangle 
        b = self.col_gold
        if (b[3] == b[4] == "#ff0000"):
            unit1 = "Gold Green"
            #print(unit1)

        elif (b[3] == b[4] == "#00ff00"):
            unit1 = "Gold Red"
            #print(unit1)
        else:
            unit1 = "avoid"
            #print(unit1)
        
        # ('Gold Green', 'Gold Green') = output: Gold Green
        # ('Gold Red', 'Gold Red')     = output: Gold Red
        # ('avoid', 'avoid')         = output: avoid
        
        # ('Gold Red', 'avoid')       = output: Gold Red
        # ('avoid', 'Gold Red')       = output: Gold Red
        # ('Gold Green', 'avoid')     = output: Gold Green
        # ('avoid', 'Gold Green')     = output: Gold Green
        
        # ('Gold Red', 'Gold Green')   = output: avoid
        # ('Gold Green', 'Gold Red')   = output: avoid
                
        if unit == unit1:
            return unit
        
        elif unit == "Gold Red" and unit1 == "avoid":
            return "Gold Red"
        
        elif unit == "avoid" and unit1 == "Gold Red":
            return "Gold Red"
        
        elif unit == "Gold Green" and unit1 == "avoid":
            return "Gold Green"
        
        elif unit == "avoid" and unit1 == "Gold Green":
            return "Gold Green"
        
        else:
            return "avoid"
        
        
    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
    def chart_ethusd(self):
        self.driver.get("https://in.tradingview.com/chart/?symbol=FPMARKETS%3AETHUSD")
        print("\n")
        
        # EFmus
        time.sleep(5)    
   
        signal1    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        signalhex1 = Color.from_string(signal1).hex    

        signal2    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        signalhex2 = Color.from_string(signal2).hex    
        
        signal3    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[5]/div").value_of_css_property("color")
        signalhex3 = Color.from_string(signal3).hex    
        
        print("ETH USd =>")
        print("Signal  :", signalhex1, signalhex2, signalhex3)
        self.col_ethusd = [signalhex1, signalhex2, signalhex3]
        
    def color_ident_ethusd(self):
        
        b = self.col_ethusd
        if b[0] == b[2] and b[2] == "#00ff00":
            #print("Gold Green")
            unit = "Eth Usd Green"
            
        elif b[1] == b[2] and b[2] == "#ff0000":
            #print("Gold Red")
            unit = "Eth Usd Red"
            
        else:
            #print("Gold Avoid")
            unit = "avoid"
        return unit

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
    
    def run_uscap(self):
        
        try:
            
            print(time.ctime(time.time()))
            self.selenium()
            self.usecookie()

            self.chart_btcusd()
            #self.chart_gold()
            #self.chart_ethusd()
            
            self.driver.quit()
            
            a     = self.color_ident_btc()
            #b     = self.color_ident_gold()
            #c     = self.color_ident_ethusd()
        
            #color = [a,b,c]
            color = [a]
            
            return color
        
        except Exception as e:
            
            print(e)
            self.driver.quit()
        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############
        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############            
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    

    
def test():
    
    print("\nBot has started")
    z = tradingview_main()
    
    print(z.run_uscap())
    
