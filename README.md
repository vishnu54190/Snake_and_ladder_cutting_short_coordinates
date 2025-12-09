This is a simple Snake and Ladder–style game implemented in Python.
The game uses a 4×4 board with positions numbered from 1 to 16.
There are 4 players, all starting at position 0, and the first player to reach position 16 wins.

The dice rolls are generated using Python’s random module.

Additional Rule

If a player lands on a position where another player is already standing,
the earlier player is sent back to position 0, and their 2D coordinate becomes (0,0).

The program prints the following details for each player:

Dice roll history

Position history

2D coordinate history based on the board layout

Win status
