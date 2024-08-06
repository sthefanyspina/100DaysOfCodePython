print("Welcome to the Tip Calculator!")

bill = float(input("What is the total bill amount?\n"))
tip = int(input("How much tip would you like to give?\n Percent:"))
split = int(input("How many people to split the bill?\n People:"))

total = ("{:.2f}".format(bill * (tip / 100) / split))

print(f"Each person should pay: ${total}")