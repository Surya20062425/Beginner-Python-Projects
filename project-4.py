"""
Unit Converter
Difficulty: Easy
Concepts: Functions, Dictionaries, Input Validation
"""


def length_converter():
    """Handle length conversions."""
    conversions = {
        "1": ("Meters to Feet", 3.28084),
        "2": ("Feet to Meters", 1 / 3.28084),
        "3": ("Kilometers to Miles", 0.621371),
        "4": ("Miles to Kilometers", 1 / 0.621371),
        "5": ("Centimeters to Inches", 0.393701),
        "6": ("Inches to Centimeters", 1 / 0.393701),
    }

    print("\n📏 Length Conversions:")
    for key, (name, _) in conversions.items():
        print(f"  {key}. {name}")

    choice = input("\nSelect conversion (1-6): ").strip()
    if choice not in conversions:
        print("❌ Invalid choice.")
        return

    name, factor = conversions[choice]
    try:
        value = float(input(f"Enter value in {name.split(' to ')[0]}: "))
        result = value * factor
        print(f"\n✅ {value:.2f} {name.split(' to ')[0]} = {result:.2f} {name.split(' to ')[1]}")
    except ValueError:
        print("❌ Please enter a valid number.")


def weight_converter():
    """Handle weight conversions."""
    conversions = {
        "1": ("Kilograms to Pounds", 2.20462),
        "2": ("Pounds to Kilograms", 1 / 2.20462),
        "3": ("Grams to Ounces", 0.035274),
        "4": ("Ounces to Grams", 1 / 0.035274),
    }

    print("\n⚖️  Weight Conversions:")
    for key, (name, _) in conversions.items():
        print(f"  {key}. {name}")

    choice = input("\nSelect conversion (1-4): ").strip()
    if choice not in conversions:
        print("❌ Invalid choice.")
        return

    name, factor = conversions[choice]
    try:
        value = float(input(f"Enter value in {name.split(' to ')[0]}: "))
        result = value * factor
        print(f"\n✅ {value:.2f} {name.split(' to ')[0]} = {result:.2f} {name.split(' to ')[1]}")
    except ValueError:
        print("❌ Please enter a valid number.")


def temperature_converter():
    """Handle temperature conversions."""
    print("\n🌡️  Temperature Conversions:")
    print("  1. Celsius → Fahrenheit")
    print("  2. Fahrenheit → Celsius")
    print("  3. Celsius → Kelvin")
    print("  4. Kelvin → Celsius")

    choice = input("\nSelect conversion (1-4): ").strip()

    try:
        value = float(input("Enter temperature value: "))

        if choice == "1":
            result = (value * 9 / 5) + 32
            print(f"\n✅ {value:.2f}°C = {result:.2f}°F")
        elif choice == "2":
            result = (value - 32) * 5 / 9
            print(f"\n✅ {value:.2f}°F = {result:.2f}°C")
        elif choice == "3":
            result = value + 273.15
            print(f"\n✅ {value:.2f}°C = {result:.2f}K")
        elif choice == "4":
            result = value - 273.15
            print(f"\n✅ {value:.2f}K = {result:.2f}°C")
        else:
            print("❌ Invalid choice.")
    except ValueError:
        print("❌ Please enter a valid number.")


def currency_converter():
    """Handle currency conversions using fixed rates."""
    rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.79,
        "JPY": 150.25,
        "INR": 83.12,
        "CAD": 1.35,
        "AUD": 1.52,
    }

    print("\n💱 Supported Currencies:", ", ".join(rates.keys()))

    try:
        amount = float(input("\nEnter amount: "))
        from_curr = input("From currency (e.g., USD): ").strip().upper()
        to_curr = input("To currency (e.g., EUR): ").strip().upper()

        if from_curr not in rates or to_curr not in rates:
            print("❌ Unsupported currency.")
            return

        # Convert to USD first, then to target
        usd_amount = amount / rates[from_curr]
        result = usd_amount * rates[to_curr]

        print(f"\n✅ {amount:.2f} {from_curr} = {result:.2f} {to_curr}")
        print(f"   (Rate: 1 {from_curr} = {rates[to_curr] / rates[from_curr]:.4f} {to_curr})")
    except ValueError:
        print("❌ Please enter a valid amount.")


def main():
    """Main menu loop."""
    print("=" * 45)
    print("🔄 UNIT CONVERTER")
    print("=" * 45)

    while True:
        print("\n📂 Categories:")
        print("  1. 📏 Length")
        print("  2. ⚖️  Weight")
        print("  3. 🌡️  Temperature")
        print("  4. 💱 Currency")
        print("  5. 🚪 Exit")

        choice = input("\nSelect category (1-5): ").strip()

        try:
            if choice == "1":
                length_converter()
            elif choice == "2":
                weight_converter()
            elif choice == "3":
                temperature_converter()
            elif choice == "4":
                currency_converter()
            elif choice == "5":
                print("\n👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please select 1-5.")
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
