import random

class DicePool:
    def __init__(self):
        self.pool = random.choices(range(1, 7), k=6)
        self.selected = []
        print("Welcome to the dice game! Your goal is to get the lowest score.")
        print("3 count as 0 in the final score. If you manage to get all 6 then your score is -1")
        print("You must pick at least 1 die to keep, and the rest will be rerolled. If you pick 0 you must take at least 2 next turn")

    def pick_dice(self):
        """Allows the player to pick dice and reroll the remaining ones."""
        penalty_pick = 0
        while self.pool:
            print(f"Available dice: {self.pool}")
            try:
                if penalty_pick == 1:
                    print("You have to pick at least 2 dice this round")
                    picks = input("Enter the positions of dice to keep (comma-separated, e.g., 1,3,5): ")
                    picks = [int(p) - 1 for p in picks.split(",")]  # Convert to zero-based index

                    if not picks or any(p < 0 or p >= len(self.pool) for p in picks):
                        print("Invalid selection. Choose valid dice positions.")
                        continue

                    if len(picks) < 2:
                        print("You have to take at least 2 dice this turn")
                        continue

                    if len(self.pool) - len(picks) == 1:
                        self.selected.extend(self.pool[p] for p in picks)
                        self.selected.extend(random.choices(range(1, 7), k=1))
                        self.pool = []

                    else:
                        # Add selected dice to the chosen list
                        self.selected.extend(self.pool[p] for p in picks)

                        # Reroll remaining dice
                        self.pool = random.choices(range(1, 7), k=len(self.pool) - len(picks))

                    penalty_pick = 0

                else:
                    picks = input("Enter 0 to re-roll the pool (you must pick 2 dice next turn) or Enter the positions of dice to keep (comma-separated, e.g., 1,3,5): ")

                    if picks == '0' and len(self.pool) > 2:
                        self.pool = random.choices(range(1, 7), k=len(self.pool))
                        penalty_pick = 1
                        print("You have chosen not to pick any dice. You will have to pick at least 2 next round")

                    elif picks == '0' and len(self.pool) == 2:
                        self.selected.extend(random.choices(range(1, 7), k=2))
                        self.pool = []

                    else:
                        picks = [int(p) - 1 for p in picks.split(",")]  # Convert to zero-based index
                        
                        if not picks or any(p < 0 or p >= len(self.pool) for p in picks):
                            print("Invalid selection. Choose valid dice positions.")
                            continue
                        
                        if len(self.pool) - len(picks) == 1:
                            self.selected.extend(self.pool[p] for p in picks)
                            self.selected.extend(random.choices(range(1, 7), k=1))
                            self.pool = []
                        else:
                            # Add selected dice to the chosen list
                            self.selected.extend(self.pool[p] for p in picks)

                            # Reroll remaining dice
                            self.pool = random.choices(range(1, 7), k=len(self.pool) - len(picks))

                print(f"Selected dice: {self.selected}")
            except ValueError:
                print("Invalid input. Please enter numbers separated by commas.")

        # Game Over - Display final score
        if sum(self.selected) == 36:
            print("Game over! You have managed to get all sixes and your total score is -1")
        else:
            dice_sum = 0
            for dice in self.selected:
                if dice == 3:
                    continue
                else:
                    dice_sum += dice
            print(f"Game over! Your final score is {dice_sum}.")

# Run the game
if __name__ == "__main__":
    game = DicePool()
    game.pick_dice()