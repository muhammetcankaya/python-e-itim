import re
import time
#Şimdi bir ögrenci kayıt etme ve ögrenci kayıt silme uygulaması
#her bir ögrencinin isim soy isim boy kilo ve tc lerini alacağız
#bunları siteme yazdıracağız bunu yaparken baya dikkatli olcağız

class ÖgrenciKayıt:
    def __init__(self):
        self.dongu=True
        self.program()
    def program(self):
        secim=self.menu()
        if secim=="1":
            self.kayıtoku()
        if secim=="2":
            self.kayıtekle()
        if secim=="3":
            self.kayıtsil()
        if secim=="4":
            self.cıkıs()    
    def menu(self):
        def kontrol(secim):
            if not re.search("[1-4]",secim):
                raise Exception("istenilen sayıları giriniz")
            elif len(secim)!=1:
                raise Exception("istenilen sayıları giriniz")
        while True:
            try:
                secim=input("Öğrenci veri tabanına HOŞGELDİNİZ\n[1] Verileri oku\n[2] Öğrenci kayıt\n[3] Öğrenci sil\n[4] Çıkış\n")
                kontrol(secim)
            except Exception as hata:
                print(hata)
            else:
                return secim
                break
        self.program()
    def kayıtekle(self):
        def ögrenciad():
            def kontrolad(ad):
                if ad.isalpha()==False:
                    raise Exception("İsminiz harflerden oluşmalıdır")
                elif len(ad)>25:
                    raise Exception("İsminiz 25 karakterden büyük olamaz")
            while True:
                try:
                    ad=input("Öğrenci adını giriniz: ")
                    kontrolad(ad)
                except Exception as hataad:
                    print(hataad)
                else:
                    return ad
                    break                                  
        def ögrencisoyad():
            def kontrolsoyad(soyad):
                if soyad.isalpha()==False:
                    raise Exception("soyad harflerden oluşmalıdır")
                elif len(soyad)>25:
                    raise Exception("soyad 25 karakterden büyük olamaz")
            while True:
                try:
                    soyad=input("Öğrenci soyad giriniz: ")
                    kontrolsoyad(soyad)
                except Exception as hatasoyad:
                    print(hatasoyad)
                else:
                    return soyad
                    break
        def ögrenciboy():
            def kontrolboy(boy):
                if boy.isdigit()==False:
                    raise Exception("Öğrenci boyunu sayılar ile giriniz")
                elif len(boy)!=3:
                    raise Exception("boyusunuz 3 karakterden büyük olamaz")
            while True:
                try:
                    boy=input("Öğrenci boy giriniz: ")
                    kontrolboy(boy)
                except Exception as boy:
                    print(boy)
                else:
                    return boy
                    break
        def ögrencikilo():
            def kontrolkilo(kilo):
                if kilo.isdigit()==False:
                    raise Exception("Öğrenci boyunu sayılar ile giriniz")
                elif not (int(kilo)>40 and int(kilo)<200):
                    raise Exception("Bu kiloda insan olmaz")
            while True:
                try:
                    kilo=input("Öğrenci kilo giriniz: ")
                    kontrolkilo(kilo)
                except Exception as kilo:
                    print(kilo)
                else:
                    return kilo
                    break
        def velinumara():
            def kontrolnumara(numara):
                if not re.search("[0-9]",numara):
                    raise Exception("Numarada harf olmaz")
                elif len(numara)!=11:
                    raise Exception("Numara 11 haneli olmalı")
                elif numara.startswith("0")==False:
                    raise Exception("Numara 0 la başlar.")
            while True:
                try:
                    numara=input("Veli numarası gir:")
                    kontrolnumara(numara)
                except Exception as hatanumber:
                    print(hatanumber)
                else:
                    return numara
                    break
        a=ögrenciad()
        b=ögrencisoyad()
        c=ögrenciboy()
        d=ögrencikilo()
        e=velinumara()
        with open("ögrencidata.txt","r",encoding="utf-8") as dosya:
            liste=dosya.readlines()
            id=len(liste)+1
        with open("ögrencidata.txt","+a",encoding="utf-8") as dosya1:
            dosya1.write(f"{id} {a} {b} {c} {d} {e}\n")
        self.menudon()
    def kayıtsil(self):
        def kontrolsil(idsil,liste):
            if idsil>len(liste):
                raise Exception("Bu id ye ait kullanıcı yoktur")            
        with open("ögrencidata.txt","r",encoding="utf-8") as dosya:
            liste=dosya.readlines()
            liste1=[]
            while True:
                try:
                    idsil=int(input("Kaydının silinmesini istediğiniz öğrencinin id'siniz"))-1
                    kontrolsil(idsil,liste)
                except Exception as hata:
                    print(hata)
                else:
                    break
            del liste[idsil]
            for i in range(0,idsil):
                liste1.append(liste[i])
            for i in range(idsil,len(liste)):
                if liste[i][0:2].isdigit()==False:
                    a=int(liste[i][0:2][0])-1                    
                    k=liste[i].split(" ")
                    k[0]=str(a)
                    liste1.append(" ".join(k))
                elif liste[i][0:2].isdigit()==True:
                    a=int(liste[i][0:2])-1
                    k=liste[i].split(" ")
                    k[0]=str(a)
                    liste1.append(" ".join(k))
        with open("ögrencidata.txt","w",encoding="utf-8") as dosya:
            for i in liste1:
                dosya.write(i)
        self.menudon()
    def kayıtoku(self):
        with open("ögrencidata.txt","r",encoding="utf-8") as dosyaoku:  
            print(dosyaoku.read())
        self.menudon()
    def menudon(self):
        a=input("[1] Ana menüye dön\n[2] Çıkış\n")
        if a=="1":
            self.program()
        elif a=="2":
            self.cıkıs()
        else:
            print("YETEEEER")
    def cıkıs(self):
        self.dongu=False       
dongu=ÖgrenciKayıt()
while dongu.dongu:
    dongu.program()

                

    