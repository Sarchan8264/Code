isim=input("Adinizi girin")
import math

print("salam " , isim)



s1=int(input("Birinci sayi girin ="))
s2=int(input ("ikinci sayi girin ="))

toplama=s1+s2
ortalama = toplama/2

print(toplama)
print(ortalama)






a=int(input("a sayisini girin :"))
b=int(input("b sayisini girin :"))
c=int(input("c sayisini girin :"))

if a>b and a>c:
   print("a en boyuk sayidir")
elif b>c and b>a:
    print("b en  boyuk  sayidir")
else:
    print("c en boyuk  sayidir")



a=int(input("a :"))
b=int(input("b :"))
c=int(input("c :"))

delta = b**2 - (4*a*c)
print(delta)

if delta>0:
   kok1=(-b+math.sqrt(delta))/(2*a)
   kok2=(-b-math.sqrt(delta))/(2*a)
   print("sistemin  2 koku  vardir" , kok1, "----", kok2)






while True:
      n=int(input("baslangic sayisin girin:"))
      m=int(input("bitis sayisin girin:"))
      if n>=m:
         print("baslangic saysisn daha kucuk girin,tekrar  deneyin")
      else:

        break



toplam=0

for i in range(n,m):
    if i%7==0:
        toplam+=i

print("yediyye  tam bolunenlerin toplami=",toplam)





isim=input("isiminiz girin :")

print(isim[::-1])

Ad =len(isim)
print(Ad)



ters = ""

for i in range(Ad-1,-1,-1):
    ters += isim[i]
print (ters)



yazi = input("bir metin yazin:")

sait_herfler ="aeıəioöuü"

samit_herfler = 0

for harf in yazi:
    if harf in sait_herfler:
        samit_herfler += 1
print("sait herflerin sayisi=",samit_herfler)
print("samit seslerin  sayisi=",len(yazi)-samit_herfler)






a=int(input("a :"))
b=int(input("b :"))
c=int(input("c :"))

delta=b**2-(4*a*c)
print(delta)

if delta>0:
 kok1 =(-b+math.sqrt(delta)) / (2*a)
 kok2 =(-b-math.sqrt(delta)) / (2*a)
 print("sistemin  2 koku var", kok1, "--",kok2)
elif delta ==0:
   kok=-b/(2*a)
   print("cakisik kok",kok)
else:
     print("sistemin  koku yoxdur")





v=int(input("Vize:"))
f=int(input("Final:"))
ortalama=v*0.40+f*0.60
print("ortalam=",ortalama)
if ortalama>=50:
 print("kecdi")
else:
 print("kaldi")




toplam=0

for i in range(100):
 toplam+=i

print(toplam)

1-1-2-3-5-8-13-21

a=1
b=1
c=2
while c<1000:
    print(b)
    c=a+b
    a=b
    b=c




# "sadece 1 -e  ve  kendisine  bolunen  ,13-> 2,3,4,......,12


bolen_sayi=0

for j in range(3,1000):
    bolen_sayi = 0
    for i in range(2,j):
       if(j%i==0):
            bolen_sayi+=1
    if bolen_sayi==0:
        print(j)


#kullanicidan 10 adet sayi alan   tek  ve cift sayilarin adetini ,
 #toplamini  ve ortalamalarini  bulan  programini  yaziniz ?



s=0
tek_sayac=0
cift_sayac=0
tek_toplam=0
cift_toplam=0

for sayi in  range(1,11):
    s=int(input("sayiniz girin:"))
    if s%2==1:
        tek_sayac+=1
        tek_toplam+=1
    else:
        cift_sayac+=1
        cift_toplam+=1
print(tek_sayac,"adet tek sayi vardir toplamlari",tek_toplam)
print("tek sayilarin ortalamasi", tek_toplam/tek_sayac)
print(cift_sayac,"adet cift sayi vardir toplamlari",cift_toplam)
print("tek sayilarin ortalamasi", cift_toplam/cift_sayac)



#kullanicinin  istediyi kadar  sayini kullanicidan alaraq bir diziye aktaran
#bu sayini toplamin  ve  ortalamsini  progrmini  yaziniz

adet=int(input("kac edet sayinizi giriniz:"))
dizi =[]
for i in range(adet):
    dizi.append(int(input("sayinizi giriniz:")))
print(dizi)
toplam=0
for x in dizi:
    toplam+=x

print("toplam",toplam)
print("ortalama",toplam/adet)






#  kullanicin istedigi  buyuklukte bir  diziyi
# 0-100 arasinda  rastgele olusturulmus sayilarla doldurulup
# bu  sayilarin standart sapmasini hesablayiniz

import random
u = int(input("dizi uzunlugunu girin:"))
dizi=[]
for i in range(u):
    dizi.append(random.randint(0,100))
print(dizi)
toplam=0
for x in dizi:
    toplam+=x
print(("toplam=",toplam))
ortalama=toplam/u
print(("ortalama =",ortalama))
fark_toplam=0
for x in dizi:
    fark =x-ortalama
    fark=fark**2
    fark_toplam+=fark
ssapma=math.sqrt(fark_toplam/u)
print("standart sapma=",ssapma)




 #kullancidan alinan bir cumlede kac adet kelime oldugunu
#ve kac edet  harf oldugunu bulan  pogramin  yazin

s=input("Bir string  giriniz:")
bosluk_sayac=0
for k in s:
    if k ==" ":
        bosluk_sayac+=1
print("bosluk adeti=",bosluk_sayac)
print("kelim sayisi:",bosluk_sayac+1)
print("harf sayisi:",len(s))


for i in range(1000,100000):
    s=str(i)
    t=s[::-1]
    if s == t:
        print(s)
