import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
row = 0
score = 0

for i in range(16):
    board_row = input()
    # print(board_row)
    ise = True
    for x in board_row:
        if x != '#':  # TODO: use .count('#')
            ise = False
    if ise:
        score += 100
        row += 1
    else:
        row = 0

    if row == 4:
        score += 400
        row = 0


print(score)