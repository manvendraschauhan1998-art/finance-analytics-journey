def calculate_future_value(principal, annual_return, years):
    future_value = principal * (1 + annual_return) ** years
    return future_value
value = calculate_future_value(100000, 0.10, 10)
print(value)