from bs4 import BeautifulSoup
import requests 
import re
url = "https://www.filmweb.pl/film/Narodziny+gwiazdy-2018-542576"


soup = BeautifulSoup(requests.get(url).text, features="html.parser")
print((soup.find("td").next_element).find("a").contents)                    #director
print((soup.find("table").find("span").contents))                           #premiere date
print(soup.find(string=re.compile("boxoffice")).next_element.contents)      #boxoffice  
print(soup.find("span", itemprop="ratingValue").contents)                   #rate    











