import random
from enum import Enum
from typing import Tuple, Optional, List
import time
from dataclasses import dataclass

class Choice(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"
    QUIT = "quit"

    @classmethod
    def list_choices(cls) -> List[str]:
        return [choice.value for choice in cls if choice != Choice.QUIT]

@dataclass
class GameStats:
    user_score: int = 0
    computer_score: int = 0
    draws: int = 0
    total_games: int = 0

class RockPaperScissors:
    def __init__(self, max_rounds: int = 3):
        self.max_rounds = max_rounds
        self.stats = GameStats()
        self.winning_combinations = {
            (Choice.SCISSORS, Choice.PAPER),
            (Choice.PAPER, Choice.ROCK),
            (Choice.ROCK, Choice.SCISSORS)
        }

    def display_welcome(self) -> None:
        """Display welcome message and game rules."""
        print(f"""
        🎮 Welcome to INATHI'S ROCK PAPER SCISSORS 🎮
        =====================================
        🌟 You have {self.max_rounds} rounds to play!
        🎯 Score points to win
        ❌ Type 'quit' to end the game
        =====================================
        """)

    def get_user_choice(self) -> Choice:
        """Get and validate user input."""
        valid_choices = [choice.value for choice in Choice]
        while True:
            choice = input("\n🎮 Your turn (rock/paper/scissors/quit): ").lower()
            if choice in valid_choices:
                return Choice(choice)
            print("❌ Invalid choice! Please try again.")

    def get_computer_choice(self) -> Choice:
        """Generate computer's choice with a dramatic pause."""
        print("\n🤖 Computer is choosing", end="")
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        choice = random.choice(Choice.list_choices())
        print(f"\n🤖 Computer chose: {choice}")
        return Choice(choice)

    def determine_winner(self, user_choice: Choice, computer_choice: Choice) -> Optional[str]:
        """Determine the winner of the round."""
        if user_choice == computer_choice:
            self.stats.draws += 1
            return None
        elif (user_choice, computer_choice) in self.winning_combinations:
            self.stats.user_score += 1
            return "user"
        else:
            self.stats.computer_score += 1
            return "computer"

    def display_round_result(self, winner: Optional[str]) -> None:
        """Display the result of the round with emoji."""
        if winner is None:
            print("🤝🏾 It's a draw!")
        elif winner == "user":
            print("🎉👊🏿 You won this round!")
        else:
            print("💻 Computer won this round!")

    def display_game_stats(self) -> None:
        """Display current game statistics."""
        stats = f"""
        📊 Game Statistics:
        ==================
        🏆 Your Score: {self.stats.user_score}
        🤖 Computer Score: {self.stats.computer_score}
        🤝🏾 Draws: {self.stats.draws}
        🎮 Games Played: {self.stats.total_games}/{self.max_rounds}
        """
        print(stats)

    def play_round(self) -> bool:
        """Play a single round and return True if the user chooses to quit."""
        user_choice = self.get_user_choice()
        if user_choice == Choice.QUIT:
            print("\n👋🏿 Thanks for playing!")
            return False
            
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, computer_choice)
        self.display_round_result(winner)
        self.stats.total_games += 1
        self.display_game_stats()
        return True

    def play_game(self) -> None:
        """Main game loop."""
        self.display_welcome()
        
        while self.stats.total_games < self.max_rounds:
            if not self.play_round():
                break

        self.display_final_results()

    def display_final_results(self) -> None:
        """Display final game results with ASCII art."""
        final_message = f"""
        🎮 Game Over! 🎮
        ================
        Final Results:
        You: {self.stats.user_score} {'🏆' if self.stats.user_score > self.stats.computer_score else ''}
        Computer: {self.stats.computer_score} {'🏆' if self.stats.computer_score > self.stats.user_score else ''}
        Draws: {self.stats.draws}
        
        {'🎉 Congratulations! You Won!' if self.stats.user_score > self.stats.computer_score else ''}
        {'🤖 Computer Wins!' if self.stats.computer_score > self.stats.user_score else ''}
        {'🤝🏾 Its a Tie!' if self.stats.user_score == self.stats.computer_score else ''}
        """
        print(final_message)


if __name__ == "__main__":
    try:
        game = RockPaperScissors()
        game.play_game()
    except KeyboardInterrupt:
        print("\n👋🏿 Game interrupted. Thanks for playing!")
