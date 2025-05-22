# Daily Prep Tasks

## Date: 2025-05-20

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
