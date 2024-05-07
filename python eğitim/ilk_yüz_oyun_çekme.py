import requests
from bs4 import BeautifulSoup

url=requests.get("https://www.imdb.com/list/ls097840768/")
soup=BeautifulSoup(url.content,"html.parser")
parçalar=soup.find_all("div",{"class":"lister-item mode-detail"})
with open("the_populer_games.txt","w",encoding="utf-8") as file:

    for oyunlar in parçalar:
        oyun_sırası=oyunlar.find("div",{"class":"lister-item-content"}).find("h3").find("span").text
        oyun_ismi=oyunlar.find("div",{"class":"lister-item-content"}).find("h3").find("a").text
        oyun_hikayesi=oyunlar.find("div",{"class":"lister-item-content"}).find("p",{"class":""}).text
        

        file.write(f"{oyun_sırası}{oyun_ismi}")
        file.write(oyun_hikayesi+"\n")

