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


print(format_inr(2160000))
print(format_inr(1000000))
print(format_inr(250000))
print(format_inr(10000))
print(format_inr(1000))
print(format_inr(500))
