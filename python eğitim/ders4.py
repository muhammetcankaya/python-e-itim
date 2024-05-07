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














































































































