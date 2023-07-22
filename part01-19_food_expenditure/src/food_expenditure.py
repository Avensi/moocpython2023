# Write your solution here
week = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

print("Average food expenditure:")
print(f"Daily: {((week * lunch_price) + groceries) / 7} euros")
print(f"Weekly: {groceries + (week * lunch_price) } euros")