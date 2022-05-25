print("Welcome to the Tip calculator.")
total_bill = input("What was the total bill? $")
percentage= input("What percentage tip would you like to give? 10, 12 or 15? ")
people_split= input("How many people to split the bill? ")
int_bill= float(total_bill)
int_people_split= float(people_split)
int_percentage= float(percentage)
newamount = (int_bill*int_percentage/100+int_bill)/int_people_split
print(f"Your new amount is ${newamount :.2f}")