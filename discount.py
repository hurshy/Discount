#Tyler Hegewald
#User enters a price and is calculated for the clearance sale at a store.

price = float(input("Please enter a price "))

week_one = price * .8
week_two = week_one * .75
week_three = week_two * .70
week_four = week_three * .5

print("Week 1: " + "$%.2f"%week_one)
print("Week 2: " + "$%.2f"%week_two)
print("Week 3: " + "$%.2f"%week_three)
print("Week 4: " + "$%.2f"%week_four)
