from __future__ import annotations

import json
import random
from pathlib import Path

try:
    from rich import print
except ImportError:
    pass


def load_data() -> list[list[str]]:
    capitals_file = Path(__file__).parent / "capitals.json"
    states_capitals = json.load(open(capitals_file))

    return states_capitals


def main() -> int:
    states_capitals = load_data()

    correct = 0
    questions = 10
    states_capitals_choices = random.sample(states_capitals, k=questions)
    for k, state_capital in enumerate(states_capitals_choices):
        state, capital = state_capital

        if random.random() < 0.5:
            print(
                f"{k+1}: Which state has the capital: [bold blue]{capital}[/bold blue]?"
            )
            user_state = input()
            if state.lower() == user_state.lower():
                correct += 1
                print("good job!")
            else:
                print(f"bad job :( the correct answer is [bold red]{state}[/bold red]")
        else:
            print(f"{k+1}: What is the capital of: [bold blue]{state}[/bold blue]?")
            user_capital = input()
            if capital.lower() == user_capital.lower():
                correct += 1
                print("good job!")
            else:
                print(
                    f"bad job :( the correct answer is [bold red]{capital}[/bold red]"
                )

    print(f"you got {correct/questions*100}% correct")

    return 0


if __name__ == "__main__":
    SystemExit(main())
