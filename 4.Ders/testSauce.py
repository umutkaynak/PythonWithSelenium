from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Sauce:
    def test_invalid_login(self):    
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        # sleep(5)
        #ilerleryen derslerde sleep yerine  en fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        # sleep(2)
        userNameInput.send_keys("1")
        passwordInput.send_keys("2")
        # sleep(2)
        login=driver.find_element(By.ID,"login-button")
        login.click()
        erorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult=erorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")
        


testClass=Test_Sauce()
testClass.test_invalid_login()

