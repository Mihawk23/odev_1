# strange metin türü ifadeleri belirtir
metin="Merhaba"
print(type(metin))
print(metin)
# integer sayısal değerleri ifade eder
sayi=16
print(type(sayi))
print(sayi)
# list, range dizi sayıları
list=["1","2","3"]
print(type(list))

for i in list:
  print(i)
print("*******")
#i=0 i<11
for i in range(5):
  print(i)

# bool mantıksal tipleri ifade eder

yeni = True
eski = False
if False:
  print(yeni)
else:
  print(eski)
  
print("*******")
# giriş yapma kısmını örnek verebiliriz

kullaniciAdi= "Osman"
kullaniciSifre=123

giris=input("Lütfen kullanıcı adınızı giriniz:")
sifre=int(input("Lütfen şifrenizi giriniz:"))
if giris==kullaniciAdi and sifre==kullaniciSifre:
  print("Hoşgeldiniz")
else:
  print("Tekrar deneyiniz.")