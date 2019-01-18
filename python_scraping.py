from bs4 import BeautifulSoup
import requests 
import re
url = "https://www.filmweb.pl/film/Narodziny+gwiazdy-2018-542576"


soup = BeautifulSoup(requests.get(url).text, features="html.parser")
print((soup.find("td").next_element).find("a").contents)                    #director
print((soup.find("table").find("span").contents))                           #premiere date
print(soup.find(string=re.compile("boxoffice")).next_element.contents)      #boxoffice  
print(soup.find("span", itemprop="ratingValue").contents)                   #rate    











######### tools and workshop



#<span itemprop="ratingValue"> 7,8<


#<div class="filmVoteRatingPanelWrapper"><div class="ratingInfo">
    #<div class="boxContainer va-middle no-margin">
       # <div class="box nowrap">
            #        <i class="ic-star_solid primary vertical-align"></i>
           #         <span class="vertical-align light ratingRateValue"><span>7,8</span></span>
      #  </div>

       # <div class="box full-width text-right communityRateInfo">
        #    <div class="communityRateInfoWrapper">58 848 głosów<br>36 327 chce zobaczyć
         #   </div>
        #</div>
    #</div>









#<span class="vertical-align light ratingRateValue"><span>7,8</span></span>




#print(soup.find(class_=re.compile("<div class="box nowrap">)))






#print(soup.find(string=re.compile("<span class="vertical-align light ratingRateValue">")).next_element.contents)


#print(soup.find("class="vertical-align light ratingRateValue"").next_element.contents)








#def has_class(tag):
 #   return tag.has_attr('class_="filmInfo bottom-15"')
    
#print(soup.find_all(has_class('class_="filmInfo bottom-15"')))




#import re
#soup.find(string=re.compile("<div class="filmInfo bottom-15">"))


#import re
#for tag in soup.find_all(re.compile("^tbody")):
 #   print(tag.name)








#<th>boxoffice:</th>







#<a href="/film/Narodziny+gwiazdy-2018-542576/dates"> <span> 30 listopada 2018 </span> (Polska) <span> 31 sierpnia 2018 </span> (świat) </a>





#if __name__ == "__main__":
#    main()

#<li itemprop="director" itemscope="" itemtype="http://schema.org/Person"><a href="/person/Bradley+Cooper-57074" title="Bradley Cooper" itemprop="name">Bradley Cooper</a></li>

#<a href="/person/Bradley+Cooper-57074" title="Bradley Cooper" itemprop="name">Bradley Cooper</a>


#soup.find_all("p")
#soup.find("p")
#soup.find(class_="tabela")
#next_element
#next_sibling