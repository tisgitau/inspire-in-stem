

import requests
from bs4 import BeautifulSoup as bs
user_name = "tisgitau" 
url = "https://github.com" +user_name #input("Enter site url")
results = requests.get(url)

soup = bs(results.content, "html.parser")
profile_pic = soup.find("img", {'alt':'Avatar'})
print(profile_pic)
