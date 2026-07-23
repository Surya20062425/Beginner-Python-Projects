"""
Expense Tracker
Difficulty: Medium
Concepts: datetime, Data Structures, File I/O
"""

import json
import os
from datetime import datetime, timedelta
from collections import defaultdict

DATA_FILE = "expenses.json"


def load_expenses():
    """Load expenses from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_expenses(expenses):
    """Save expenses to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def get_date_input(prompt="Date"):
    """Get a valid date from user."""
    while True:
        date_str = input(f"{prompt} (YYYY-MM-DD, or 'today'): ").strip()
        if date_str.lower() == "today":
            return datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD.")


def add_expense(expenses):
    """Add a new expense."""
    print("\n➕ Add Expense")
    print("-" * 40)

    try:
        amount = float(input("Amount: $").strip())
        if amount <= 0:
            print("❌ Amount must be positive.")
            return
    except ValueError:
        print("❌ Invalid amount.")
        return

    category = input("Category (e.g., Food, Transport, Bills): ").strip().title()
    if not category:
        category = "Uncategorized"

    date = get_date_input()
    note = input("Note (optional): ").strip()

    expense = {
        "id": len(expenses) + 1,
        "amount": round(amount, 2),
        "category": category,
        "date": date,
        "note": note,
        "created_at": datetime.now().isoformat()
    }

    expenses.append(expense)
    save_expenses(expenses)
    print(f"✅ Added: ${amount:.2f} for {category}")


def view_expenses(expenses):
    """View expenses with filters."""
    print("\n📋 View Expenses")
    print("-" * 40)
    print("Filter by:")
    print("  1. Date range")
    print("  2. Category")
    print("  3. All expenses")

    choice = input("\nChoose (1-3): ").strip()
    filtered = expenses[:]

    if choice == "1":
        start = get_date_input("Start date")
        end = get_date_input("End date")
        filtered = [e for e in expenses if start <= e["date"] <= end]
    elif choice == "2":
        cats = sorted(set(e["category"] for e in expenses))
        print(f"\nCategories: {', '.join(cats)}")
        cat = input("Enter category: ").strip().title()
        filtered = [e for e in expenses if e["category"] == cat]

    if not filtered:
        print("📭 No expenses found.")
        return

    print(f"\n{'─' * 60}")
    print(f"  {'ID':<5}{'Date':<12}{'Category':<14}{'Amount':<10}{'Note'}")
    print(f"{'─' * 60}")

    total = 0
    for e in sorted(filtered, key=lambda x: x["date"]):
        print(f"  {e['id']:<5}{e['date']:<12}{e['category']:<14}${e['amount']:<9.2f}{e['note'][:20]}")
        total += e["amount"]

    print(f"{'─' * 60}")
    print(f"  Total: ${total:.2f}  ({len(filtered)} transaction(s))")
    print(f"{'─' * 60}")


def set_budgets(expenses):
    """Set and check monthly budgets."""
    budgets = {}
    print("\n💰 Set Monthly Budgets")
    print("(Enter 0 to skip a category)")

    cats = sorted(set(e["category"] for e in expenses))
    if not cats:
        print("📭 No expenses yet. Add some first!")
        return budgets

    for cat in cats:
        try:
            budget = float(input(f"Budget for {cat}: $").strip() or "0")
            if budget > 0:
                budgets[cat] = budget
        except ValueError:
            pass

    return budgets


def monthly_summary(expenses, budgets=None):
    """Generate monthly summary with ASCII bar chart."""
    print("\n📊 Monthly Summary")
    print("-" * 40)

    year_month = input("Enter month (YYYY-MM): ").strip()
    try:
        datetime.strptime(year_month, "%Y-%m")
    except ValueError:
        print("❌ Invalid format. Use YYYY-MM.")
        return

    monthly = [e for e in expenses if e["date"].startswith(year_month)]
    if not monthly:
        print(f"📭 No expenses for {year_month}.")
        return

    # Category breakdown
    cat_totals = defaultdict(float)
    for e in monthly:
        cat_totals[e["category"]] += e["amount"]

    total = sum(cat_totals.values())

    print(f"\n{'=' * 50}")
    print(f"  📅 {year_month} Summary")
    print(f"{'=' * 50}")
    print(f"  Total Spent: ${total:.2f}")
    print(f"  Transactions: {len(monthly)}")
    print(f"  Avg/Transaction: ${total/len(monthly):.2f}")
    print(f"{'─' * 50}")

    # ASCII bar chart
    max_val = max(cat_totals.values()) if cat_totals else 1
    print("\n  Category Breakdown:")
    for cat, amount in sorted(cat_totals.items(), key=lambda x: -x[1]):
        bar_len = int((amount / max_val) * 20)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        pct = (amount / total) * 100
        alert = ""
        if budgets and cat in budgets and amount > budgets[cat]:
            alert = " ⚠️ OVER BUDGET"
        print(f"  {cat:<14} {bar}  ${amount:>7.2f} ({pct:>4.1f}%){alert}")

    print(f"{'=' * 50}")


def export_report(expenses):
    """Export monthly report to text file."""
    year_month = input("Enter month to export (YYYY-MM): ").strip()
    filename = f"expense_report_{year_month}.txt"

    monthly = [e for e in expenses if e["date"].startswith(year_month)]
    if not monthly:
        print(f"📭 No expenses for {year_month}.")
        return

    cat_totals = defaultdict(float)
    for e in monthly:
        cat_totals[e["category"]] += e["amount"]

    total = sum(cat_totals.values())

    with open(filename, "w") as f:
        f.write(f"Expense Report - {year_month}\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Total Spent: ${total:.2f}\n")
        f.write(f"Transactions: {len(monthly)}\n\n")
        f.write("Category Breakdown:\n")
        for cat, amount in sorted(cat_totals.items(), key=lambda x: -x[1]):
            pct = (amount / total) * 100
            f.write(f"  {cat:<15} ${amount:>8.2f}  ({pct:.1f}%)\n")
        f.write("\nTransactions:\n")
        for e in sorted(monthly, key=lambda x: x["date"]):
            f.write(f"  {e['date']}  {e['category']:<12} ${e['amount']:>7.2f}  {e['note']}\n")

    print(f"📤 Report exported to {filename}")


def main():
    """Main application loop."""
    expenses = load_expenses()
    budgets = {}

    print("=" * 50)
    print("💸 EXPENSE TRACKER")
    print("=" * 50)

    while True:
        print("\n📂 Menu:")
        print("  1. ➕ Add expense")
        print("  2. 📋 View expenses")
        print("  3. 💰 Set budgets")
        print("  4. 📊 Monthly summary")
        print("  5. 📤 Export report")
        print("  6. 🚪 Exit")

        choice = input("\nChoose (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            budgets = set_budgets(expenses)
        elif choice == "4":
            monthly_summary(expenses, budgets)
        elif choice == "5":
            export_report(expenses)
        elif choice == "6":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
