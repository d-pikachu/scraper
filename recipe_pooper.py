import urllib.request
from bs4 import BeautifulSoup
import t_p_w

def poop(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page , "html.parser")

    recipe = "ERROR"
    if "thepioneerwoman.com" in url:
        recipe = t_p_w.get_recipe(soup)
        
    return recipe