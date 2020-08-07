import sqlite3


raw_text = ""
ing_start = 0
dir_start = 0
type_start = 0
prep_start = 0
cook_start = 0
serve_start = 0

ing_list = []
dir_list = []
recipe = {}
ingredients = {}

def qty_to_num(string)-> float: 
    if "/" in string:
        slash = string.index("/")
        numerator = int(string[:slash])
        denominator = int(string[slash+1:])
        num = numerator / denominator
    else:
        num = float(string)
    
    return num


##### Pull in raw text from formatted file #####
with open("/Users/adamzadnik/Documents/Recipes/Exports from Notes/chickpea_salad_raw.txt","r") as f:
    raw_text = f.read()

split_text = raw_text.split("\n")

# Determine starting points for each recipe section
title = split_text[0]

for x in range(len(split_text)):
    if 'ingredients:' in split_text[x].lower():
        #print(f"Found ingredient at index {x}")
        ing_start = x
    elif 'directions:' in split_text[x].lower():
        #print(f"Found directions at index {x}")
        dir_start = x
    elif 'type:' in split_text[x].lower():
        #print(f"Found type at index {x}")
        type_start = x
    elif 'prep time:' in split_text[x].lower():
        #print(f"Found prep time at index {x}")
        prep_start = x
    elif 'cook time:' in split_text[x].lower():
        #print(f"Found cook time at index {x}")
        cook_start = x
    elif 'servings:' in split_text[x].lower():
        #print(f"Found servings at index {x}")
        servings_start = x



##### RECIPE TYPE #####
rec_type = split_text[type_start][6:]
# TODO - lookup for recipe types

##### PREP TIME #####
prep = split_text[prep_start][11:]
if prep == "N/A":
    prep = 0.0


##### COOK TIME #####
cook = split_text[cook_start][11:]
if cook == "N/A":
    cook = 0.0


##### SERVINGS #####
servings = float(split_text[servings_start][10:])


##### INGREDIENTS #####
ing_list = split_text[ing_start+1:dir_start-1]
ing_list = [x.replace('* ','') for x in ing_list]
ing_list = [x.split(" ") for x in ing_list]

for y in ing_list:

    ing_temp = " ".join(y[2:])
    del y[3:]

    try:
        style_start = ing_temp.index(",")
        y[2] = ing_temp[:style_start].lower()
        y.append(ing_temp[style_start+2:].lower())
    except ValueError:
        y[2] = ing_temp.lower()
        y.append("")

    ingredients[y[2]] = {"qty" : qty_to_num(y[0]), "measure" : y[1].lower(), "style" : y[3]}


##### DIRECTIONS #####
dir_list = [x.replace('* ','') for x in split_text[dir_start+1:]]
directions = "\n\n".join(dir_list)



##### ASSEMBLE RECIPE #####
recipe = {
    "Title" : title,
    "Recipe_Type" : rec_type,
    "Prep_Time" : prep,
    "Cook_Time" : cook,
    "Servings" : servings,
    "Ingredients" : ingredients,
    "Directions" : directions,
}


##### DATABASE #####

db = sqlite3.connect('/Users/adamzadnik/Desktop/Development/django/recipeapp/db.sqlite3')
cursor = db.cursor()

# Check for existence of recipe to be added
cursor.execute('''SELECT id FROM recipe_store_recipe WHERE name=?''', (recipe["Title"],))
recipe_id = cursor.fetchone()

if recipe_id:
    print("Recipe already exists")
else:
    cursor.execute('''INSERT INTO recipe_store_recipe(name, type, servings, prep_time, cook_time, directions) VALUES(?,?,?,?,?,?)''', (recipe["Title"], recipe["Recipe_Type"], recipe["Servings"], recipe["Prep_Time"], recipe["Cook_Time"], recipe["Directions"]))
    recipe_id = cursor.lastrowid
    print("Recipe added to Recipe table")

    # FOR EACH INGREDIENT
    # 1. search for the name in the ingredients table
    #   a. If the name exists, get the ID
    #   b. If the name does not exist, add the name to the Ingredients table
    # 2. Save the ingredient ID, QTY, measurement, and recipe ID to the recipeingredient table

    for a in recipe["Ingredients"]:
        
        cursor.execute('''SELECT id FROM recipe_store_ingredient WHERE name=?''', (a,))
        ing_id = cursor.fetchone()
        
        if not ing_id:
            print(f"{a} not found, adding to recipe_store_ingredient table")
            cursor.execute('''INSERT INTO recipe_store_ingredient(name) VALUES(?)''', (a,))
            ing_id = cursor.lastrowid
        else:
            ing_id = ing_id[0]

        cursor.execute('''SELECT id FROM recipe_store_unit WHERE abbreviation=?''', (recipe["Ingredients"][a]["measure"],))
        meas_id = cursor.fetchone()

        meas_id = meas_id[0] if meas_id else 99

        cursor.execute('''INSERT INTO recipe_store_recipeingredient(quantity, ingredient_id, recipe_id, units_id, style) VALUES(?,?,?,?,?)''', (recipe["Ingredients"][a]["qty"], ing_id, recipe_id, meas_id, recipe["Ingredients"][a]["style"]))
        #recipe["Ingredients"][a]["qty"]

db.commit()
db.close()




