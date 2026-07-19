"""
Personal Finance Dashboard
Difficulty: Hard
Concepts: matplotlib, pandas, Data Visualization
"""

import os
from datetime import datetime

try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use("Agg")  # Non-interactive backend
except ImportError:
    print("Please install required packages:")
    print("  pip install pandas matplotlib")
    exit(1)


def create_sample_data(filename="transactions.csv"):
    """Create sample transaction data if file doesn't exist."""
    if os.path.exists(filename):
        return

    sample_data = """date,amount,category,type,note
2026-01-05,3000.00,Salary,income,Monthly salary
2026-01-08,45.50,Food,expense,Groceries
2026-01-10,120.00,Transport,expense,Monthly pass
2026-01-12,800.00,Rent,expense,January rent
2026-01-15,60.00,Entertainment,expense,Movie night
2026-01-18,35.00,Food,expense,Lunch
2026-01-20,200.00,Utilities,expense,Electric bill
2026-01-22,50.00,Food,expense,Dinner
2026-01-25,150.00,Shopping,expense,Clothes
2026-01-28,90.00,Transport,expense,Gas
2026-02-05,3000.00,Salary,income,Monthly salary
2026-02-08,55.00,Food,expense,Groceries
2026-02-10,120.00,Transport,expense,Monthly pass
2026-02-12,800.00,Rent,expense,February rent
2026-02-14,40.00,Entertainment,expense,Concert
2026-02-18,30.00,Food,expense,Lunch
2026-02-20,180.00,Utilities,expense,Electric + Water
2026-02-22,65.00,Food,expense,Dinner
2026-02-25,200.00,Shopping,expense,Electronics
2026-02-28,95.00,Transport,expense,Gas
2026-03-05,3200.00,Salary,income,Monthly salary + bonus
2026-03-08,50.00,Food,expense,Groceries
2026-03-10,120.00,Transport,expense,Monthly pass
2026-03-12,800.00,Rent,expense,March rent
2026-03-15,80.00,Entertainment,expense,Game night
2026-03-18,40.00,Food,expense,Lunch
2026-03-20,220.00,Utilities,expense,Electric bill
2026-03-22,70.00,Food,expense,Dinner
2026-03-25,120.00,Shopping,expense,Books
2026-03-28,85.00,Transport,expense,Gas
"""
    with open(filename, "w") as f:
        f.write(sample_data)
    print(f"📄 Created sample data: {filename}")


def load_data(filename):
    """Load and preprocess transaction data."""
    df = pd.read_csv(filename)
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.to_period("M")
    return df


def monthly_income_vs_expenses(df):
    """Plot monthly income vs expenses line chart."""
    monthly = df.groupby(["month", "type"])["amount"].sum().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(10, 5))
    monthly.plot(kind="line", ax=ax, marker="o", linewidth=2)
    ax.set_title("Monthly Income vs Expenses", fontsize=14, fontweight="bold")
    ax.set_xlabel("Month", fontsize=11)
    ax.set_ylabel("Amount ($)", fontsize=11)
    ax.legend(title="Type")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("chart_income_expenses.png", dpi=150)
    plt.close()
    print("  📊 Saved: chart_income_expenses.png")


def expense_breakdown_pie(df):
    """Plot expense breakdown pie chart."""
    expenses = df[df["type"] == "expense"].groupby("category")["amount"].sum()

    fig, ax = plt.subplots(figsize=(8, 8))
    colors = plt.cm.Set3(range(len(expenses)))
    wedges, texts, autotexts = ax.pie(
        expenses.values,
        labels=expenses.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=colors,
        textprops={"fontsize": 10}
    )
    ax.set_title("Expense Breakdown by Category", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig("chart_expense_pie.png", dpi=150)
    plt.close()
    print("  📊 Saved: chart_expense_pie.png")


def savings_trend(df):
    """Plot savings trend area chart."""
    monthly = df.groupby(["month", "type"])["amount"].sum().unstack(fill_value=0)
    monthly["savings"] = monthly.get("income", 0) - monthly.get("expense", 0)
    monthly["cumulative"] = monthly["savings"].cumsum()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.fill_between(
        range(len(monthly)),
        monthly["cumulative"].values,
        alpha=0.4,
        color="green"
    )
    ax.plot(range(len(monthly)), monthly["cumulative"].values, color="green", linewidth=2, marker="o")
    ax.set_title("Cumulative Savings Trend", fontsize=14, fontweight="bold")
    ax.set_xlabel("Month", fontsize=11)
    ax.set_ylabel("Cumulative Savings ($)", fontsize=11)
    ax.set_xticks(range(len(monthly)))
    ax.set_xticklabels([str(m) for m in monthly.index], rotation=45)
    ax.axhline(y=0, color="gray", linestyle="--", alpha=0.5)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("chart_savings_trend.png", dpi=150)
    plt.close()
    print("  📊 Saved: chart_savings_trend.png")


def category_spending_bar(df):
    """Plot category-wise spending bar chart."""
    expenses = df[df["type"] == "expense"].groupby("category")["amount"].sum().sort_values(ascending=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(expenses.index, expenses.values, color=plt.cm.Pastel1(range(len(expenses))))
    ax.set_title("Spending by Category", fontsize=14, fontweight="bold")
    ax.set_xlabel("Total Amount ($)", fontsize=11)

    # Add value labels
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 5, bar.get_y() + bar.get_height()/2,
                f"${width:.0f}", ha="left", va="center", fontsize=9)

    ax.grid(True, axis="x", alpha=0.3)
    plt.tight_layout()
    plt.savefig("chart_category_spending.png", dpi=150)
    plt.close()
    print("  📊 Saved: chart_category_spending.png")


def budget_vs_actual(df):
    """Plot budget vs actual spending comparison."""
    # Example budgets (can be customized)
    budgets = {
        "Food": 200,
        "Transport": 150,
        "Rent": 800,
        "Utilities": 250,
        "Entertainment": 100,
        "Shopping": 200,
    }

    actual = df[df["type"] == "expense"].groupby("category")["amount"].sum()

    categories = list(budgets.keys())
    budget_values = [budgets.get(c, 0) for c in categories]
    actual_values = [actual.get(c, 0) for c in categories]

    x = range(len(categories))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar([i - width/2 for i in x], budget_values, width, label="Budget", color="steelblue", alpha=0.8)
    ax.bar([i + width/2 for i in x], actual_values, width, label="Actual", color="coral", alpha=0.8)

    ax.set_title("Budget vs Actual Spending", fontsize=14, fontweight="bold")
    ax.set_xlabel("Category", fontsize=11)
    ax.set_ylabel("Amount ($)", fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=45, ha="right")
    ax.legend()
    ax.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("chart_budget_vs_actual.png", dpi=150)
    plt.close()
    print("  📊 Saved: chart_budget_vs_actual.png")


def print_summary(df):
    """Print console summary report."""
    print("\n" + "=" * 55)
    print("📈 FINANCIAL SUMMARY REPORT")
    print("=" * 55)

    total_income = df[df["type"] == "income"]["amount"].sum()
    total_expense = df[df["type"] == "expense"]["amount"].sum()
    net_savings = total_income - total_expense

    print(f"\n  💰 Total Income:    ${total_income:>10,.2f}")
    print(f"  💸 Total Expenses:  ${total_expense:>10,.2f}")
    print(f"  📊 Net Savings:     ${net_savings:>10,.2f}")
    print(f"  📉 Savings Rate:    {(net_savings/total_income*100 if total_income else 0):>10.1f}%")

    print(f"\n  {'─' * 50}")
    print(f"  {'Category':<18}{'Spent':>12}{'% of Total':>12}{'Transactions':>12}")
    print(f"  {'─' * 50}")

    expenses = df[df["type"] == "expense"]
    cat_summary = expenses.groupby("category").agg({"amount": "sum", "date": "count"})
    cat_summary = cat_summary.sort_values("amount", ascending=False)

    for cat, row in cat_summary.iterrows():
        pct = (row["amount"] / total_expense * 100) if total_expense else 0
        print(f"  {cat:<18}${row['amount']:>10,.2f}{pct:>10.1f}%{row['date']:>10}")

    print(f"  {'─' * 50}")
    print(f"  {'Total':<18}${total_expense:>10,.2f}{'100.0%':>10}{len(expenses):>10}")
    print(f"  {'─' * 50}")

    # Monthly breakdown
    print(f"\n  📅 Monthly Breakdown:")
    print(f"  {'─' * 40}")
    monthly = df.groupby(["month", "type"])["amount"].sum().unstack(fill_value=0)
    for month, row in monthly.iterrows():
        inc = row.get("income", 0)
        exp = row.get("expense", 0)
        sav = inc - exp
        print(f"  {month:<10}  Income: ${inc:>8,.2f}  Exp: ${exp:>8,.2f}  Save: ${sav:>8,.2f}")
    print(f"  {'─' * 40}")
    print("=" * 55)


def main():
    """Main dashboard runner."""
    filename = "transactions.csv"
    create_sample_data(filename)

    print("=" * 55)
    print("💼 PERSONAL FINANCE DASHBOARD")
    print("=" * 55)

    df = load_data(filename)
    print(f"\n📄 Loaded {len(df)} transactions")

    print("\n📊 Generating charts...")
    monthly_income_vs_expenses(df)
    expense_breakdown_pie(df)
    savings_trend(df)
    category_spending_bar(df)
    budget_vs_actual(df)

    print("\n✅ All charts exported as PNG files!")
    print_summary(df)


if __name__ == "__main__":
    main()
