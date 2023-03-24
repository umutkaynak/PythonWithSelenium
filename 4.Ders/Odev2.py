                    # AMAÇ:
# Derste gösterilen konuların pekiştirilmesi.

                # ÖDEV TANIMI:

# Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.
# Yazacağınız tüm kodları oluşturduğunuz bir classda fonksiyonlar oluşturarak gerçekleştiriniz. Bu classın fonksiyonlarını çağırarak test ediniz.

                        # Test Caseler;
# Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
# Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
# Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
#. Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır.
# ..Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
# Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
# Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

class Case:
    def uPAllert(self):
        driver= webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        #kullanıcı adı şifre değerleri girme
        userNameİnput=driver.find_element(By.ID,"user-name")
        userPassword=driver.find_element(By.ID,"password")
        #boş değerleri atama
        userNameİnput.send_keys("")
        userPassword.send_keys("")
        #login etme
        login=driver.find_element(By.ID,"login-button")
        login.click()
        sleep(5)
        #hata mesajı doğrulama
        hata=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        donus=hata=="Epic sadface: Username is required"
        #hata mesajını ekrana gösterme
        print(f"TEST SONUCU: {donus}")
        sleep(10)
        

    def pasAlert(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        uName=driver.find_element(By.ID,"user-name")
        uPassword=driver.find_element(By.ID,"password")
        uName.send_keys("giris")
        uPassword.send_keys("")
        
        log=driver.find_element(By.ID,"login-button")
        log.click()
        # sleep(3)
        message=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        donus=message=="Epic sadface: Password is required"
        print(f"TEST SONUC: {donus}")
        sleep(10)

    def req(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        UserName=driver.find_element(By.ID,"user-name")
        UPasword=driver.find_element(By.ID,"password")
        UserName.send_keys("locked_out_user")
        UPasword.send_keys("secret_sauce")
        login=driver.find_element(By.ID,"login-button")
        login.click()

        err=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        donus =err.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {donus}")
        sleep(10)

    def x(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        uName=driver.find_element(By.ID,"user-name")
        uPass=driver.find_element(By.ID,"password")
        uName.send_keys("")
        uPass.send_keys("")
        log=driver.find_element(By.ID,"login-button")
        log.click()
        sleep(3)
        errClose=driver.find_element(By.CLASS_NAME,"error-button")
        errClose.click()
        sleep(10)
    def transfer(self):
        uName=driver.find_element(By.ID,"user-name")
        uPas=driver.find_element(By.ID,"password")
        uName.send_keys("standard_user")
        uPas.send_keys("secret_sauce")
        log=driver.find_element(By.ID,"login-button")
        log.click()
    
    def pAmount(self):
        case.transfer()
        listOfCourse= driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f" sitede : {len(listOfCourse)} adet ürün var.")
        



    
    

    

case=Case()
#case.uPAllert()
#case.pasAlert()
#case.req()
#case.x()
#case.transfer()
case.pAmount()
