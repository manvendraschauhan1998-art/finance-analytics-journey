portfolio = {
    "equity": 600000,
    "debt": 250000,
    "gold": 100000,
    "cash": 50000
}

total_portfolio=0
for i in portfolio:
    total_portfolio+=portfolio[i]
equity_portfolio = portfolio["equity"]/total_portfolio
debt_portfolio = portfolio["debt"]/total_portfolio
gold_portfolio = portfolio["gold"]/total_portfolio
cash_portfolio = portfolio["cash"]/total_portfolio
print(f"Total portfolio:{total_portfolio:,.0f}")
print(f"Equity: {equity_portfolio:,.0%}")
print(f"debt: {debt_portfolio:,.0%}")
print(f"gold: {gold_portfolio:,.0%}")
print(f"cash: {cash_portfolio:,.0%}")
