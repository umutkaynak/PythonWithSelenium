from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Kodlamaio:
    def test_invalid_login(self):    
    #kişinin doğru giriş yapmadığı kontrolü edecek.
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.kodlama.io/")
        sleep(3)
        loginBtn=driver.find_element(By.XPATH,"/html/body/header/div/div/div/div/ul/li[3]/a")
        loginBtn.click()
        sleep(30)


testClass=Test_Kodlamaio
testClass.test_invalid_login("s")

while True:
    pass

