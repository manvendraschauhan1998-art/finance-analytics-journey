portfolio = {
    "Equity": 600000,
    "Debt": 250000,
    "Gold": 100000,
    "Cash": 50000
}
def calculate_portfolio_metrics(portfolio):
    total_value = sum(portfolio.values())
    allocations={}
    for asset, value in portfolio.items():
        allocation = value/total_value*100
        allocations[asset]=allocation

    largest_asset=max(portfolio,key=portfolio.get)
    smallest_asset = min(portfolio,key=portfolio.get)
    return total_value, allocations, largest_asset,smallest_asset
total_value, allocations, largest_asset, smallest_asset = calculate_portfolio_metrics(portfolio)

print("====================================")
print("        PORTFOLIO SUMMARY")
print("====================================")

for asset, value in portfolio.items():
    print(f"{asset}: ₹{value:,.0f}   {allocations[asset]:.1f}%")

print("------------------------------------")
print(f"Total Portfolio: ₹{total_value:,.0f}")
print("------------------------------------")

print(f"Largest allocation: {largest_asset}")
print(f"Smallest allocation: {smallest_asset}")