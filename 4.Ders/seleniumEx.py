from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()#açılan ekranı tam ekran yapar
driver.get("https://www.google.com")#verilen url'nin açıılmasını sağlar

input=driver.find_element(By.NAME,"q")
sleep(4)#ekleme işlemi olacağından intertte arama  kısmaında internet hızına göre hata verememesi için bekleme attık
input.send_keys("kodalamaio")#arama kısmına kodlamaiovv


searchButton= driver.find_element(By.NAME,"btnK")
sleep(2)
searchButton.click()
firstResult=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a ")
sleep(2)
firstResult.click()

listOfCourse= driver.find_elements(By.CLASS_NAME,"course-listing")
print(f" Kodlamaio sitesinde şuanda : {len(listOfCourse)} adet kurs vardır")

# sleep(10)#10 sn bekler
while True:
    pass
#HTML LOCATORS
    #web safyasının yüklenen kodları input içinde arama yapma denebilir.

#full xPath
# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a