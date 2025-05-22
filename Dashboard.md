# Bar Dashboard

## Quick Access
- [[../999 Templates/Cocktail Template|New Cocktail]]
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
