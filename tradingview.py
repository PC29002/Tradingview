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
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############       
    
    def chart_btcusd(self):
        
        self.driver.get("https://in.tradingview.com/chart/?symbol=BINANCE%3ABTCUSD")
        print("Login Successful")
        print("\n")

        # EFmus
        time.sleep(5)    

        # 1 EMA Triangle and SuperTrend Cross    
        # HypT
        HypT    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        HypThex = Color.from_string(HypT).hex    
        
        #Macd
        macd    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        macdhex = Color.from_string(macd).hex 
        
        #BASE Indicator
        EMA_TriangleG    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div").value_of_css_property("color")
        EMA_TrianglehexG = Color.from_string(EMA_TriangleG).hex    
        
        EMA_TriangleR    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[4]/div").value_of_css_property("color")
        EMA_TrianglehexR = Color.from_string(EMA_TriangleR).hex  
        
        print("BTCUSD =>")
        print("Signal  :",EMA_TrianglehexG, EMA_TrianglehexR, HypThex, macdhex)
        self.col_btcusd   = [EMA_TrianglehexG, EMA_TrianglehexR, HypThex, macdhex]
                
            
    def color_ident_btc(self):
        
        # 1 EMA Triangle and SuperTrend Cross
        b = self.col_btcusd
                
        """green = #00ff00
        red   = #ffff00"""
        
        if  (b[0] == b[2] == b[3] == "#00ff00"):
            #print("BTC Green")
            unit = "BTC Green"
        
        elif (b[1] == b[2] == b[3]  == "#ffff00"):
            #print("BTC Red")
            unit = "BTC Red"

        else:
            #print("avoid")
            unit = "avoid"
                
        return unit
                
    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
    def chart_xauusd(self):
        
        self.driver.get("https://in.tradingview.com/chart/?symbol=FOREXCOM%3AXAUUSD")

        # EFmus
        time.sleep(5)    

        # 1 EMA Triangle and SuperTrend Cross    
        
        # S-P
        HypT    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        HypThex = Color.from_string(HypT).hex    
        
        #Macd
        macd    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        macdhex = Color.from_string(macd).hex 
        
        #BASE Indicator
        EMA_TriangleG    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div").value_of_css_property("color")
        EMA_TrianglehexG = Color.from_string(EMA_TriangleG).hex    
        
        EMA_TriangleR    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[4]/div").value_of_css_property("color")
        EMA_TrianglehexR = Color.from_string(EMA_TriangleR).hex  
        
        
        print("XAUUSD =>")
        print("Signal  :",EMA_TrianglehexG, EMA_TrianglehexR, HypThex, macdhex)
        self.col_xauusd = [EMA_TrianglehexG, EMA_TrianglehexR, HypThex, macdhex]
        
    def color_ident_xauusd(self):
        
        # 1 EMA Triangle and SuperTrend Cross
        b = self.col_xauusd
        
        if  (b[0] == b[2] == b[3] == "#00ff00"):
            #print("BTC Green")
            unit = "XAU Green"
        
        elif (b[1] == b[2] == b[3] == "#ff0000"):
            #print("BTC Red")
            unit = "XAU Red"

        else:
            #print("avoid")
            unit = "avoid"
                
        return unit

    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
    def chart_bgpjyp(self):
        
        self.driver.get("https://in.tradingview.com/chart/?symbol=FOREXCOM%3AGBPJPY")

        # EFmus
        time.sleep(5)    

        # 1 EMA Triangle and SuperTrend Cross    
        
        # S-P
        HypT    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        HypThex = Color.from_string(HypT).hex    
        
        #Macd
        macd    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        macdhex = Color.from_string(macd).hex 
        
        #BASE Indicator
        EMA_TriangleG    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div").value_of_css_property("color")
        EMA_TrianglehexG = Color.from_string(EMA_TriangleG).hex    
        
        EMA_TriangleR    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[4]/div").value_of_css_property("color")
        EMA_TrianglehexR = Color.from_string(EMA_TriangleR).hex  
        
        
        print("BGPJYP =>")
        print("Signal  :",EMA_TrianglehexG, EMA_TrianglehexR, HypThex, macdhex)
        self.col_bgpjyp = [EMA_TrianglehexG, EMA_TrianglehexR, HypThex, macdhex]
        
    def color_ident_bgpjyp(self):
        
        # 1 EMA Triangle and SuperTrend Cross
        b = self.col_bgpjyp
        
        if  (b[0] == b[2] == b[3] == "#00ff00"):
            #print("BTC Green")
            unit = "BGPJYP Green"
        
        elif (b[1] == b[2] == b[3] == "#ff0000"):
            #print("BTC Red")
            unit = "BGPJYP Red"

        else:
            #print("avoid")
            unit = "avoid"
                
        return unit

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
    def chart_oil(self):
        
        self.driver.get("https://in.tradingview.com/chart/?symbol=TVC%3AUSOIL")

        # EFmus
        time.sleep(5)    

        # 1 EMA Triangle and SuperTrend Cross    
        
        # S-P
        HypT    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        HypThex = Color.from_string(HypT).hex    
        
        #Macd
        macd    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        macdhex = Color.from_string(macd).hex 
        
        #BASE Indicator
        EMA_TriangleG    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div").value_of_css_property("color")
        EMA_TrianglehexG = Color.from_string(EMA_TriangleG).hex    
        
        EMA_TriangleR    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[4]/div").value_of_css_property("color")
        EMA_TrianglehexR = Color.from_string(EMA_TriangleR).hex  
        
        
        print("OIL =>")
        print("Signal  :",EMA_TrianglehexG, EMA_TrianglehexR, HypThex, macdhex)
        self.col_oil = [EMA_TrianglehexG, EMA_TrianglehexR, HypThex, macdhex]
        
    def color_ident_oil(self):
        
        # 1 EMA Triangle and SuperTrend Cross
        b = self.col_oil
        
        if  (b[0] == b[2] == b[3] == "#00ff00"):
            #print("BTC Green")
            unit = "OIL Green"
        
        elif (b[1] == b[2] == b[3] == "#ff0000"):
            #print("BTC Red")
            unit = "OIL Red"

        else:
            #print("avoid")
            unit = "avoid"
                
        return unit

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
    def chart_audnzd(self):
        
        self.driver.get("https://in.tradingview.com/chart/?symbol=FOREXCOM%3AAUDNZD")

        # EFmus
        time.sleep(5)    

        # 1 EMA Triangle and SuperTrend Cross    
        
        # S-P
        HypT    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        HypThex = Color.from_string(HypT).hex    
        
        #Macd
        macd    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        macdhex = Color.from_string(macd).hex 
        
        #BASE Indicator
        EMA_TriangleG    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div").value_of_css_property("color")
        EMA_TrianglehexG = Color.from_string(EMA_TriangleG).hex    
        
        EMA_TriangleR    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[4]/div").value_of_css_property("color")
        EMA_TrianglehexR = Color.from_string(EMA_TriangleR).hex  
        
        
        print("AUDNZD =>")
        print("Signal  :",EMA_TrianglehexG, EMA_TrianglehexR, HypThex, macdhex)
        self.col_audnzd = [EMA_TrianglehexG, EMA_TrianglehexR, HypThex, macdhex]
        
    def color_ident_audnzd(self):
        
        # 1 EMA Triangle and SuperTrend Cross
        b = self.col_audnzd
        
        if  (b[0] == b[2] == b[3] == "#00ff00"):
            #print("BTC Green")
            unit = "AUDNZD Green"
        
        elif (b[1] == b[2] == b[3] == "#ff0000"):
            #print("BTC Red")
            unit = "AUDNZD Red"

        else:
            #print("avoid")
            unit = "avoid"
                
        return unit

###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############        
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
    
    def run_uscap(self):
        
        try:
            
            print(time.ctime(time.time()))
            self.selenium()
            self.usecookie()

            self.chart_btcusd()
            self.chart_xauusd()
            self.chart_bgpjyp()
            self.chart_audnzd()
            self.chart_oil()
            
            self.driver.quit()
            
            a     = self.color_ident_btc()
            b     = self.color_ident_xauusd()
            c     = self.color_ident_bgpjyp()
            d     = self.color_ident_audnzd()
            e     = self.color_ident_oil()
        
            color = [a, b, c, d, e]
            return color
        
        except Exception as e:
            
            print(e)
            self.driver.quit()
        
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

    


