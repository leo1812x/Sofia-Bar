import os
import json
import re
from datetime import datetime

# Base directory for the Obsidian vault
BASE_DIR = "Bar-Management"

# Define the folder structure
FOLDERS = [
    "Cocktails",
    "Batches",
    "Syrups",
    "Infusions",
    "Juices",
    "Spirits",
    "Modifiers",
    "Kegs",
    "Social Drinks",
    "Templates",
    "Production"
]

# Define cocktail recipes from the images
COCKTAILS = [
    {
        "name": "Dream of Zorro",
        "glassware": "Double rocks glass",
        "garnish": "Tamarind mango candy garnish",
        "method": "Shake, dirty dump",
        "ingredients": [
            "2 oz batch",
            "1 oz mango syrup",
            "0.75 oz lime juice"
        ],
        "batch": {
            "ingredients": [
                "3L chili oil tequila",
                "1L genepy"
            ],
            "storage": "Keep refrigerated",
            "shelf_life": "30 days"
        },
        "notes": "NO substitutions of base spirit. If someone wants a different tequila, it will be a spicy mango marg with spicy bitters",
        "tags": ["tequila", "genepy", "mango", "lime", "shaken"]
    },
    {
        "name": "Sofia Old Fashioned",
        "glassware": "Double rocks glass",
        "garnish": "Fattyyyy orange peel",
        "method": "Big rock, stir",
        "ingredients": [
            "2 oz batch",
            "2 dash cardamom bitters",
            "5 dash ango bitters"
        ],
        "batch": {
            "ingredients": [
                "3L bourbon",
                "1L contratto aperitif"
            ],
            "storage": "Room temperature",
            "shelf_life": "90 days"
        },
        "notes": "",
        "tags": ["bourbon", "contratto", "bitters", "stirred"]
    },
    {
        "name": "Sofia Dirty Martini",
        "glassware": "Coupe",
        "garnish": "Cracked pink peppercorn, olive pick",
        "method": "Hard shake, double strain",
        "ingredients": [
            "3 oz batch"
        ],
        "batch": {
            "ingredients": [
                "2L olive oil vodka",
                "750 mL olive brine"
            ],
            "storage": "Keep in freezer",
            "shelf_life": "30 days"
        },
        "notes": "NO substitutions of vodka. Can add more olive brine but no available mods for 'light dirt'",
        "tags": ["vodka", "olive", "freezer", "shaken"]
    },
    {
        "name": "Too Much Romance",
        "glassware": "Coupe glass",
        "garnish": "Tarragon sprig",
        "method": "Shake, strain",
        "ingredients": [
            "2 oz batch",
            "0.75 oz grapefruit cordial",
            "0.5 oz lemon juice",
            "Egg white"
        ],
        "batch": {
            "ingredients": [
                "3L bourbon",
                "1L italicus"
            ],
            "storage": "Room temperature",
            "shelf_life": "90 days"
        },
        "notes": "",
        "tags": ["bourbon", "italicus", "grapefruit", "lemon", "egg_white", "shaken"]
    },
    {
        "name": "Woman from Cocociara",
        "glassware": "Nick and Nora",
        "garnish": "Orchid garnish",
        "method": "Shake, strain",
        "ingredients": [
            "2.25 oz batch",
            "0.75 oz lime",
            "0.5 oz dem"
        ],
        "batch": {
            "ingredients": [
                "1.5L coconut fat washed rum",
                "750 mL cochi americano"
            ],
            "storage": "Refrigerated",
            "shelf_life": "30 days"
        },
        "notes": "NO substitutions!",
        "tags": ["rum", "coconut", "cochi_americano", "lime", "shaken"]
    },
    {
        "name": "Milano Menta",
        "glassware": "Double rocks glass",
        "garnish": "",
        "method": "Build",
        "ingredients": [
            "4 oz batch"
        ],
        "batch": {
            "ingredients": [
                "2.5L vodka",
                "1L contratto aperitif"
            ],
            "storage": "Refrigerated",
            "shelf_life": "30 days"
        },
        "notes": "",
        "tags": ["vodka", "contratto", "built", "keg"]
    },
    {
        "name": "Evening Colombo",
        "glassware": "Double rocks glass",
        "garnish": "",
        "method": "Build",
        "ingredients": [
            "4 oz batch"
        ],
        "batch": {
            "ingredients": [
                "3L tequila",
                "1L pamplemousse"
            ],
            "storage": "Refrigerated",
            "shelf_life": "30 days"
        },
        "notes": "",
        "tags": ["tequila", "pamplemousse", "built", "keg"]
    },
    {
        "name": "Espresso Martini",
        "glassware": "Coupe",
        "garnish": "Coffee beans",
        "method": "Shake, double strain",
        "ingredients": [
            "3L vodka",
            "2L cold brew",
            "1L house amaro",
            "18.5oz coffee liqueur"
        ],
        "batch": {
            "ingredients": [
                "3L vodka",
                "2L cold brew",
                "1L house amaro",
                "18.5oz coffee liqueur"
            ],
            "storage": "Refrigerated",
            "shelf_life": "7 days"
        },
        "notes": "Cold brew must be fresh",
        "tags": ["vodka", "coffee", "cold_brew", "amaro", "shaken"]
    },
    {
        "name": "Espresso - No Vodka",
        "glassware": "Coupe",
        "garnish": "Coffee beans",
        "method": "Shake, double strain",
        "ingredients": [
            "1L cold brew",
            "500mL house amaro",
            "8.25oz coffee liqueur"
        ],
        "batch": {
            "ingredients": [
                "1L cold brew",
                "500mL house amaro",
                "8.25oz coffee liqueur"
            ],
            "storage": "Refrigerated",
            "shelf_life": "7 days"
        },
        "notes": "Non-alcoholic version",
        "tags": ["non_alcoholic", "coffee", "cold_brew", "amaro", "shaken"]
    },
    {
        "name": "Blue Drank",
        "glassware": "Collins",
        "garnish": "",
        "method": "Build, stir",
        "ingredients": [
            "1L tequila",
            "500mL blue curacao",
            "250mL passao"
        ],
        "batch": {
            "ingredients": [
                "1L tequila",
                "500mL blue curacao",
                "250mL passao"
            ],
            "storage": "Refrigerated",
            "shelf_life": "30 days"
        },
        "notes": "",
        "tags": ["tequila", "curacao", "passao", "built"]
    }
]

# Define syrup recipes from the images
SYRUPS = [
    {
        "name": "Simple Syrup",
        "base": "Sugar and water",
        "ingredients": [
            "400g hot water",
            "500g sugar"
        ],
        "method": "Combine, stir until dissolved",
        "yield": "Approximately 900mL",
        "shelf_life": "30 days",
        "storage": "Refrigerated",
        "tags": ["basic", "refrigerated"]
    },
    {
        "name": "Rich Demerara",
        "base": "Brown sugar and water",
        "ingredients": [
            "300g water",
            "600g brown sugar"
        ],
        "method": "Bring to boil on high heat and reduce to medium and simmer for 10-15 minutes",
        "yield": "Approximately 750mL",
        "shelf_life": "30 days",
        "storage": "Refrigerated",
        "tags": ["basic", "refrigerated"]
    },
    {
        "name": "Toasted Cinnamon Syrup",
        "base": "Simple syrup and toasted cinnamon",
        "ingredients": [
            "3-4 Toasted Cinnamon sticks per quart of simple syrup"
        ],
        "method": "Toast cinnamon sticks either in pan on stove or in flat pan in oven. Add toasted cinnamon to simple syrup on stovetop, bring to boil on high heat. Reduce heat to medium and let simmer for 10-15 minutes",
        "yield": "Approximately 1 quart",
        "shelf_life": "30 days",
        "storage": "Refrigerated",
        "tags": ["flavored", "refrigerated", "cinnamon"]
    },
    {
        "name": "Lavender Simple",
        "base": "Simple syrup and dried lavender",
        "ingredients": [
            "30g dried lavender to every liter of simple syrup",
            "1 teaspoon of butterfly pea powder to every liter for coloring"
        ],
        "method": "Let steep until cool. Strain. Add butterfly pea powder and mix via immersion blender",
        "yield": "Approximately 1 liter",
        "shelf_life": "30 days",
        "storage": "Refrigerated",
        "tags": ["flavored", "refrigerated", "lavender", "colored"]
    },
    {
        "name": "Tamarind Demerara",
        "base": "Rich Demerara syrup and tamarind paste",
        "ingredients": [
            "1:3 Tamarind paste to Rich Demerara syrup"
        ],
        "method": "Cook on stovetop. Bring to boil on high heat then reduce to medium and let simmer for 10-15 minutes",
        "yield": "Varies",
        "shelf_life": "30 days",
        "storage": "Refrigerated",
        "tags": ["flavored", "refrigerated", "tamarind"]
    },
    {
        "name": "Grapefruit Cordial",
        "base": "Grapefruit juice and sugar",
        "ingredients": [
            "1 quart grapefruit juice",
            "1 cup white sugar",
            "10 grams of malic acid"
        ],
        "method": "Cook on stovetop. Bring to boil, reduce heat and let simmer for 10-15 minutes. Let cool and add 10 grams of malic acid and mix thoroughly.",
        "yield": "Approximately 1 quart",
        "shelf_life": "14 days",
        "storage": "Refrigerated",
        "tags": ["cordial", "refrigerated", "grapefruit", "acidified"]
    },
    {
        "name": "Cranberry Ginger Syrup",
        "base": "Simple syrup with cranberry and ginger",
        "ingredients": [
            "2 cups cranberry per quart of simple syrup",
            "2 frozen ginger squares"
        ],
        "method": "Cook on stove top, keep on low until simmering for 20-30 minutes. Take off heat, let cool, strain.",
        "yield": "Approximately 1 quart",
        "shelf_life": "14 days",
        "storage": "Refrigerated",
        "tags": ["flavored", "refrigerated", "cranberry", "ginger", "seasonal"]
    },
    {
        "name": "Blackberry Mint Demerara",
        "base": "Brown sugar and water with blackberries and mint",
        "ingredients": [
            "500g water",
            "500g brown sugar",
            "2 cups Blackberries frozen or fresh",
            "Handful of mint"
        ],
        "method": "Cook on stovetop. Bring to boil, then reduce heat. Let simmer for 10-15 minutes",
        "yield": "Approximately 750mL",
        "shelf_life": "14 days",
        "storage": "Refrigerated",
        "tags": ["flavored", "refrigerated", "blackberry", "mint"]
    },
    {
        "name": "Mango Demerara",
        "base": "Brown sugar and mango puree",
        "ingredients": [
            "1 quart mango puree",
            "1 cup brown sugar"
        ],
        "method": "Cook on stovetop on low heat, let simmer for 20 minutes. Let cool. Should be in a squeeze bottle for service",
        "yield": "Approximately 1 quart",
        "shelf_life": "14 days",
        "storage": "Refrigerated, squeeze bottle",
        "tags": ["flavored", "refrigerated", "mango", "service_bottle"]
    }
]

# Define infusions
INFUSIONS = [
    {
        "name": "Chili Oil Tequila",
        "base": "Tequila",
        "ingredients": [
            "2 oz chili oil per liter tequila"
        ],
        "method": "Same method as olive oil vodka. Will not freeze solid, will need to be double strained!",
        "yield": "Approximately 1 liter per batch",
        "shelf_life": "60 days",
        "storage": "Refrigerated",
        "tags": ["infusion", "refrigerated", "tequila", "spicy"]
    },
    {
        "name": "Olive Oil Vodka",
        "base": "Vodka",
        "ingredients": [
            "2 oz olive oil per liter vodka"
        ],
        "method": "Same method as coconut rum",
        "yield": "Approximately 1 liter per batch",
        "shelf_life": "60 days",
        "storage": "Refrigerated",
        "tags": ["infusion", "refrigerated", "vodka", "savory"]
    },
    {
        "name": "Coconut Rum",
        "base": "Rum",
        "ingredients": [
            "4 oz melted coconut oil per liter of Rum"
        ],
        "method": "Stir periodically for 30 minutes. Freeze overnight, remove solid fat, strain remaining liquor through coffee filter.",
        "yield": "Approximately 1 liter per batch",
        "shelf_life": "60 days",
        "storage": "Refrigerated",
        "tags": ["infusion", "refrigerated", "rum", "coconut", "fat_washed"]
    }
]

# Define social drinks from the images
SOCIAL_DRINKS = [
    {
        "name": "Category 3",
        "ingredients": [
            "4 oz batch",
            "Garnish: orange rounds or pineapple if available"
        ],
        "batch": {
            "ingredients": [
                "1.5L white rum",
                "1.5L dark rum",
                "500mL golden falernum"
            ],
            "storage": "Refrigerated",
            "shelf_life": "30 days"
        },
        "method": "Built in glass over ice",
        "tags": ["rum", "falernum", "built", "batch", "highball"]
    },
    {
        "name": "Dublin",
        "ingredients": [
            "8 oz Tequila",
            "8 oz pomegranate juice",
            "4 oz grapefruit juice",
            "2 oz lemon juice",
            "1 spring can"
        ],
        "method": "GARNISH: grapefruit, garnish in dublin glasses",
        "tags": ["tequila", "pomegranate", "grapefruit", "lemon", "built", "highball"]
    },
    {
        "name": "Milano Menta Portion",
        "ingredients": [
            "16 oz vodka",
            "8 oz contratto aperitif",
            "8 oz lemon juice",
            "6 oz mint simple",
            "4 oz watermelon juice"
        ],
        "method": "GARNISH: lemon wheels, thoughout dubilns at top of ice in dublin glasses",
        "tags": ["vodka", "contratto", "lemon", "mint", "watermelon", "built", "highball"]
    },
    {
        "name": "Mule Keg",
        "ingredients": [
            "3 liter vodka",
            "32 oz ginger juice (spicy)",
            "80 oz simple syrup",
            "80 oz lime juice",
            "300 oz water"
        ],
        "method": "Keg and carbonate",
        "tags": ["vodka", "ginger", "lime", "keg", "carbonated"]
    },
    {
        "name": "Aperol Keg",
        "ingredients": [
            "1 case Aperol",
            "5 liter Aperol"
        ],
        "method": "Keg and carbonate",
        "tags": ["aperol", "keg", "carbonated"]
    }
]

# Define juices from the images (inferred from cocktail recipes)
JUICES = [
    {
        "name": "Lime Juice",
        "ingredients": ["Fresh limes"],
        "method": "Juice daily",
        "shelf_life": "24 hours",
        "storage": "Refrigerated",
        "tags": ["juice", "citrus", "daily_prep", "refrigerated"]
    },
    {
        "name": "Lemon Juice",
        "ingredients": ["Fresh lemons"],
        "method": "Juice daily",
        "shelf_life": "24 hours",
        "storage": "Refrigerated",
        "tags": ["juice", "citrus", "daily_prep", "refrigerated"]
    },
    {
        "name": "Grapefruit Juice",
        "ingredients": ["Fresh grapefruits"],
        "method": "Juice daily",
        "shelf_life": "24 hours",
        "storage": "Refrigerated",
        "tags": ["juice", "citrus", "daily_prep", "refrigerated"]
    }
]

# Create folder structure
def create_folders():
    if not os.path.exists(BASE_DIR):
        os.mkdir(BASE_DIR)
    
    for folder in FOLDERS:
        folder_path = os.path.join(BASE_DIR, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

# Create template files
def create_templates():
    template_dir = os.path.join(BASE_DIR, "Templates")
    
    # Cocktail template
    with open(os.path.join(template_dir, "Cocktail Template.md"), "w") as f:
        f.write("""---
name: "{{title}}"
type: "cocktail"
status: "active"
date_created: {{date:YYYY-MM-DD}}
last_modified: {{date:YYYY-MM-DD}}
batch_linked: "[[{{title}} Batch]]"
glassware: ""
garnish: ""
method: ""
tags: []
---

# {{title}}

## Ingredients
- 

## Preparation
1. 

## Notes
- 

## Linked Items
- Batch: [[{{title}} Batch]]
- Key Components:
""")
    
    # Batch template
    with open(os.path.join(template_dir, "Batch Template.md"), "w") as f:
        f.write("""---
name: "{{title}}"
type: "batch"
volume: ""
shelf_life: ""
storage: ""
status: "in stock" 
next_prep: ""
tags: []
---

# {{title}}

## Ingredients
- 

## Method
1. 

## Storage
- 

## Used In
- [[]]
""")
    
    # Syrup template
    with open(os.path.join(template_dir, "Syrup Template.md"), "w") as f:
        f.write("""---
name: "{{title}}"
type: "syrup"
base: ""
yield: ""
shelf_life: ""
storage: ""
status: "in stock" 
next_prep: ""
last_made: ""
tags: []
---

# {{title}}

## Ingredients
- 

## Method
1. 

## Notes
- 

## Used In
- [[]]
""")
    
    # Infusion template
    with open(os.path.join(template_dir, "Infusion Template.md"), "w") as f:
        f.write("""---
name: "{{title}}"
type: "infusion"
base_spirit: ""
yield: ""
shelf_life: ""
storage: ""
status: "in stock" 
next_prep: ""
last_made: ""
tags: []
---

# {{title}}

## Ingredients
- 

## Method
1. 

## Notes
- 

## Used In
- [[]]
""")
    
    # Juice template
    with open(os.path.join(template_dir, "Juice Template.md"), "w") as f:
        f.write("""---
name: "{{title}}"
type: "juice"
source: ""
prep_frequency: ""
yield: ""
shelf_life: ""
storage: ""
status: "needs daily prep"
tags: []
---

# {{title}}

## Ingredients
- 

## Method
1. 

## Notes
- 

## Used In
- [[]]
""")
    
    # Keg template
    with open(os.path.join(template_dir, "Keg Template.md"), "w") as f:
        f.write("""---
name: "{{title}}"
type: "keg"
volume: ""
carbonated: true/false
shelf_life: ""
status: "in stock" 
next_prep: ""
last_made: ""
tags: []
---

# {{title}}

## Ingredients
- 

## Method
1. 

## Notes
- 

## Service Notes
- 
""")

# Create cocktail files
def create_cocktail_files():
    today = datetime.now().strftime("%Y-%m-%d")
    
    for cocktail in COCKTAILS:
        # Create cocktail file
        cocktail_path = os.path.join(BASE_DIR, "Cocktails", f"{cocktail['name']}.md")
        
        # Build wikilinks for ingredients
        ingredient_links = []
        for ingredient in cocktail["ingredients"]:
            if "batch" in ingredient.lower():
                ingredient_links.append(f"- {ingredient} [[{cocktail['name']} Batch]]")
            elif "syrup" in ingredient.lower():
                syrup_name = re.search(r'(\w+)\s+syrup', ingredient.lower())
                if syrup_name:
                    ingredient_links.append(f"- {ingredient} [[{syrup_name.group(1).capitalize()} Syrup]]")
                else:
                    ingredient_links.append(f"- {ingredient}")
            elif "juice" in ingredient.lower():
                juice_name = re.search(r'(\w+)\s+juice', ingredient.lower())
                if juice_name:
                    ingredient_links.append(f"- {ingredient} [[{juice_name.group(1).capitalize()} Juice]]")
                else:
                    ingredient_links.append(f"- {ingredient}")
            else:
                ingredient_links.append(f"- {ingredient}")
        
        with open(cocktail_path, "w") as f:
            f.write(f"""---
name: "{cocktail['name']}"
type: "cocktail"
status: "active"
date_created: {today}
last_modified: {today}
batch_linked: "[[{cocktail['name']} Batch]]"
glassware: "{cocktail['glassware']}"
garnish: "{cocktail['garnish']}"
method: "{cocktail['method']}"
tags: {json.dumps(cocktail['tags'])}
---

# {cocktail['name']}

## Ingredients
{chr(10).join(ingredient_links)}

## Preparation
1. {cocktail['method']}
2. Serve in {cocktail['glassware']}
{f"3. Garnish with {cocktail['garnish']}" if cocktail['garnish'] else ""}

## Notes
{cocktail['notes'] if cocktail['notes'] else "- No special notes"}

## Linked Items
- Batch: [[{cocktail['name']} Batch]]
- Key Components: {', '.join(['[[' + tag.capitalize() + ']]' for tag in cocktail['tags'] if tag in ['tequila', 'vodka', 'gin', 'rum', 'bourbon', 'whiskey', 'mezcal']])}
""")
        
        # Create batch file
        batch_path = os.path.join(BASE_DIR, "Batches", f"{cocktail['name']} Batch.md")
        
        with open(batch_path, "w") as f:
            f.write(f"""---
name: "{cocktail['name']} Batch"
type: "batch"
volume: "{sum([float(re.search(r'(\d+(?:\.\d+)?)', i).group(1)) for i in cocktail['batch']['ingredients'] if re.search(r'(\d+(?:\.\d+)?)', i)])}L approx."
shelf_life: "{cocktail['batch']['shelf_life']}"
storage: "{cocktail['batch']['storage']}"
status: "in stock"
next_prep: ""
tags: {json.dumps(cocktail['tags'] + ['batch'])}
---

# {cocktail['name']} Batch

## Ingredients
{chr(10).join(['- ' + ingredient for ingredient in cocktail['batch']['ingredients']])}

## Method
1. Combine all ingredients in a clean container
2. Mix thoroughly
3. Label with name and date
4. {cocktail['batch']['storage']}

## Storage
- {cocktail['batch']['storage']}
- Shelf life: {cocktail['batch']['shelf_life']}

## Used In
- [[{cocktail['name']}]]
""")

# Create syrup files
def create_syrup_files():
    today = datetime.now().strftime("%Y-%m-%d")
    
    for syrup in SYRUPS:
        syrup_path = os.path.join(BASE_DIR, "Syrups", f"{syrup['name']}.md")
        
        # Find which cocktails use this syrup
        used_in = []
        for cocktail in COCKTAILS:
            for ingredient in cocktail['ingredients']:
                if syrup['name'].lower().split()[0] in ingredient.lower() and 'syrup' in ingredient.lower():
                    used_in.append(f"- [[{cocktail['name']}]]")
        
        with open(syrup_path, "w") as f:
            f.write(f"""---
name: "{syrup['name']}"
type: "syrup"
base: "{syrup['base']}"
yield: "{syrup['yield']}"
shelf_life: "{syrup['shelf_life']}"
storage: "{syrup['storage']}"
status: "in stock"
next_prep: ""
last_made: "{today}"
tags: {json.dumps(syrup['tags'])}
---

# {syrup['name']}

## Ingredients
{chr(10).join(['- ' + ingredient for ingredient in syrup['ingredients']])}

## Method
{syrup['method']}

## Storage
- {syrup['storage']}
- Shelf life: {syrup['shelf_life']}
- Store in appropriate container, label with name and date

## Used In
{chr(10).join(used_in) if used_in else "- Not currently used in any cocktails"}

## Notes
- Prep when stock is low, never run out completely
""")

# Create infusion files
def create_infusion_files():
    today = datetime.now().strftime("%Y-%m-%d")
    
    for infusion in INFUSIONS:
        infusion_path = os.path.join(BASE_DIR, "Infusions", f"{infusion['name']}.md")
        
        # Find which cocktails use this infusion
        used_in = []
        for cocktail in COCKTAILS:
            for ingredient in cocktail['batch']['ingredients']:
                if infusion['name'].lower() in ingredient.lower():
                    used_in.append(f"- [[{cocktail['name']}]] (via batch)")
        
        with open(infusion_path, "w") as f:
            f.write(f"""---
name: "{infusion['name']}"
type: "infusion"
base_spirit: "{infusion['base']}"
yield: "{infusion['yield']}"
shelf_life: "{infusion['shelf_life']}"
storage: "{infusion['storage']}"
status: "in stock"
next_prep: ""
last_made: "{today}"
tags: {json.dumps(infusion['tags'])}
---

# {infusion['name']}

## Ingredients
{chr(10).join(['- ' + ingredient for ingredient in infusion['ingredients']])}

## Method
{infusion['method']}

## Storage
- {infusion['storage']}
- Shelf life: {infusion['shelf_life']}
- Store in appropriate bottle, label with name and date

## Used In
{chr(10).join(used_in) if used_in else "- Not currently used in any cocktails"}

## Notes
- Prep at least 2 days before needed for service
- Batch dispensers and bottles should be kept in coolers
""")

# Create juice files
def create_juice_files():
    today = datetime.now().strftime("%Y-%m-%d")
    
    for juice in JUICES:
        juice_path = os.path.join(BASE_DIR, "Juices", f"{juice['name']}.md")
        
        # Find which cocktails use this juice
        used_in = []
        for cocktail in COCKTAILS:
            for ingredient in cocktail['ingredients']:
                if juice['name'].split()[0].lower() in ingredient.lower() and 'juice' in ingredient.lower():
                    used_in.append(f"- [[{cocktail['name']}]]")
        
        with open(juice_path, "w") as f:
            f.write(f"""---
name: "{juice['name']}"
type: "juice"
source: "{juice['ingredients'][0]}"
prep_frequency: "Daily"
yield: "Varies based on fruit size and quality"
shelf_life: "{juice['shelf_life']}"
storage: "{juice['storage']}"
status: "needs daily prep"
tags: {json.dumps(juice['tags'])}
---

# {juice['name']}

## Ingredients
{chr(10).join(['- ' + ingredient for ingredient in juice['ingredients']])}

## Method
1. Wash fruit thoroughly
2. Cut in half
3. Juice using electric juicer
4. Strain if necessary
5. Store in clean, labeled container
6. Refrigerate immediately

## Storage
- {juice['storage']}
- Shelf life: {juice['shelf_life']}
- Fresh juice must be made daily
- Label with time and date when prepped

## Used In
{chr(10).join(used_in) if used_in else "- Not currently used in any cocktails"}

## Notes
- Must be prepped daily before service
- Amount needed varies based on expected volume, season, and featured cocktails
- Aim for consistent yield by selecting similar sized fruits
""")

# Create social drink files
def create_social_drink_files():
    today = datetime.now().strftime("%Y-%m-%d")
    
    for drink in SOCIAL_DRINKS:
        drink_path = os.path.join(BASE_DIR, "Social Drinks", f"{drink['name']}.md")
        
        with open(drink_path, "w") as f:
            f.write(f"""---
name: "{drink['name']}"
type: "social_drink"
date_created: {today}
last_modified: {today}
method: "{drink['method']}"
tags: {json.dumps(drink['tags'])}
---

# {drink['name']}

## Ingredients
{chr(10).join(['- ' + ingredient for ingredient in drink['ingredients']])}

## Method
{drink['method']}

## Notes
- Designed for social/group service
- Batch size makes approximately {len(drink['ingredients'])*2} servings
""")
        
        # If it has a batch, create a batch file
        if "batch" in drink:
            batch_path = os.path.join(BASE_DIR, "Batches", f"{drink['name']} Batch.md")
            
            with open(batch_path, "w") as f:
                f.write(f"""---
name: "{drink['name']} Batch"
type: "batch"
volume: "{sum([float(re.search(r'(\d+(?:\.\d+)?)', i).group(1)) for i in drink['batch']['ingredients'] if re.search(r'(\d+(?:\.\d+)?)', i)])}L approx."
shelf_life: "{drink['batch']['shelf_life']}"
storage: "{drink['batch']['storage']}"
status: "in stock"
next_prep: ""
tags: {json.dumps(drink['tags'] + ['batch', 'social'])}
---

# {drink['name']} Batch

## Ingredients
{chr(10).join(['- ' + ingredient for ingredient in drink['batch']['ingredients']])}

## Method
1. Combine all ingredients in a clean container
2. Mix thoroughly
3. Label with name and date
4. {drink['batch']['storage']}

## Storage
- {drink['batch']['storage']}
- Shelf life: {drink['batch']['shelf_life']}

## Used In
- [[{drink['name']}]]
""")

# Create keg files (for drinks that are kegged)
def create_keg_files():
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Filter cocktails and social drinks that should be kegged
    keg_drinks = []
    
    for cocktail in COCKTAILS:
        if "keg" in cocktail.get("tags", []):
            keg_drinks.append({
                "name": cocktail["name"],
                "ingredients": cocktail["batch"]["ingredients"],
                "carbonated": "carbonated" in cocktail.get("tags", []),
                "shelf_life": cocktail["batch"]["shelf_life"],
                "tags": cocktail["tags"]
            })
    
    for drink in SOCIAL_DRINKS:
        if "keg" in drink.get("tags", []):
            keg_drinks.append({
                "name": drink["name"],
                "ingredients": drink["batch"]["ingredients"] if "batch" in drink else drink["ingredients"],
                "carbonated": "carbonated" in drink.get("tags", []),
                "shelf_life": drink["batch"]["shelf_life"] if "batch" in drink else "7 days",
                "tags": drink["tags"]
            })
    
    # Add specific kegs from the images
    if not any(d["name"] == "Mule Keg" for d in keg_drinks):
        keg_drinks.append({
            "name": "Mule Keg",
            "ingredients": [
                "3 liter vodka",
                "32 oz ginger juice (spicy)",
                "80 oz simple syrup",
                "80 oz lime juice",
                "300 oz water"
            ],
            "carbonated": True,
            "shelf_life": "7 days",
            "tags": ["vodka", "ginger", "lime", "keg", "carbonated"]
        })
    
    if not any(d["name"] == "Aperol Keg" for d in keg_drinks):
        keg_drinks.append({
            "name": "Aperol Keg",
            "ingredients": [
                "1 case Aperol",
                "5 liter Aperol"
            ],
            "carbonated": True,
            "shelf_life": "30 days",
            "tags": ["aperol", "keg", "carbonated"]
        })
    
    for keg in keg_drinks:
        keg_path = os.path.join(BASE_DIR, "Kegs", f"{keg['name']} Keg.md")
        
        with open(keg_path, "w") as f:
            f.write(f"""---
name: "{keg['name']} Keg"
type: "keg"
volume: "19L standard keg"
carbonated: {"true" if keg['carbonated'] else "false"}
shelf_life: "{keg['shelf_life']}"
status: "in stock"
next_prep: ""
last_made: "{today}"
tags: {json.dumps(keg['tags'])}
---

# {keg['name']} Keg

## Ingredients
{chr(10).join(['- ' + ingredient for ingredient in keg['ingredients']])}

## Method
1. Clean keg thoroughly with appropriate sanitizer
2. Combine all ingredients in clean container and mix thoroughly
3. Fill keg leaving appropriate headspace
4. {"Carbonate according to standard procedure" if keg['carbonated'] else "Pressurize with nitrogen"}
5. Label with name and date
6. Allow to settle for at least 1 hour before service

## Storage
- Keep keg refrigerated at all times
- Shelf life: {keg['shelf_life']}
- {"Maintain CO2 pressure at 12-15 PSI" if keg['carbonated'] else "Maintain nitrogen pressure at 30-35 PSI"}

## Service Notes
- {"Pour slowly to manage foam" if keg['carbonated'] else "Pour at a steady rate"}
- Clean lines weekly
- Check pressure daily before service
""")

# Create dashboard/MOC
# Create dashboard/MOC
def create_dashboard():
    dashboard_path = os.path.join(BASE_DIR, "Dashboard.md")
    
    with open(dashboard_path, "w") as f:
        f.write("""# Bar Dashboard

## Quick Access
- [[Templates/Cocktail Template|New Cocktail]]
- [[Templates/Batch Template|New Batch]]
- [[Templates/Syrup Template|New Syrup]]
- [[Production/Prep Tasks|Today's Prep]]

## Inventory Status
```dataview
TABLE status, next_prep
FROM "Syrups" OR "Infusions" OR "Batches" OR "Kegs" 
WHERE status = "out of stock" OR status = "low stock"
SORT status ASC, next_prep ASC
```

## Daily Prep Required
```dataview
TABLE type, status
FROM "Juices"
SORT type ASC
```

## Featured Cocktails
```dataview
TABLE glassware, garnish, tags
FROM "Cocktails"
WHERE featured = true
SORT name ASC
```

## Recently Modified
```dataview
TABLE type, last_modified as "Last Updated"
FROM "Cocktails" OR "Batches" OR "Syrups" OR "Infusions" OR "Juices" OR "Kegs"
SORT file.mtime DESC
LIMIT 5
```

## Weekly Production Schedule
- Monday: Syrups, Infusions
- Tuesday: Batches
- Wednesday: Restock
- Thursday: Syrups, Batches
- Friday: Pre-weekend Prep
- Saturday: Emergency Prep Only
- Sunday: Weekly Deep Clean & Inventory

## Keg Status
```dataview
TABLE status, next_prep, last_made as "Last Made"
FROM "Kegs"
SORT status ASC
```

## Tags Index
- #tequila #vodka #gin #rum #bourbon #whiskey #mezcal - Base Spirits
- #shaken #stirred #built - Preparation Methods
- #refrigerated #freezer - Storage Requirements 
- #batch #infusion #syrup #juice - Product Types
- #daily_prep #weekly_prep - Production Schedule
- #spicy #sweet #sour #bitter - Flavor Profiles
""")

# Create production files
def create_production_files():
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Weekly Schedule
    schedule_path = os.path.join(BASE_DIR, "Production", "Weekly Schedule.md")
    with open(schedule_path, "w") as f:
        f.write("""# Weekly Production Schedule

## Monday
- [ ] Make all basic syrups 
- [ ] Start any new infusions
- [ ] Check stock levels for weekend

## Tuesday
- [ ] Make specialty syrups
- [ ] Prep batches for high-volume cocktails
- [ ] Filter any infusions started last week

## Wednesday
- [ ] Restock all spirits and modifiers
- [ ] Deep clean bar station
- [ ] Inventory check

## Thursday
- [ ] Top up all syrups
- [ ] Prep remaining batches
- [ ] Fill kegs as needed

## Friday
- [ ] Final pre-weekend prep
- [ ] Double-check all mise en place
- [ ] Ensure all juices are fresh and stocked

## Saturday
- [ ] Emergency prep only
- [ ] Quick restock as needed

## Sunday
- [ ] Weekly deep clean
- [ ] Full inventory
- [ ] Plan production for upcoming week
""")
    
    # Prep Tasks
    tasks_path = os.path.join(BASE_DIR, "Production", "Prep Tasks.md")
    with open(tasks_path, "w") as f:
        f.write(f"""# Daily Prep Tasks

## Date: {today}

## Morning Prep
- [ ] Fresh juice all citrus
- [ ] Check syrup levels
- [ ] Check batch levels
- [ ] Fill ice wells
- [ ] Prep all garnishes
- [ ] Check keg pressure and levels

## Batches Needed
```dataview
TABLE status, next_prep 
FROM "Batches"
WHERE status = "out of stock" OR status = "low stock"
SORT next_prep ASC
```

## Syrups Needed
```dataview
TABLE status, next_prep 
FROM "Syrups"
WHERE status = "out of stock" OR status = "low stock"
SORT next_prep ASC
```

## Infusions Needed
```dataview
TABLE status, next_prep 
FROM "Infusions"
WHERE status = "out of stock" OR status = "low stock"
SORT next_prep ASC
```

## Notes & Special Tasks


## Completed
- [ ] All daily juices made
- [ ] All needed batches made
- [ ] All syrups restocked
- [ ] All mise en place complete
- [ ] All stations wiped down and organized
""")

# Main function to run everything
def main():
    print("Creating Obsidian Bar Management System...")
    create_folders()
    print("✓ Folders created")
    
    create_templates()
    print("✓ Templates created")
    
    create_cocktail_files()
    print("✓ Cocktail files created")
    
    create_syrup_files()
    print("✓ Syrup files created")
    
    create_infusion_files()
    print("✓ Infusion files created")
    
    create_juice_files()
    print("✓ Juice files created")
    
    create_social_drink_files()
    print("✓ Social drink files created")
    
    create_keg_files()
    print("✓ Keg files created")
    
    create_dashboard()
    print("✓ Dashboard created")
    
    create_production_files()
    print("✓ Production files created")
    
    print("\nObsidian Bar Management System successfully created!")
    print(f"\nYour vault is ready in the '{BASE_DIR}' directory.")
    print("\nImport instructions:")
    print("1. Open Obsidian")
    print("2. Click 'Open folder as vault'")
    print(f"3. Navigate to the '{BASE_DIR}' folder")
    print("4. Install recommended plugins: Dataview, Calendar, Templater")
    print("5. Start with the Dashboard.md file to navigate your system")

if __name__ == "__main__":
    main()