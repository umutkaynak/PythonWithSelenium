faiz=1.59
vade="36"
krediAdi="İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

#print(vade+2)
#metinsel karakter ile sayısal değer arasınad matematiksel işlemler yapılmaz

#print("36"+2)
#dolayısıyla tip dönüşümü yapılmalı.
print(int(vade)+12) #vade değişkenini int değişkene değiştirdi.

print(type(str(faiz)))

vade=int(input("istenen vade sayısını giriniz: "))
print(vade)
#kulanıcadan vade istenen değer alınır ama alınan değerin türüde sayısal mı?
print(type(vade))
#int türde veri almak için tanımlarken int türüne çevirirsek daha rahat ederiz.
vade=vade+12

        #string interpolation
print("seçilen vade sonucu ortaya çıkan vade: " + str(vade))
print("seçilen vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))

