#ilk sayfadaki bütün şirket isimlerine ulaşacağız 
#diğer linki gideceğiz ordan finan bilgilerine geçip
import requests
from bs4 import BeautifulSoup
import re
import time
import textwrap
class Borsaistanbul:
    
    def __init__(self):
        self.dongu=True
    
    def program(self):
        secim=self.menu()
        if secim=="1":
            print("Şirket kodları isimleri vb. çağırılıyor...")
            time.sleep(2)
            self.şirketisimleri()
        if secim=="2":
            #time.sleep(2)
            self.şirketfinansveriler()
        if secim=="3":
            print("Çıkıs yapılıyor...")
            time.sleep(2)
            self.cıkıs()
    
    def menu(self):
        
        def kontrol(secim):
            if not re.search("[1-3]",secim):
                raise Exception("Lütfen 1 ve 3 arasında bir sayı giriniz")
            elif (len(secim))!=1:
                raise Exception("Lütfen 1 ve 3 arasında bir sayı giriniz")
        while True:
            try:
                secim=input("[1]Şirket kodları ve isimleri için basınız\n[2]Şirket finans verileri için basınız\n[3]Çıkmak için 3 e basınız\n")
                kontrol(secim)


            except Exception as hata:
                print(hata)
            else:
                break
        return secim
    
    def şirketisimleri(self):
        url=requests.get("https://www.kap.org.tr/tr/bist-sirketler").content
        soup=BeautifulSoup(url,"html.parser")
        şirketler=soup.find_all("div",{"class":"w-clearfix w-inline-block comp-row"})
        for şirket in şirketler:
            a=şirket.find("div",{"class":"comp-cell _04 vtable"}).text
            b=şirket.find("div",{"class":"comp-cell _14 vtable"}).text
            c=şirket.find("div",{"class":"comp-cell _12 vtable"}).text
            d=şirket.find("div",{"class":"comp-cell _11 vtable"}).text

            print(f"KOD\n{a.strip()}\nŞİRKET UNVANİ\n{textwrap.fill(b.strip())}\nŞEHİR\n{textwrap.fill(c.strip())}\nBAĞIMSIZ DENETİM KURULUŞU\n{textwrap.fill(d.strip())}")
        self.menudon()
    
    def şirketfinansveriler(self):
        url=requests.get("https://www.kap.org.tr/tr/bist-sirketler").content
        soup=BeautifulSoup(url,"html.parser")
        şirketler=soup.find_all("div",{"class":"w-clearfix w-inline-block comp-row"})
        aid=list()
        link=list()
        for şirket in şirketler:
            a=şirket.find("div",{"class":"comp-cell _04 vtable"}).text
            b=şirket.find("div",{"class":"comp-cell _04 vtable"}).find("a",{"class":"vcell"}).get("href")
            c="https://www.kap.org.tr/"+b
            aid.append(a.strip())
            link.append(c)
        kaynak=dict(zip(aid,link))
        print(kaynak)
        l=True
        while l:
            try:    
                şirketid=input("Hangi şirketin fianansal verilerine ulaşmak istiyorsanız kısaltma ismini yazınız").upper()
                print("ŞİRKET FİNANS VERİLERİNE ULAŞILIYOR...")
                time.sleep(2)
                print("İŞLEM BİR KAÇ SENİYE SÜREBİLİR\nTABLO BİRAZ KÖTÜ GÖZÜKEBİLİR DÜZELTEMEDİM :(")
                time.sleep(3)
                finanslinki=requests.get(kaynak.get(şirketid)).content
                soup3=BeautifulSoup(finanslinki,"html.parser")
                finansalveri=list(soup3.find("div",{"class":"w-clearfix tab-block"}).children)
                finansaltablolink="https://www.kap.org.tr/"+finansalveri[len(finansalveri)-4].get("href")                
                soup4=BeautifulSoup(requests.get(finansaltablolink).content,"html.parser")  
                tablo=soup4.find("div",{"class":"exportClass"})
                for tabloparca in tablo:
                    x=tabloparca.text.replace("\n","").replace("       ","").split("\n\n")
                    for i in x:
                        print(i.replace("\n",""))
                    
                    
                l=False  
                self.menudon()
            except Exception:
                print("lütfet doğru şirket kısaltması giriniz ")

    def menudon(self):
        secim=input("[4]Ana menüye dönmek için\n[5]Çıkıs yapmak için")
        if secim=="4":
            print("Ana menüye dönülüyor...")
            time.sleep(2)
            self.program()
        elif secim=="5":
            print("Programdan çıkılıyor...")
            time.sleep(2)
            self.cıkıs()
    
    def cıkıs(self):
        self.dongu=False
        exit()



cagırma=Borsaistanbul()
while cagırma.dongu:
    cagırma.program()
