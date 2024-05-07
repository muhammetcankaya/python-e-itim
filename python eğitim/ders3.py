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





































































































