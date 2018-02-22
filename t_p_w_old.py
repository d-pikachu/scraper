'''THE PIONEER WOMEN'''

'''TITLE'''
title = soup.title.string.replace("| The Pioneer Woman" , "")


'''INGREDIENTS'''
ingredients = {}
ings = soup.find(attrs = {"class":"list-ingredients"})
for i in ings.find_all("li"):
    item = i.find(attrs = {"itemprop":"name"}).get_text()
    amt = i.find(attrs = {"itemprop":"amount"}).get_text()
    ingredients[item] = amt


'''RECIPE'''
for i in soup.find_all("div" , {"role":"tabpanel"}):
    if i.has_attr("id") and "recipe-instructions" in i["id"]:
        recipe = i.find("div" , {"class" : "panel-body"}).get_text()
        break

recipe = recipe.replace(".)",").")
recipe = recipe.replace("\t","")
recipe = recipe.replace("\n","")
recipe = recipe.split(".")

for i , step in enumerate(recipe):
    recipe[i] = step.strip()+"."
    if recipe[i] == ".":
        recipe.pop(i)

'''RECIPE SUMMARY'''
summ = soup.find(attrs={"class":"recipe-summary-time"})
cookTime = "Not available"
preptime = "Not available"
difficulty = "Not available"
serving = "Not available"

for s in summ.find_all("dl"):
    data = s.find("dt").string.strip()
    value = s.find("dd").string.strip()
    if "Cook" in data:
        cookTime = value
    elif "Prep" in data:
        preptime = value
    elif "Difficulty" in data:
        difficulty = value
    elif "Servings" in data:
        serving = value

'''test inputs
http://thepioneerwoman.com/cooking/ultimate-grilled-cheese-sandwich/
http://thepioneerwoman.com/cooking/easter-leftover-sandwich/
'''

print("dish - " + title)
#print(ingredients)
print("step 1  - " + recipe[0])
print("preptime - " + preptime)
print("cooktime - " + cookTime)
print("difficulty - " + difficulty)
print("serving - " + serving)
