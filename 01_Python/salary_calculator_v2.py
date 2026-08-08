monthly_salary = int(input("Enter your monthly salary: "))
annual_bonus = int(input("Enter your annual bonus: "))
annual_salary = (monthly_salary * 12)
total_annual_compensation = annual_salary + annual_bonus
monthly_compensation = total_annual_compensation / 12
bonus_percentage = (annual_bonus / annual_salary) * 100

if monthly_salary < 0:
    print("Salary cannot be negative")
if annual_bonus < 0:
    print("Bonus cannot be negative")

print("Annual salary:", f"₹{annual_salary:,}")
print("Total annual compensation:", f"₹{total_annual_compensation:,}")  
print("Monthly compensation:", f"₹{monthly_compensation:,}")
print("Bonus percentage:", f"{bonus_percentage:.2f}%")
