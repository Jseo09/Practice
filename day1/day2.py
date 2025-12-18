print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? % ")
percentage = input(" how much tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")

final_bill = (float(total_bill)+(float(total_bill) * (float(percentage)/100)))/float(people)

print(f"The final bill is {final_bill:.2f} per person")
