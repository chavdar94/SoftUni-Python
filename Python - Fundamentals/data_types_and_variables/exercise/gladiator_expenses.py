lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmets = lost_fights // 2
broken_swords = lost_fights // 3
broken_shields = lost_fights // 6
broken_armors = broken_shields // 2

expenses = broken_helmets * helmet_price +\
           broken_swords * sword_price + \
           broken_shields * shield_price +\
           broken_armors * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")