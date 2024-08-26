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
   
    def chart_btcusd(self):
        
        self.driver.get("https://in.tradingview.com/chart/?symbol=BINANCE%3ABTCUSD")
        print("Login Successful")
        print("\n")

        # EFmus
        time.sleep(5)    

        # 1 EMA Triangle and SuperTrend Cross    
        
        # Regression 
        regression    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        regressionhex = Color.from_string(regression).hex 
    
        # S-P
        SuppRes    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div").value_of_css_property("color")
        SuppReshex = Color.from_string(SuppRes).hex    
        
        #HyperTrend
        hypertrend    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div").value_of_css_property("color")
        hypertrendhex = Color.from_string(hypertrend).hex 
        
        #Macd
        macd    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[5]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div").value_of_css_property("color")
        macdhex = Color.from_string(macd).hex 
        
        #BASE Indicator
        EMA_TriangleG    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[4]/div").value_of_css_property("color")
        EMA_TrianglehexG = Color.from_string(EMA_TriangleG).hex    
        
        EMA_TriangleR    = self.driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div[5]/div").value_of_css_property("color")
        EMA_TrianglehexR = Color.from_string(EMA_TriangleR).hex  
        
        
        print("BTCUSD =>")
        print("Signal  :", EMA_TrianglehexG, EMA_TrianglehexR, SuppReshex, hypertrendhex, regressionhex, macdhex)
        self.col_btcusd = [EMA_TrianglehexG, EMA_TrianglehexR, SuppReshex, hypertrendhex, regressionhex, macdhex]
        
    def color_ident_btc(self):
        
        # 1 EMA Triangle and SuperTrend Cross
        b = self.col_btcusd
        
        if  (b[0] == b[2] == b[3] == b[4] == b[5] == "#00ff00"):
            #print("BTC Green")
            unit = "BTC Green"

        #elif (b[2] == '#00ff00' and b[3] == '#ff0000' and b[1] == '#ff0000'):
            #print('BTC Green')
        #    unit = "BTC Green"
        
        #elif (b[2] == '#ff0000' and b[3] == '#00ff00' and b[1] == '#ff0000'):
            #print('BTC Green')
        #    unit = "BTC Green"
        
        elif (b[1] == b[2] == b[3]  == b[4] == b[5]  == "#ff0000"):
            #print("BTC Red")
            unit = "BTC Red"

        #elif (b[2] == '#00ff00' and b[3] == '#ff0000' and b[0] == '#00ff00'):  
            #print('BTC Red')
        #    unit = "BTC Red"

        #elif (b[2] == '#ff0000' and b[3] == '#00ff00' and b[0] == '#00ff00'):  
            #print('BTC Red')
        #    unit = "BTC Red"

        else:
            #print("avoid")
            unit = "avoid"
                
        return unit
        # ('BTC Green', 'BTC Green') = output: BTC Green
        # ('BTC Red', 'BTC Red')     = output: BTC Red
        # ('avoid', 'avoid')         = output: avoid
        
        # ('BTC Red', 'avoid')       = output: BTC Red
        # ('avoid', 'BTC Red')       = output: BTC Red
        # ('BTC Green', 'avoid')     = output: BTC Green
        # ('avoid', 'BTC Green')     = output: BTC Green
        
        # ('BTC Red', 'BTC Green')   = output: avoid
        # ('BTC Green', 'BTC Red')   = output: avoid
                
    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
    
    
###############    ###############  ############### ############### ############### ############### ############### ############### ############### ############### ############### ###############    
    
    def run_uscap(self):
        
        try:
            
            print(time.ctime(time.time()))
            self.selenium()
            self.usecookie()

            self.chart_btcusd()
            
            self.driver.quit()
            
            a     = self.color_ident_btc()
        
            #color = [a,b]
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


