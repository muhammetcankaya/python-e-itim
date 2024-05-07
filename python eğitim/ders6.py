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























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


































































































































































































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    