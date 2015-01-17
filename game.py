"""
This is a module that creates a chess game
"""
import sys
import players

try:
    black_name = raw_input("Enter a name for black: ")
except EOFError:
    print
    print "Program is quitting..."
    sys.exit()

try:
    white_name = raw_input("Enter a name for white: ")
except EOFError:
    print
    print "Program is quitting..."
    sys.exit()


white = players.Player(white_name, "white")
black = players.Player(black_name, "black")

ended = False
turn = "w"

while not ended:
    if turn == "w":
        move = raw_input("Move for white: ")
        move_coord = parse_move(move)
        if not is_valid_move(move_coord):
            continue

        turn = "b"
    elif turn == "b":
        move = raw_input("Move for black: ")
        move_coord = parse_move(move)
        if not is_valid_move(move_coord):
            continue

        turn = "w"
    else:
        print "Fatal Error. Contact creator"

