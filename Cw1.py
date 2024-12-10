import requests
from bs4 import BeautifulSoup #beautifulsoup4

data = requests.get("https://www.sggw.edu.pl/category/aktualnosci/")

soup = BeautifulSoup(data.text,"html.parser")
#all_links = soup.find_all("a")
#print(len(all_links))
#for link in all_links:
    #print(link.attrs['href']) <- znajduje linki

articles = soup.find_all("article")
with open("output.csv","w") as outputfile:
    for article in articles:
        header = (article.find("h1").text)#znajduje header
        link = (article.find("a").attrs.get("href","-"))
        outputfile.write(
            f"{header};{link}\n"
        )
