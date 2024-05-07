#Bu kısımda İMDB nin bizimle ücretsiz paylaşdığı APİ sayesinden en iyi 
#250 film dizi veya film vb. bilgilere ulaşabilileceğiz 
#Bu projede requests yapısı json yapısını aktif olarak kullanıp son kez bu konuları tekrar etmiş olacağız
#Uzun ve meşakatli bu yolda bizimle birlikte ögrenme sürecine devam ettiğin için teşekkürler CANKAYA 
import requests
import json
import time
import textwrap
class İMBD:
    def __init__(self):
        self.dongu=True
    def menu(self):
        secim=input("HOŞGELDİNİZ\n[1]En iyi 250 film \n[2]En iyi 250 dizi\n[3]Sinemalarda\n[4]Film hakkında bilgi almak\n[5]Çıkmak için\n")
        if secim=="1":
            self.film250()
        elif secim=="2":
            self.dizi250()
        elif secim=="3":
            self.sinemalarda()
        elif secim=="4":
            self.filmbilgi()
        elif secim=="5":
            self.cıkıs()
        else:
            print("lütfen istenilen ifade dışında bir şey girmeyiniz")

    def film250(self):
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/Top250Movies/k_rec2yfmc")
        site=url.json()
        for i in site["items"]:
            değişken=i["rank"]+" "+i["title"]
            print(değişken)
    def dizi250(self):
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/Top250TVs/k_rec2yfmc")
        site=url.json()
        for i in site["items"]:
            değişken=i["rank"]+" "+ i["fullTitle"]
            print(değişken)
    def sinemalarda(self):
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/ComingSoon/k_rec2yfmc")
        site=url.json()
        for i in site["items"]:
            değişken=i["title"]+" "+i["releaseState"]
            print((değişken))
    def filmbilgi(self):
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/Top250Movies/k_rec2yfmc")
        site=url.json()
        AD=list()
        İD=list()
        for i in site["items"]:
            AD.append(i["title"])
            İD.append(i["id"])
        film=input("Araştırmak istediğiniz filmi giriniz:")
        değişken=dict(zip(AD,İD))
        try:
            url=requests.get("https://imdb-api.com/tr/API/Wikipedia/k_rec2yfmc/"+değişken[film])
            bilgi=url.json()
            print(textwrap.fill(bilgi["plotShort"]["plainText"]))
        except KeyError:
            print("gecerli ifade giriniz")


    def cıkıs(self):
        self.dongu=False

imdb=İMBD()
while imdb.dongu:
    time.sleep(3)
    imdb.menu()