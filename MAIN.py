import recipe_pooper
import json

url = "http://thepioneerwoman.com/cooking/ultimate-grilled-cheese-sandwich/"
dish = recipe_pooper.poop(url)

'''----------------------------------------------------------------------------'''
t = "title"
i = "ingredients"
r = "recipe"
c = "cooktime"
p = "preptime"
d = "difficulty"
s = "serving"
'''----------------------------------------------------------------------------'''


jsn = json.dumps(dish)
with open("poop.json" , "w") as f:
    json.dump(dish , f)
f.close()

ex_poop = json.load(open("poop.json"))
print(ex_poop[c])


'''
dish = {title , ingredients , recipe , cookTime , preptime , difficulty , serving}
'''

'''test inputs
http://thepioneerwoman.com/cooking/ultimate-grilled-cheese-sandwich/
http://thepioneerwoman.com/cooking/easter-leftover-sandwich/
'''