income = float(input("Enter your income: "))

if income <= 85528:
    tax = (income * 0.18) - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32


tax = max(0, tax)


print("Tax to be paid: ", round(tax), " thalers")
