store_inventory = [
    {"name": "חלב", "price": 6.5, "quantity": 20},
    {"name": "לחם", "price": 8.0, "quantity": 15},
    {"name": "ביצים", "price": 14.0, "quantity": 10},
]

# 2. רשימת המוצרים שהגיעו במשלוח החדש (חלקם קיימים וחלקם חדשים)
delivery = [
    {"name": "חלב", "price": 6.5, "quantity": 30},  # קיים - הכמות תעלה ל-50
    {"name": "ביצים", "price": 14.5, "quantity": 12},  # קיים - הכמות תעלה ל-22
    {"name": "גבינה צהובה", "price": 24.0, "quantity": 8},  # חדש בחנות
    {"name": "שוקולד", "price": 5.5, "quantity": 40},  # חדש בחנות
]


for g in delivery:
        for i in store_inventory:
            if g["name"] ==i["name"]:
                i["quantity"]+=g["quantity"]
                break
               
            
        else:
             store_inventory.append(g)
print(store_inventory)
