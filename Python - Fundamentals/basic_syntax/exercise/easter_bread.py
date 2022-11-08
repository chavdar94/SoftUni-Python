budget = float(input())
price_per_flour = float(input())
#  egg price is 75% less than flour price
egg_price = price_per_flour * 0.75

#  1 liter milk is 25% more expensive than the price for flour
price_for_liter_milk = price_per_flour + (price_per_flour * 0.25)
milk_price = price_for_liter_milk / 4

#  recipe for easter bread
easter_bread_price = price_per_flour + egg_price + milk_price

easter_breads = 0
colored_eggs = 0
while budget > easter_bread_price:
    budget -= easter_bread_price
    easter_breads += 1
    colored_eggs += 3
    if easter_breads % 3 == 0:
        colored_eggs -= easter_breads - 2


print(f"You made {easter_breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")


