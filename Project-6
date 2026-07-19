"""
Contact Book
Difficulty: Medium
Concepts: File I/O, JSON/CSV, Search, Classes
"""

import json
import os
import re
import csv
from datetime import datetime

DATA_FILE = "contacts.json"


class Contact:
    """Represents a single contact."""

    def __init__(self, name, phone, email, address=""):
        self.name = name.strip()
        self.phone = phone.strip()
        self.email = email.strip().lower()
        self.address = address.strip()
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data):
        c = cls(data["name"], data["phone"], data["email"], data.get("address", ""))
        c.created_at = data.get("created_at", datetime.now().isoformat())
        return c

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email}"


class ContactBook:
    """Manages a collection of contacts."""

    def __init__(self):
        self.contacts = []
        self.load()

    def load(self):
        """Load contacts from JSON file."""
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    data = json.load(f)
                    self.contacts = [Contact.from_dict(c) for c in data]
            except (json.JSONDecodeError, KeyError):
                self.contacts = []

    def save(self):
        """Save contacts to JSON file."""
        with open(DATA_FILE, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=2)

    def add(self, contact):
        """Add a new contact."""
        self.contacts.append(contact)
        self.save()
        print(f"✅ Added: {contact.name}")

    def search(self, query):
        """Search contacts by name (partial match, case-insensitive)."""
        query = query.lower()
        return [c for c in self.contacts if query in c.name.lower()]

    def list_all(self):
        """Return all contacts sorted alphabetically."""
        return sorted(self.contacts, key=lambda c: c.name.lower())

    def delete(self, index):
        """Delete contact by index."""
        if 0 <= index < len(self.contacts):
            removed = self.contacts.pop(index)
            self.save()
            return removed
        return None

    def update(self, index, **kwargs):
        """Update contact fields."""
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            for key, value in kwargs.items():
                if value:
                    setattr(contact, key, value.strip())
            self.save()
            return contact
        return None

    def export_csv(self, filename="contacts_export.csv"):
        """Export contacts to CSV."""
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "phone", "email", "address"])
            writer.writeheader()
            for c in self.contacts:
                writer.writerow({"name": c.name, "phone": c.phone, "email": c.email, "address": c.address})
        print(f"📤 Exported to {filename}")

    def import_csv(self, filename):
        """Import contacts from CSV."""
        try:
            with open(filename, "r", newline="") as f:
                reader = csv.DictReader(f)
                count = 0
                for row in reader:
                    if row.get("name") and row.get("phone"):
                        self.contacts.append(Contact(row["name"], row["phone"], row.get("email", ""), row.get("address", "")))
                        count += 1
                self.save()
                print(f"📥 Imported {count} contacts from {filename}")
        except FileNotFoundError:
            print(f"❌ File not found: {filename}")


def validate_phone(phone):
    """Basic phone validation."""
    cleaned = re.sub(r"[^\d+\-\s()]", "", phone)
    return len(cleaned) >= 7


def validate_email(email):
    """Basic email validation."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def display_contacts(contacts, title="Contacts"):
    """Display contacts in a formatted table."""
    if not contacts:
        print("📭 No contacts found.")
        return

    print(f"\n{'─' * 70}")
    print(f"  {title} ({len(contacts)} total)")
    print(f"{'─' * 70}")
    print(f"  {'#':<4}{'Name':<20}{'Phone':<18}{'Email'}")
    print(f"{'─' * 70}")
    for i, c in enumerate(contacts):
        print(f"  {i + 1:<4}{c.name[:18]:<20}{c.phone[:16]:<18}{c.email[:25]}")
    print(f"{'─' * 70}")


def add_contact(book):
    """Interactive add contact flow."""
    print("\n➕ Add New Contact")
    name = input("Name: ").strip()
    if not name:
        print("❌ Name is required.")
        return

    phone = input("Phone: ").strip()
    if not validate_phone(phone):
        print("⚠️  Phone number seems invalid. Continuing anyway...")

    email = input("Email: ").strip()
    if email and not validate_email(email):
        print("⚠️  Email format seems invalid. Continuing anyway...")

    address = input("Address (optional): ").strip()

    book.add(Contact(name, phone, email, address))


def edit_contact(book):
    """Interactive edit contact flow."""
    contacts = book.list_all()
    display_contacts(contacts)
    if not contacts:
        return

    try:
        idx = int(input("\nEnter contact number to edit: ")) - 1
        if 0 <= idx < len(contacts):
            print("\nLeave blank to keep current value.")
            name = input(f"Name [{contacts[idx].name}]: ").strip()
            phone = input(f"Phone [{contacts[idx].phone}]: ").strip()
            email = input(f"Email [{contacts[idx].email}]: ").strip()
            address = input(f"Address [{contacts[idx].address}]: ").strip()

            book.update(idx, name=name or contacts[idx].name,
                        phone=phone or contacts[idx].phone,
                        email=email or contacts[idx].email,
                        address=address or contacts[idx].address)
            print("✅ Contact updated.")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def delete_contact(book):
    """Interactive delete contact flow."""
    contacts = book.list_all()
    display_contacts(contacts)
    if not contacts:
        return

    try:
        idx = int(input("\nEnter contact number to delete: ")) - 1
        removed = book.delete(idx)
        if removed:
            print(f"🗑️  Deleted: {removed.name}")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def search_contacts(book):
    """Search contacts by name."""
    query = input("\n🔍 Search by name: ").strip()
    if query:
        results = book.search(query)
        display_contacts(results, f"Search results for '{query}'")


def main():
    """Main application loop."""
    book = ContactBook()
    print("=" * 50)
    print("📇 CONTACT BOOK")
    print("=" * 50)

    while True:
        print("\n📂 Menu:")
        print("  1. ➕ Add contact")
        print("  2. 📋 List all contacts")
        print("  3. 🔍 Search contacts")
        print("  4. ✏️  Edit contact")
        print("  5. 🗑️  Delete contact")
        print("  6. 📤 Export to CSV")
        print("  7. 📥 Import from CSV")
        print("  8. 🚪 Exit")

        choice = input("\nChoose (1-8): ").strip()

        if choice == "1":
            add_contact(book)
        elif choice == "2":
            display_contacts(book.list_all())
        elif choice == "3":
            search_contacts(book)
        elif choice == "4":
            edit_contact(book)
        elif choice == "5":
            delete_contact(book)
        elif choice == "6":
            book.export_csv()
        elif choice == "7":
            filename = input("CSV filename to import: ").strip()
            book.import_csv(filename)
        elif choice == "8":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
