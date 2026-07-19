"""
Quiz App
Difficulty: Medium
Concepts: Classes, JSON, time module
"""

import json
import os
import time
from datetime import datetime, timedelta

QUESTIONS_FILE = "quiz_questions.json"
SCORES_FILE = "quiz_scores.json"

# Default questions if file doesn't exist
DEFAULT_QUESTIONS = [
    {
        "category": "Science",
        "question": "What planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": 1
    },
    {
        "category": "Science",
        "question": "What is the chemical symbol for water?",
        "options": ["HO", "H2O", "O2H", "H2"],
        "answer": 1
    },
    {
        "category": "History",
        "question": "In which year did World War II end?",
        "options": ["1943", "1944", "1945", "1946"],
        "answer": 2
    },
    {
        "category": "History",
        "question": "Who was the first President of the United States?",
        "options": ["Thomas Jefferson", "John Adams", "George Washington", "Benjamin Franklin"],
        "answer": 2
    },
    {
        "category": "Tech",
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Personal Unit", "Central Processor Unit", "Central Process Unit"],
        "answer": 0
    },
    {
        "category": "Tech",
        "question": "Which programming language is known as the 'language of the web'?",
        "options": ["Python", "Java", "JavaScript", "C++"],
        "answer": 2
    },
]


class Question:
    """Represents a single quiz question."""

    def __init__(self, data):
        self.category = data["category"]
        self.question = data["question"]
        self.options = data["options"]
        self.answer = data["answer"]

    def ask(self, question_num, total):
        """Display question and get user answer with timer."""
        print(f"\n{'─' * 50}")
        print(f"  Question {question_num}/{total}  |  Category: {self.category}")
        print(f"{'─' * 50}")
        print(f"  {self.question}\n")

        for i, opt in enumerate(self.options):
            print(f"  {i + 1}. {opt}")

        print(f"\n  ⏱️  Time limit: 15 seconds")
        start_time = time.time()

        try:
            answer = int(input("\n  Your answer (1-4): ").strip()) - 1
            elapsed = time.time() - start_time

            if elapsed > 15:
                print(f"  ⏰ Time's up! (took {elapsed:.1f}s)")
                return False, elapsed

            if answer == self.answer:
                print(f"  ✅ Correct! ({elapsed:.1f}s)")
                return True, elapsed
            else:
                print(f"  ❌ Wrong! Correct: {self.options[self.answer]}")
                return False, elapsed

        except (ValueError, IndexError):
            elapsed = time.time() - start_time
            print(f"  ❌ Invalid answer!")
            return False, elapsed


class Quiz:
    """Manages the quiz session."""

    def __init__(self, questions):
        self.questions = [Question(q) for q in questions]
        self.score = 0
        self.total_time = 0
        self.category_scores = {}
        self.category_totals = {}

    def run(self):
        """Run the full quiz."""
        print("=" * 50)
        print("🎯 QUIZ TIME!")
        print("=" * 50)
        print(f"Total questions: {len(self.questions)}")
        print("You have 15 seconds per question.\n")
        input("Press Enter to start...")

        for i, q in enumerate(self.questions, 1):
            correct, elapsed = q.ask(i, len(self.questions))
            self.total_time += elapsed

            cat = q.category
            self.category_totals[cat] = self.category_totals.get(cat, 0) + 1
            if correct:
                self.score += 1
                self.category_scores[cat] = self.category_scores.get(cat, 0) + 1

        return self.get_results()

    def get_results(self):
        """Compile and return results."""
        percentage = (self.score / len(self.questions)) * 100
        return {
            "score": self.score,
            "total": len(self.questions),
            "percentage": percentage,
            "time": self.total_time,
            "category_breakdown": {
                cat: {
                    "correct": self.category_scores.get(cat, 0),
                    "total": self.category_totals[cat]
                }
                for cat in self.category_totals
            }
        }


def load_questions():
    """Load questions from file or use defaults."""
    if os.path.exists(QUESTIONS_FILE):
        try:
            with open(QUESTIONS_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass

    # Create default questions file
    with open(QUESTIONS_FILE, "w") as f:
        json.dump(DEFAULT_QUESTIONS, f, indent=2)
    return DEFAULT_QUESTIONS


def save_score(results, player_name):
    """Save score to leaderboard."""
    scores = []
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, "r") as f:
                scores = json.load(f)
        except json.JSONDecodeError:
            scores = []

    scores.append({
        "player": player_name,
        "score": results["score"],
        "total": results["total"],
        "percentage": results["percentage"],
        "time": round(results["time"], 1),
        "date": datetime.now().isoformat()
    })

    # Keep top 10
    scores.sort(key=lambda x: (x["percentage"], -x["time"]), reverse=True)
    scores = scores[:10]

    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)


def show_leaderboard():
    """Display high scores."""
    if not os.path.exists(SCORES_FILE):
        print("\n📭 No scores yet. Be the first!")
        return

    try:
        with open(SCORES_FILE, "r") as f:
            scores = json.load(f)
    except json.JSONDecodeError:
        return

    print("\n" + "=" * 55)
    print("🏆 LEADERBOARD — Top 10")
    print("=" * 55)
    print(f"  {'Rank':<6}{'Player':<15}{'Score':<10}{'Time':<10}{'Date'}")
    print("-" * 55)

    for i, s in enumerate(scores, 1):
        medal = {1: "🥇", 2: "🥈", 3: "🥉"}.get(i, "  ")
        date_str = s["date"][:10]
        print(f"  {medal} #{i:<3}{s['player'][:13]:<15}{s['score']}/{s['total']:<6}{s['time']}s{'':<4}{date_str}")
    print("=" * 55)


def show_results(results):
    """Display quiz results."""
    print("\n" + "=" * 50)
    print("📊 QUIZ RESULTS")
    print("=" * 50)
    print(f"  Score:        {results['score']}/{results['total']}")
    print(f"  Percentage:   {results['percentage']:.1f}%")
    print(f"  Time:         {results['time']:.1f} seconds")
    print(f"  Avg/Question: {results['time']/results['total']:.1f}s")
    print("-" * 50)

    if results["category_breakdown"]:
        print("  Category Breakdown:")
        for cat, data in results["category_breakdown"].items():
            pct = (data["correct"] / data["total"]) * 100
            bar = "█" * int(pct / 10) + "░" * (10 - int(pct / 10))
            print(f"    {cat:<12} {bar}  {data['correct']}/{data['total']} ({pct:.0f}%)")

    print("=" * 50)

    if results["percentage"] >= 80:
        print("  🌟 Excellent work!")
    elif results["percentage"] >= 60:
        print("  👍 Good job!")
    elif results["percentage"] >= 40:
        print("  📚 Keep practicing!")
    else:
        print("  💪 Don't give up!")


def main():
    """Main application loop."""
    questions = load_questions()

    print("=" * 50)
    print("🧠 PYTHON QUIZ APP")
    print("=" * 50)

    while True:
        print("\n📂 Menu:")
        print("  1. 🎯 Start Quiz")
        print("  2. 🏆 View Leaderboard")
        print("  3. 🚪 Exit")

        choice = input("\nChoose (1-3): ").strip()

        if choice == "1":
            name = input("\nEnter your name: ").strip() or "Anonymous"
            quiz = Quiz(questions)
            results = quiz.run()
            show_results(results)
            save_score(results, name)

        elif choice == "2":
            show_leaderboard()

        elif choice == "3":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
