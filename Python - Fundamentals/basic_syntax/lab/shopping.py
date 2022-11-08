budget = int(input())
command = input()

has_money = True
while command != "End":
	price = int(command)
	budget -= price
	if budget < 0:
		has_money = False
		print("You went in overdraft!")
		break
	command = input()
	
if has_money:
	print("You bought everything needed.")

