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



































































































































