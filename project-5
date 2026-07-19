"""
Rock Paper Scissors
Difficulty: Easy
Concepts: random, Conditionals, Score Tracking
"""

import random
from enum import Enum


class Choice(Enum):
    """Enum for game choices."""
    ROCK = "🪨 Rock"
    PAPER = "📄 Paper"
    SCISSORS = "✂️  Scissors"


CHOICE_MAP = {
    "r": Choice.ROCK,
    "p": Choice.PAPER,
    "s": Choice.SCISSORS,
}


def get_computer_choice():
    """Randomly select computer's choice."""
    return random.choice(list(Choice))


def get_player_choice():
    """Get and validate player's choice."""
    while True:
        print("\nYour move: [r]ock | [p]aper | [s]cissors | [q]uit")
        move = input("Choose: ").strip().lower()

        if move in ("q", "quit"):
            return None
        if move in CHOICE_MAP:
            return CHOICE_MAP[move]
        print("❌ Invalid choice. Use r, p, s, or q.")


def determine_winner(player, computer):
    """Determine round winner. Returns: 'player', 'computer', or 'tie'."""
    if player == computer:
        return "tie"

    beats = {
        Choice.ROCK: Choice.SCISSORS,
        Choice.PAPER: Choice.ROCK,
        Choice.SCISSORS: Choice.PAPER,
    }

    return "player" if beats[player] == computer else "computer"


def play_match(best_of=5):
    """Play a best-of-N match."""
    wins_needed = (best_of // 2) + 1
    player_wins = 0
    computer_wins = 0
    ties = 0
    round_num = 0

    print("=" * 50)
    print(f"🎮 ROCK PAPER SCISSORS — Best of {best_of}")
    print(f"   First to {wins_needed} wins!")
    print("=" * 50)

    while player_wins < wins_needed and computer_wins < wins_needed:
        round_num += 1
        print(f"\n📌 Round {round_num}")
        print("-" * 30)

        player_choice = get_player_choice()
        if player_choice is None:
            print("\n🏳️  Match abandoned.")
            return None

        computer_choice = get_computer_choice()

        print(f"   You:      {player_choice.value}")
        print(f"   Computer: {computer_choice.value}")

        result = determine_winner(player_choice, computer_choice)

        if result == "tie":
            ties += 1
            print("   🤝 It's a tie!")
        elif result == "player":
            player_wins += 1
            print("   🎉 You win this round!")
        else:
            computer_wins += 1
            print("   😢 Computer wins this round!")

        print(f"\n   Score: You {player_wins} | Computer {computer_wins} | Ties {ties}")

    return {
        "player_wins": player_wins,
        "computer_wins": computer_wins,
        "ties": ties,
        "total_rounds": round_num,
    }


def show_final_scoreboard(stats):
    """Display match results."""
    print("\n" + "=" * 50)
    print("🏆 FINAL SCOREBOARD")
    print("=" * 50)
    print(f"   Total Rounds: {stats['total_rounds']}")
    print(f"   Your Wins:    {stats['player_wins']}")
    print(f"   Computer Wins:{stats['computer_wins']}")
    print(f"   Ties:         {stats['ties']}")
    print("-" * 50)

    if stats["player_wins"] > stats["computer_wins"]:
        print("   🎉 YOU WIN THE MATCH!")
    else:
        print("   😢 Computer wins the match. Better luck next time!")
    print("=" * 50)


def main():
    """Main game loop."""
    print("Welcome to Rock Paper Scissors!")

    while True:
        stats = play_match(best_of=5)
        if stats:
            show_final_scoreboard(stats)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\n👋 Thanks for playing!")
            break


if __name__ == "__main__":
    main()
