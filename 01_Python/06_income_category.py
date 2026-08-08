monthly_salary = int(input("Enter your monthly salary: "))
annual_income = 12*monthly_salary
if annual_income<1000000:
    print("You are in the low income category")
elif annual_income>=1000000 and annual_income<2500000:
    print("You are in the medium income category") 
elif annual_income>=2500000 and annual_income<5000000:
    print("You are in the high income category")
else:
    print("You are in the very high income category")
