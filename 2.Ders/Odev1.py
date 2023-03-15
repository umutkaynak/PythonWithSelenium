                        #Öğrenci Kayıt Sistemi

"""
Aldığı isim soy isim ile listeye öğrenci ekleyen

Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
Listeye birden fazla öğrenci eklemeyi mümkün kılan
Listedeki tüm öğrencileri tek tek ekrana yazdıran
Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.
Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir."""


liste=["umut kaynak","ali soydan","sudenur toprak","sedat devecik"]

#Aldığı isim soy isim ile listeye öğrenci ekleyen
def ekle():
    adSoyad=input("ad soyad gir: ")
    liste.append(adSoyad)#listeye ekler
#Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
def sil():
    adSoyad=input("ad soyad gir: ")
    for i in liste:
      if i==adSoyad:
        liste.remove(adSoyad)

#Listeye birden fazla öğrenci eklemeyi mümkün kılan            
def exEkle():
    devam=True
    while devam==True:
        adSoyad=input("ad soyad gir, durmak için 'stop' yaz: ").lower()
        liste.append(adSoyad)
        if adSoyad=="stop":
          liste.remove(adSoyad)#stop komutunun da yazdığımızda en son listeden siliyoruz ki gözükmesin
          devam=False
          
#Listedeki tüm öğrencileri tek tek ekrana yazdıran
def ogrenciGoster():
   for i in liste:
      print(i)

#Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
def ogrenciNumara():
   ogrenci=input("numarasını öğrenmek istedğiniz öğrencinin adını girimn")
   liste.index(ogrenci)

#Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
def exSil():
   devam=True
   while devam==True:
       adSoyad=input("silmek istediğiniz öğrencinin ad soyad gir, durmak için 'stop' yaz: ").lower()
       if adSoyad=="stop":
          devam=False
       else:
          liste.remove(adSoyad)
      

ekle()
sil()
exEkle()
ogrenciGoster()
ogrenciNumara()
exSil()


