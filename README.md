# python_dice_game
A simple dice game I often play with my friends in a digital form
## How to play
Your goal is to get the lowest score possible from rolling and selecting dice

First you will start with a pool of 6 dice

In a turn you can do the following:

1.Pick at least 1 dice and re-roll the rest

2.Re-roll the pool but take at least 2 dice next turn. You can only to this if you have not done this step the previous turn

## Scoring

3's value is 0 and the rest are summed up by their face value

If you manage to get all 6's then your score is -1 and you beat anyone that has all 3's

Whoever rolls the lowest amount of points wins

## Running the script

No packages are needed to install. Just run the script and you will enter the choices in your terminal
   ```sh
   python dice_game.py
   ```

## Limitations

As of now this game is only single-player and is played in the terminal. There is no way to save or compare scores with others other than reading the console output
