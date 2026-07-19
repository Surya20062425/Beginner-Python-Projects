"""
To-Do List CLI App
Difficulty: Easy
Concepts: Lists, Dictionaries, File I/O, JSON
"""

import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("📋 TO-DO LIST MANAGER")
    print("=" * 40)
    print("1. ➕ Add a task")
    print("2. ✅ Mark task as done")
    print("3. 🗑️  Delete a task")
    print("4. 📋 List all tasks")
    print("5. 🚪 Exit")
    print("=" * 40)


def list_tasks(tasks):
    """Display all tasks with status indicators."""
    if not tasks:
        print("\n📭 No tasks found. Add one!")
        return

    print("\n" + "-" * 40)
    print(f"{'ID':<5}{'Status':<10}{'Task'}")
    print("-" * 40)

    for i, task in enumerate(tasks, 1):
        status = "✅ Done" if task["done"] else "⏳ Todo"
        print(f"{i:<5}{status:<10}{task['title']}")

    print("-" * 40)
    done_count = sum(1 for t in tasks if t["done"])
    print(f"Progress: {done_count}/{len(tasks)} completed")


def add_task(tasks):
    """Add a new task."""
    title = input("\nEnter task description: ").strip()
    if not title:
        print("❌ Task cannot be empty!")
        return

    task = {
        "title": title,
        "done": False,
        "created_at": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: \"{title}\"")


def mark_done(tasks):
    """Mark a task as completed."""
    list_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("\nEnter task number to mark done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            save_tasks(tasks)
            print(f"✅ Marked as done: \"{tasks[choice - 1]['title']}\"")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def delete_task(tasks):
    """Delete a task."""
    list_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("\nEnter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"🗑️  Deleted: \"{removed['title']}\"")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def main():
    """Main application loop."""
    tasks = load_tasks()
    print("🎉 Welcome to your To-Do List!")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            mark_done(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            list_tasks(tasks)
        elif choice == "5":
            print("\n👋 Goodbye! Your tasks are saved.")
            break
        else:
            print("❌ Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()
