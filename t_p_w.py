'''THE PIONEER WOMEN'''
def get_recipe(soup):
    dish = {}

    '''TITLE'''
    title = soup.title.string.replace("|", "").replace("The Pioneer Woman","").strip()
    dish["title"] = "-1" if title is None else title


    '''INGREDIENTS'''
    ingredients = {}
    ings = soup.find(attrs = {"class":"list-ingredients"})
    if ings is not None:
        for i in ings.find_all("li"):
                item = i.find(attrs = {"itemprop":"name"}).get_text()
                amt = i.find(attrs = {"itemprop":"amount"}).get_text()
                ingredients[item] = amt

    dish["ingredients"] = ingredients

    '''RECIPE'''
    recipe = None
    for i in soup.find_all("div" , {"role":"tabpanel"}):
            if i.has_attr("id") and "recipe-instructions" in i["id"]:
                recipe = i.find("div" , {"class" : "panel-body"}).get_text()
                break

    if recipe is not None:
        recipe = recipe.replace(".)",").")
        recipe = recipe.replace("\t","")
        recipe = recipe.replace("\n","")
        recipe = recipe.split(".")

        for i , step in enumerate(recipe):
            recipe[i] = step.strip()+"."
            if recipe[i] == ".":
                recipe.pop(i)

    dish["recipe"] = recipe


    '''RECIPE SUMMARY'''
    summ = soup.find(attrs={"class":"recipe-summary-time"})
    cooktime = "Not available"
    preptime = "Not available"
    difficulty = "Not available"
    serving = "Not available"

    if summ is not None:
        for s in summ.find_all("dl"):
            data = s.find("dt").string.strip()
            value = s.find("dd").string.strip()
            if "Cook" in data:
                dish["cooktime"] = value
            elif "Prep" in data:
                dish["preptime"] = value
            elif "Difficulty" in data:
                dish["difficulty"] = value
            elif "Servings" in data:
                dish["serving"] = value


    if dish == {} or ingredients == {} or recipe == None:
        print("ERROR")

    return dish

'''test inputs
http://thepioneerwoman.com/cooking/ultimate-grilled-cheese-sandwich/
http://thepioneerwoman.com/cooking/easter-leftover-sandwich/
'''

'''print("dish - " + title)
#print(ingredients)
print("step 1  - " + recipe[0])
print("preptime - " + preptime)
print("cooktime - " + cookTime)
print("difficulty - " + difficulty)
print("serving - " + serving)'''
