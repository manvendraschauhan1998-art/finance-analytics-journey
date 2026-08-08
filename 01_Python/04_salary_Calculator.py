monthly_salary = int(input("Enter your monthly salary: "))
annual_bonus = int(input("Enter your annual bonus: "))
annual_salary = (monthly_salary * 12)
total_annual_compensation = annual_salary + annual_bonus

print("Annual salary:", f"₹{annual_salary:,}")
print("Total annual compensation:", f"₹{total_annual_compensation:,}")