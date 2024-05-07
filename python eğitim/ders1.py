#sayılar ve stringlere giriş
#stringere giriş
#köşeli parantez olarak gönderdiğimizde
#python bunu string olğunu anlar
#stringlerde + ve * işlemleri kullanabilir

# LEN[] metodu 
#len strnglerin harf sayısını alır
# len() şeklinde kullanılır
#a ="geleceği_yazanlar"
#print(len(a)) #şeklinde kullanınca 17 vercektir

#UPPER ve LOWER metodları
#upper bütün harfleri büyütür
#lower bütün harfleri küçültür
#upper ve lower motedları {.upper()} şeklinde kullanılır
 
# isupper() veya is lower()
# stingin bütün harflerini kontrol eder
# isupper() butun harfleri büyükse true çıktısı verir

# REPLACE METODU
# .replace() şeklinde kullanılır
#bir stingde üzerinde yapacağımız değişikliği gösteriri 
#örnek aşağıdaki gibidir
#a ="geleceği yazanlar"
#print(a.replace("e", "O"))
#NOT: metodlarla yaptığımız işlemler kalıcı olsun istiyorsak
#metod uygulanmış hale değer atamaktır

# STRİP METODU
# .strip() şeklinde kullanılır
# boşluk ve özel karakterlerden kurtulmak için kullanılır
#örnek şekildeki gibidir
#a ="*****geleceği_yazanlar**"
#print(a.strip("*"))
#NOT strip metodunda özel karakter değişebiilir

#METODLARA GENEL BAKIŞ
# dir() fonksiyonu elimizde olan stringin uzerinde yapabileceğimiz özellikleri gösteririr
#dir() metodların hepsini gösteriri
#örnek altdaki formu yazdığımızı gösterir
#a ="geleceği_yazanlar"
#dir(a) bu kısım çok önemlidir.

#Karakter dizilerinde altküme işlemleri(Substrings)
#Elimizdeki karakterlerin alt bileşenlerine erişmek alt küme oluşturmak amacıyla kullanılır
#a ="geleceği_yazanlar"
#print(a[4]) c harfini verecektir
#a parametresindeki 0. indeksdeki karaktere ulaşmış oluyoruz
# eger a dan ilk üç harf veya 5 gibi istekde bulunucaksak
#print(a[0:3])şeklinde kullanmamız gerekir
#eger ikişer ikişer atla dersek veya 3 er
#a ="geleceği_yazanlar"
#print(a[0:8:2]) sıfırdan sekize kadar ikişer ikişer atla


# DEĞİŞKENLER
# a= 654865 GİBİ a değişkeni oluşturulur int
# b= "alı maldır" str dir
#bu atanan değişkenlerden direkt olarak işlem yapabiliriz

# TİP DÖNÜŞÜMLERİ
# İNPUT FONKSİYONU: kullanıcıdan bilgi almak için kullanılır
# string olarak gelen değerlerin başına int yazarak değiştirebiliriz
#terside mümkündür #float yazarakta ondalık yapabiliriz
 
#PRİNT FONKSİYONU
#EKRANA birşeyler yazdırmayı print ile yapıyoruz
#not alt görev belirteçlere arguman denir
#print("geleceği","yazanlar",sep = "_")
#yukarıdaki sep argumandır
#VERİ YAPILARI
#LİSTELER
#PYTHON da liste oluşturmak için iki yönetem vardır
#[] veya list()
# örnek:notlar=[90,80,50,60]

#Liste içi tip sorgulama
#ornek
#notlar=[90,80,50,60,"muhammet"]
#type(notlar[2]) 50 yanı int verir
#type(notlar[4]) muhammet yani str verir
#Liste birleştirme
#örnek
#notlar=[90,80,50,60,"muhammet"]
#notlar2=[90,80,50,60]
#tum_notlar=[notlar,notlar2]
#print(tum_notlar)
#liste silme "del notlar" bu işlem notlar listesini siler

#Liste elaman işlemleri
#oluşturduğumuz listedeki elamanlara erişmek
#liste=[10,20,30,50,60]
#liste[3]#4. indeksi alırız
#liste[0:3]#0 dan üçe kadar alırız
#liste içindweki listeye erişmek
#liste2=["a","b",10,60,90,[10,20,30,50,60]]
#print(liste2[5][3]) #şeklinde gerçekleşir

#Listeye eleman ekleme,silme ve değiştirme
#liste=["ali","veli","ahmet","memo"]
#listeki ali verisini alinin babası yapalım
#liste[0]="alinin_babası"
#print(liste)#şeklinde uygulanır
#çoklu değişiklik yapma
#liste[1:4]="velinin_babası","ahmetin_babası","memonun_babası"
#print(liste)#şeklindeki uygulamada çoklu değişiklik yapmış olduk
#listeye elaman ekleme
#liste=["ali","veli","ahmet","memo"]
#liste= liste +["kemal tahir"]
#print(liste)#listeye kemal tahir eklenmmiş oldu

# Listeden beri silmek
#liste=["ali","veli","ahmet","memo"]
#del liste[3]
#print(liste)#şeklinde uygulanır


# Liste metodları-listeler
#append listeleye eleman ekler .append
#liste metodları kalıcı değişiklik yapabilir
#remove listeden elaman siler
#liste=["ali","veli","ahmet","memo"]
#dir(liste)
#liste.append("mami")
#liste#"mami" ekler
#liste.remove("mami")
#liste#"mami siler

#listenin içinden istediğimiz indekse eleman ekleme
#insert metodu .insert(indeks sayısı)

#liste=["ali","veli","ahmet","memo"]
#liste
#liste.insert(1,"ganyotcu")
#liste #birinci indekse ganyotcu eklemiş olduk
#sona eklleme
#liste=["ali","veli","ahmet","memo"]
#liste
#len(liste)#indeks sayısını buldum şimdide insert içine yazabilirim

#liste.insert(5,"cuguli")#veya
# liste.insert(len(liste),"cuguli")
#liste
#listeden indeks silme pop metodu
#.pop
#liste=["ali","veli","ahmet","memo"]
#liste
#liste.pop(0)
#liste#"ali" gitti 

#COUNT METODU .count()
#indekslerin liste içinde kaç kere geçtiğini verir
#örnek
#liste=["ali","veli","ahmet","memo","ali"]
#liste
#liste.count("ali")#şeklinde utgulanır 2 çıktısını alırız

#COPY METODU .copy()
#elimizdeki mevcut listeyi korumak kopyalamak için kullanılır
#liste=["ali","veli","ahmet","memo","ali"]
#liste
#liste_yedek=liste.copy()#böylelikle listeyi kopyalamış olduk 
#liste_yedek elimizde kalacak istediğimizde ulaşırız

#EXTEND METODU .extend
#iki listeyi birliştirmek için kullanılıyor
#liste=["ali","veli","ahmet","memo","ali"]
#liste
#liste.extend([10,20])
#liste#şeklinde iki listeyi birleştirmiş olduk

#Bir elemanın hangi indeks de oldugunu bulma
#İNDEX METODU
#liste=["ali","veli","ahmet","memo","ali"]
#liste
#liste.index("ahmet")#şeklinde vermektedir

#REVERSE METODU
#LİSTEDİNİN elemanlarını tersine çevirir
#liste=["ali","veli","ahmet","memo","ali"]
#liste
#liste.reverse()
#liste#şeklinde uygulanır

#SORT metodu
#sıralama yapmak için kullanılır
#liste=[10,65,50,42,65]
#liste
#liste.sort()
#liste# listeyi küçükten büyüge sıralamış olduk

#clear metodu
#clear bütün listeyi siler .clear
#liste.clear()
#liste #liste sıfırlandır

#ders 4
#VERİ YAPILARI- TUPLE(LİSTELERİN AKSİNE DEĞİŞTİRİLEMEZ)
#TUPLE PARANTEZ İLE OLUŞTURULUR
#KAPSAYICI,SIRALI VE DEĞİŞTİRİLEMEZ
#ÖRNEK
#t=("ALİ","veli",5,6)#veya tuple() şeklindede oluşturulabilir
#içinde listede barındırabilir farklı tipleri içerir tuple(demet)

#tuple eleman işlemler
#tuple daki elemanlara erişme
#t=("ali","velii",1,6,5,)
#t
#t[0:3]#şekildeki gibi olur
#indeks değiştirme işlemi yapamayız
#aşagıdaki örnek çalışmaz!!!
#t=("ali","velii",1,6,5,)
#t
#[3]=9999
#tuple larda hiçbirşeyi değiştirmek istemiyorsak kullanmamız gerekir


#SÖZLÜK YAPILARI(DİCTİONARY)
#KAPSAYICIDIR,SIRASIZDIR VE DEĞİŞTİRİLEBİLİRDİR
#ANAHTAR İFADELERİN BİR ARADA TUTULDUĞU VERİ YAPISIDIR
#ÖRNEK
#sozluk = {"reg":"regresyon modeli",
#          "loj":"lojistik regresyon",
#          "cart":"cassification and reg"}
#sozluk #şeklinde kullanılır. sağ tarafa int olabilir

#sozluk = {"reg":["regresyon modeli",10],
#          "loj":["lojistik regresyon",50],
#          "cart":["cassification and reg",20]}
#sozluk # bu şekilde içerisinde liste barındırabilir



#Sözlük eleman işlemleri
#sıralı olmadığı içinden indeks seçemeyiz
#sozluk = {"reg":"regresyon modeli",
 #         "loj":"lojistik regresyon",
#          "cart":"cassification and reg"}
#sozluk["reg"]#bu şekilde anaktar kelimelerin anlamalrına ulaşabillriz
 
#iç içe geçmiş sözlük yapılarından eleman seçmek
#sozluk[][]#iki köşeli parantez kullanılarak seçilir

#SÖZLÜK ELEMAN EKLEME-DEĞİŞTİRME
#SÖZLÜKLERDE KEY LER ANAHTARLAR SABİT VERİ YAPILARI OLMALIDIR STRİNG İNTECER GİBİ
#örnek

sozluk={"a":"adem",
        "b":"badem",
        "c":"ceyda"}
#elaman ekleme
#sozluk["d"]="derya"
#sozluk
#eleman değiştirme
#sozluk["a"]="ali"
#sozluk

#SETLER (KÜMELER)
#SIRASIZDIR, DEĞERLERİ SABİTTİR,DEĞİŞİR VE FARKLI TİPLER BARINDIRABİLİR
#HIZ İSTEDİĞMİZDE KULLANILABİLİR
#SET OLUŞTURMA

#liste= ["a","b",5,6,5,6,5,6,"a"]
#liste
#s=set(liste)
#print(s)#çıktı olarak tekrar eden ifadeleri yok eder setler
#setler sırasız olduğu için sıralama yoktur


#SETLERE ELEMAN EKLEME-ÇIKARMA

# l = ["geleceği","yazanlar"]

#s = set(l)
#ekleme
#s.add("yazmayanlar")
#s    #görüleceği üzere rast gele ekler
#çıkarma
#s.remove("yazanlar")
#s
#discard fonksiyonu varsa siler yoksa hata vermez önemlidir işe yarar
#.discard şeklinde kullanılır

# SETLER İÇİNDE İŞLEMLER
# difference
# set1=set([1,3,5])
# set2=set([1,2,6])
# set1.difference(set2)#çıktısı3,5 olur
# set2.difference(set1)#çıktısı 2,6 olur
#bu şekilde farklılıkları incelyebiliriz 
#SYMMETRİC_DİFFERENCE SİMETRİK FARKI ALIR 

#SETLERDE KEŞİŞİM-BİRLEŞİM
#İNTERSECTİON-UNİON
# set1=set([1,2,3])
# set2=set([3,2,6])
# set1.intersection(set2) kesisim bu şekilde
#birleşim
#set1=set([1,2,3])
#set2=set([3,2,6])
#set1.union(set2) #birleşim işlemi yapmış olduk

# SETLER SORGU İŞLEMLERİ
set1= set([1,2,3])
set2= set([1,2,5,3,6,5])
#isdisjoint iki kümenin boş olup olmadığını sorgular
#issubset bir kumenin butun elemanlarının başka kümede yer alıp almadığını söyler
#issuperset  bir kümenin diğer kumeyi kapsayıp kasmadığını söyler
#

# ders5
#FONKSİYONLARA GİRİŞ VE FONKSİYON OKURYAZARLIĞI
#FONKSİYON NASIL YAZILIR
# DEF İFADESİYLE FONKSŞYON TANIMLANIR
# def girildikten sonra bizden bir isim ister
#o isim fonksiyon ismi olur
#o fonksiyonla yapmak istediklerimizi
#alt satırda devam ettiririz
#fonksiyon arkada çalışır ekrena vermek istersek print gerekir
#fonksyonu kullanmak istersek return ifadesibi kullanmamız gerekmektedir
#örnek
# =============================================================================
# def kare_al(x):
#     print(x**2)
#     
# kare_al(4)
# 
# =============================================================================

# BİLGİ NOTUYLA ÇIKTI ÜRETMEK

# =============================================================================
# def kare_al(x):
#     print("SAYININ KARESİ",x**2)
#      
# kare_al(4)
# 
# def kare_al(x):
#     print("SAYININ KARESİ",x**2)
#     print("girilen sayı"+str(x))
# kare_al(4)
# =============================================================================

#İKİ ARGÜMANLI FONKSİYON TANIMLAMAK

# =============================================================================
# def carpma_yap(x,y):
#     print("işlemin sonucu",x*y)
# 
# carpma_yap(5,6)
# 
# =============================================================================

#NE ZAMAN FONKSİYON YAZARIZ
#TEKRAR EDEN GÖREVLERİ YERİNE GETİRİR


#RETURN FONKSİYON ÇIKTILARINI GİRDİ OLARAK KULLANMAK

# =============================================================================
# def hesap(x,y,z):
#     print((x+y)/z)
#     
# hesap(5,9,7)
# =============================================================================

# =============================================================================
# def hesap(x,y,z):
#     return ((x+y)/z)
#     
# sonuc=hesap(5,9,7)
# print(sonuc*9)
# 
# =============================================================================

#LOCAL VE GLOBAL DEĞİŞKENLER
#BİZİM TANIMLAMIŞ OLDUĞUMUZ DEĞİİŞKENLER GLOBAL DEĞİŞKENLERDİR
#FONKSŞYON İÇİNDE OLANLARDA LOCAL DEĞİŞKENLERDİR

#ders 6
#İF fonksiyonu
# eğer çevirisiyle aynı yeri tutar
# şöyleyse bölye yap böyleyse şöyle yap
# =============================================================================
# sınır=50000
# gelir =40000
# if gelir<sınır:
    # print("gelir sınırdan küçük")
# =============================================================================
# gelir sınırdan küçük oldğı-uğu için 
#true yannıtını aldı ve printi ekrana yazdırdı

# =============================================================================
# sınır=50000
# gelir =40000
# if gelir<sınır:
#     print("gelir sınırdan küçük")
#     print(gelir*2)#☻şeklindede kullanılabilir
#     
# =============================================================================


# =============================================================================
# sınır=50000
# gelir =6000000
# if gelir<sınır:
#     print("gelir sınırdan küçük")#♠true gelmez ise çalışmaz
#     
# =============================================================================
    
# ELSE fonksiyonu
# if in alt kümesi gibidir 
#şöyle değilse böyle yap
#örnek


# =============================================================================
# sınır=50000
# gelir =40000
# if gelir<sınır:
#     print("gelir sınırdan küçük")
# else:
#     print("gelir sınırdan büyüktür")
# #göründüğü gibi ihtimal else yi kapsadığı için else çallışır
# 
# 
# =============================================================================

# diğer örnek


# =============================================================================
# # sınır=50000
# # gelir =40000
# # if gelir==sınır:
# #     print("gelir sınırdan küçük")
# # else:
# #     print("gelir sınıra eşit değildir")
# 
# 
# =============================================================================


# ELİF FONKSİYONU
# BİRDEN FAZLA KOŞUL KULLANMAK İÇİN KULLANILIR


# =============================================================================
# sınır=50000
# gelir1 =60000
# gelir2= 50000
# gelir3=35000
# 
# if gelir2>sınır:
#     print("tebrikler")
# elif gelir2<sınır:
#     print("uyarı")
# else:
#     print("takibe devam")
#     
# göründüğü gibiüç koşullu ihimal yapmış olduk
# =============================================================================


# =============================================================================
# sınır=50000
# magaza_adı=input("mağaza adı nedir? ")
# gelir=int(input("mağaza gelirinizi giriniz: "))
# 
# if gelir>sınır:
#     print("tebrikler ")
# elif gelir<sınır:
#     print( "tebrikler değil")
# else:
#     print("takibe devam")
# 
# =============================================================================

# sınır=50000
# magaza_adı="m.can"
# gelir=40000

# if gelir>sınır:
#     print("tebrikler ")
# elif gelir<sınır:
#     print( "tebrikler değil")
# else:
#     print("takibe devam")

#Döngüler 
#FOR döngüsü
# =============================================================================
# 
# ogrenci=["ali","veli","ayşe","berk"]
# 
# for i in ogrenci:
#     print(i)
# #bütün elemanları gezdi i geçiçi değişkeni bütün elemanları geziyor
# 
# =============================================================================

# for döngüsü örnek
#maas 3000 den küçük ise yüzde on
# büyük ise yüzde elli zam yap

# =============================================================================
# 
# maaslar=[1000,2000,30000,
#          5000026,65489,65478]
# 
# for i in maaslar:
#     if i<3000:
#         i=i+i*(10/100)
#         print(int(i))
#     else:
#         i=i+i*(50/100)
#         print(int(i))
# 
# =============================================================================

#Döngüler ile fonksiyonlarkı birlikte kullanmak

#maaşlara yüzde yirmi zam yapılacak
#gereken kodu def ile yaz

# =============================================================================
# 
# maaslar=[1000,2000,3000,4000,5000]
# 
# def yeni_maas(x,y=100):
#     for i in maaslar:
#         i=i+i*x/y
#         print(int(i))
# yeni_maas(20)
#         
# =============================================================================
    
# İF,FOR VE FONKSİYONLARI BİRLİKTE KULLANIMI
#maaşı 3000tl üstü olana yüzde 10
#3000tl altı olana yuzde 30 zam
#3000 olana yüzde 20 zam yapılacak 

# =============================================================================
# maaslar=[1000,2000,3000,4000,5000]
# 
# def yenı_maaslar(x,y,z,k=100):
#     for i in maaslar:
#         if i<3000:
#             i=i+i*x/k
#             print(i)
#         elif i>3000:
#             i=i+i*y/k
#             print(i)
#         else:
#             i=i+i*z/k
#             print(i)
# 
# yenı_maaslar(30,10,20)
# =============================================================================

#DİĞER ÖRNEK
# =============================================================================
# 
# maaslar=[1000,2000,3000,4000,5000] 
# 
# def maas_ust(x):
#     print(x*10/100+x)
#     
# def maas_alt(x):
#     print(x*20/100+x)
# 
# for i in maaslar:
#     if i >= 3000:
#         maas_ust(i)
#     else:
#         maas_alt(i)
# 
# 
# =============================================================================

# ders7
#Nesneye yönelik programlama
#sınıf nedir
#benzer özellikler taşıyan gruplamak için kullanılır
# class şeeklinde kullanılır

# =============================================================================
# class veri_bilimce():
    # şeklinde kulllanılır
#     print("bu bir sınıftır")
# =============================================================================

# =============================================================================
# #sınıf özellikleri
# 
# class veribilimci():
#     bolum=""
#     sql="evet"
#     deneyım_yılı=0
#     bildiği_dşller= []
# #class yapısının altındaki kısım sınıfın özellikleri
# veribilimci.sql
# veribilimci.deneyım_yılı
# 
# # sınıfların özezlliklerini değiştirmek
# veribilimci.sql="hayir"
# a=veribilimci.sql
# print(a) #sql bilgisini değiştirdim
#  
#  
# 
# =============================================================================

# =============================================================================
# class veribilimci:
#     sql="hayır"
#     bolum="matematik"
#     diller=[]
# 
# ali= veribilimci()
# 
# print(ali.sql,"," ,ali.bolum)
# 
# 
# =============================================================================

# =============================================================================
# #örnek özellikleri
# class veribilimci():
#     def __init__(self):
#         self.bildiiği_diller=[]
#         self.bolum=""
#         self.tecrube=0
# 
# ali=veribilimci()
# ali.bildiiği_diller.append("pythonn,java,c")
# print(ali.bildiiği_diller)
# veli=veribilimci()
# veli.bildiiği_diller.append("R")
# print(veli.bildiiği_diller)
# # eğer self kullanmadan sınınf özelliüğü değiştirirsek
# # değişiklik kalıcı olacaktır bunun yerine
# # def __init__(self) kullanıp özellikleri örnek oolarak veriyoruz
# 
# =============================================================================


#örnek metodları
#örnekler üzerinde çalışan fonksiyonlar
#burada ne yaptık
#veri bilimci sınıfını oluşturduk
#özelliklerini yazdık yani calısanlara
#sonra örnekler yazdık bildiği diller gibi
#ardından dil ekleyen bir fonksşyon yazdık işimiz kolay olsun diye
#bu fonksiyonuda kullanarak dil ekleme işini kolaylaştırdık
# =============================================================================
# 
# class veribilimci():
#     calısanlar=[]
#     def __init__(self):
#         self.bildiiği_diller=[]
#         self.bolum=""
#     def dil_ekle(self,yeni_dil):
#         self.bildiiği_diller.append(yeni_dil)
#         
# ali=veribilimci()
# veli=veribilimci()
# 
# ali.dil_ekle("R")
# veli.dil_ekle("python")
# 
# print(ali.bildiiği_diller)
# print(veli.bildiiği_diller)
# =============================================================================

#Miras yapıları
#önceki classın özelliklerini miras olarak kullanma
#önceki kılasları kullanarak class oluşturmak gibi
#örnek
#görüldüğü üzere employes sınıfını miras olarak öbürlerine gönderdik
#diğer sınıflar employes sınıfının özelliklerinide almış oldu buda çok iişimize yaradı
# =============================================================================
# 
# class employees():
#     def __init__(self):
#         self.firstname=""
#         self.lastname=""
#         self.addres=""
# 
# class dataScienstist(employees):
#     def __init__(self):
#         self.programming=""
# 
# class marketing(employees):
#     def __init__(self):
#        self.storyTelling
# 
# data1=dataScienstist()
# mar1=marketing()
# =============================================================================















