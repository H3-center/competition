import requests
from bs4 import NavigableString, BeautifulSoup

def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString) and isinstance(tag.previous_element,NavigableString))

req = requests.get("http://www.naver.com")
con = req.content
# soup = BeautifulSoup(con,"html.parser")
soup = BeautifulSoup(con,"html5lib")
# print(soup)
for tag in soup.find_all(surrounded_by_strings):
    print(tag.name)
    print(tag.sourceline,tag.sourcepos)