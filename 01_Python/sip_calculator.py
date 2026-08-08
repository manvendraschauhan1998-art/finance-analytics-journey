monthly_sip= float(input("Enter your monthly SIP: "))
annual_return= float(input("Enter the expected annual return (%): "))/100
years=int(input("Enter the number of years you want to invest: "))

def calculate_sip(monthly_sip, annual_return, years):
    if monthly_sip <= 0:
        print("Monthly SIP cannot be zero or negative")
        return 
    if annual_return <= 0:
        print("Annual return must be positive")
        return
    if years <= 0:
        print("Investment period must be positive")
        return
    monthly_return = annual_return / 12 
    number_of_months = years * 12
    future_value = monthly_sip*((1+monthly_return)**number_of_months-1)*(1+monthly_return)/monthly_return
    total_invested = monthly_sip * number_of_months
    wealth_created = future_value - total_invested
    return total_invested, future_value, wealth_created

def format_inr(number):
    number = round(number)

    number_str = str(number)

    if len(number_str) <= 3:
        formatted_number = number_str
    else:
        last_three = number_str[-3:]
        remaining = number_str[:-3]

        groups = []

        while len(remaining) > 2:
            groups.insert(0, remaining[-2:])
            remaining = remaining[:-2]

        if remaining:
            groups.insert(0, remaining)

        formatted_number = ",".join(groups) + "," + last_three

    return "₹" + formatted_number

total_invested, future_value, wealth_created = calculate_sip(monthly_sip, annual_return, years)
print(f"Total invested: {format_inr(total_invested)}")  
print(f"Future value of SIP: ₹{future_value:,.0f}")
print(f"Wealth created: ₹{wealth_created:,.0f}")
