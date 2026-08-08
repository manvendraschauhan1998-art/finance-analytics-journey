initial_investment = 100000
annual_return = 0.10

for year in range(1, 11):
    # calculate value
    value = initial_investment * (1 + annual_return) ** year
    print(f"Year {year}: Value = {value:.2f}")