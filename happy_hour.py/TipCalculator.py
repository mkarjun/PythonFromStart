# Tip Calculator

# This program will calculate the tip for a meal.
# It will ask the user for the meal cost and the tip percentage.
# It will then display the tip amount.
# It will also display the total cost of the meal.
# The program will replace the dollar sign with a blank space.

print(input("Name: "))
meal_cost = (input("Meal cost: "))
meal_cost_dlr = float(meal_cost.replace("$", ""))
tip_percentage = float(input(" Tip Percentage: "))
tip_amount = meal_cost_dlr * ( tip_percentage / 100)
total_cost = meal_cost_dlr + tip_amount
print(f"Tip amount is: ${round(tip_amount,2)}")
print(f"Total Cost is: ${round(total_cost,2)}")
