#ilk kod

#ekrana çıktı yazma
print("Kodlamaio") 

#Değişkenler

#sürekli bir değer göndermek istersek
print("Taşıt Kredisi")
print("Taşıt Kredisi")
print("Taşıt Kredisi")
print("Taşıt Kredisi")
#sürekli printlemek yerine değişkene atayabiliriz

#değişken tanımlarken değişkene vermek istenen isim verilir
baslik = "Taşıt Kredisi"
print(baslik)


#Değişken Türleri
#string= metinsel ifadeleri temsil eder.
baslik="İhtiyaç Kredisi"
print(baslik)
#int= tam sayı
vade=36

ekVade=6

vade2="36" #int sayı gibi görünsede metinsel yani string türde veri türüdür. matematiksel operatörler kullanılamaz

#ondalıklı sayı - float , decimal , double gibi türleri mevcut 
aylikOdeme = 200.50

#bool , boolean=> true, yada false değerlerini alır. 
yukselisteMi=True 

#Matematiksel operatörler
#toplama
print(5 + 5)
print(vade + 12)
print(vade + ekVade)

#çıkartma
print(5-5)
print(vade-12)
print(vade)

#çarpma
print(5*5)
print(vade*2)
print(vade * ekVade)

#bölme
print(5/5)
print(vade/2)
print(vade/ekVade)


yeniVade = vade/2
fiyat = 100
indirimliFiyat = fiyat - 20
 
print(yeniVade)
print(indirimliFiyat)

#mod=sayıyıya bölümünden kalanı gösterir. % işaretiyle sembolize edilir.
print(10%2)
print(vade%ekVade)

#mantıksal operatorler
#eşitlik veya denklik
print(1==1) #  denk mi anlamına gelir ve eşitse true  değilse False değerini verir.
print(1==2)

# büyüklük operatoru.
print(1 > 2) #  büyükse true değilse false
print(3 > 1)

#eşitsizlik durumu
print(1 != 1) #1,1'e eşit değildir diyor. False dönecek çünkü eşit
print(1 != 2) #1, 2'ye eşit değildir diyor. True dönecek çünkü eşit değil



#or / and yapıları
# or birden fazla operatör kullanılacağı zaman kullanılır. sağlanan 2 değerin birinin doğru olması durumunda TRUE döner.sadece bir tane true değeri olması yeterlidir.
 
# and her ikisi doğru olmalı yada her ikisi false olmalı. bir tane karşıt değer yani true , false var ise cevap false döner.  karışık kullanımlarda kullanılır.
 
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2) 

#Şart yapıları "if - else"
sayi1 = 15
sayi2 = 15
# sayi1 > sayi2 ise  sayi1 daha büyük yazar


#condition = ŞART
if sayi1 < sayi2:
    #sayı true ise direkt cevabı verip şarttan çıkar.
    print("sayi1 daha küçüktür")
    print("Hala if bloğu içindeyim")
 
elif sayi1 == sayi2:
    #if bloğu sağlanmadığında girer.
    print("İki sayı eşittir")
else:
    #hiçbir şart sağlanmadığında bu döngüye girer.
    print("Sayi1 sayi2'den büyüktür")
#if else bloğundan ayrı ve bağımsızz olarak çalışır.
print("dışında")

