"""
This is a module with the classes for a chess game
"""
import sys

def die(text):
    sys.exit(text)

class Pawn:
    """The class for a pawn"""
    def __init__(self, color, column):
        # black or white
        self.color = color

        # number of moves so far
        self.moves = 0

        # Determines the moveset the piece will move in
######### En passant and capturing have not been made yet #################
        if color == "white":
            self.moveset = (0, 1),
        elif color == "black":
            self.moveset = (0, -1),
        else:
            die("Choose white or black for the Pawn!")

        # Which square does this pawn start on?
        valid_columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] 
        if not column in valid_columns:
            die("Choose a valid column a - h!")
        elif self.color == "white":
            self.start = column + "2"
        elif self.color == "black":
            self.start = column + "7"
        else:
            die("Impossibility in Pawn class!")

        self.current = self.start

class Rook:
    """The class for a rook"""
    def __init__(self, color, column):
        # black or white
        if color == "white" or color == "black":
            self.color = color
        else:
            die("Choose a valid color for the rook!")

        # number of moves so far
        self.moves = 0

        # Determines the pattern the piece will move in
        # They are made explicit here for clarity
        self.moveset = (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),\
                       (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6),\
                       (0, -7), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), \
                       (6, 0), (7, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0), \
                       (-5, 0), (-6, 0), (-7, 0)

        # Which square does this rook start on?
        if not column == 'a' and not column == 'h':
            die("Choose a valid column a or h!")
        elif self.color == "white":
            self.start = column + "1"
        elif self.color == "black":
            self.start = column + "8"
        else:
            die("Impossibility in Rook class!")

        self.current = self.start

class Knight:
    """The class for a knight"""
    def __init__(self, color, column):
        # black or white
        if color == "white" or color == "black":
            self.color = color
        else:
            die("Choose a valid color for the knight!")

        # number of moves so far
        self.moves = 0

        # Determines the pattern the piece will move in
        # They are made explicit here for clarity
        self.moveset = (1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2),\
                       (-2, 1), (-2, -1)

        # Which square does this knight start on?
        if not column == 'b' and not column == 'g':
            die("Choose a valid column a - h!")
        elif self.color == "white":
            self.start = column + "1"
        elif self.color == "black":
            self.start = column + "8"
        else:
            die("Impossibility in Knight class!")
            
        self.current = self.start

class Bishop:
    """The class for a Bishop"""
    def __init__(self, color, column):
        # black or white
        if color == "white" or color == "black":
            self.color = color
        else:
            die("Choose a valid color for the bishop!")

        # number of moves so far
        self.moves = 0

        # Determines the pattern the piece will move in
        # They are made explicit here for clarity
        self.moveset = (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),\
                       (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6),\
                       (7, -7), (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5),\
                       (-6, 6), (-7, 7), (-1, -1), (-2, -2), (-3, -3),\
                       (-4, -4), (-5, -5), (-6, -6), (-7, -7)


        # Which square does this bishop start on?
        if not column == 'c' and not column == 'f':
            die("Choose a valid column a - h!")
        elif self.color == "white":
            self.start = column + "1"
        elif self.color == "black":
            self.start = column + "8"
        else:
            die("Impossibility in Bishop class!")

        self.current = self.start

class Queen:
    """The class for a Queen"""
    def __init__(self, color):
        # black or white
        if color == "white" or color == "black":
            self.color = color
        else:
            die("Choose a valid color for the queen!")

        # number of moves so far
        self.moves = 0

        # Determines the pattern the piece will move in
        # They are made explicit here for clarity. 
        # A queen is just a combination of a bishop and a rook
        self.moveset = (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),\
                       (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6),\
                       (7, -7), (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5),\
                       (-6, 6), (-7, 7), (-1, -1), (-2, -2), (-3, -3),\
                       (-4, -4), (-5, -5), (-6, -6), (-7, -7),\
                       (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),\
                       (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6),\
                       (0, -7), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),\
                       (6, 0), (7, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0),\
                       (-5, 0), (-6, 0), (-7, 0)

        if color == "white":
            self.start = "d1"
        elif color == "black":
            self.start = "d8"
        else:
            die("Impossibility in Queen class!")

        self.current = self.start

class King:
    """The class for a King"""
    def __init__(self, color):
        # black or white
        if color == "white" or color == "black":
            self.color = color
        else:
            die("Choose a valid color for the king!")

        # number of moves so far
        self.moves = 0

        # Determines the pattern the piece will move in
        # They are made explicit here for clarity. 
        self.moveset = (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1),\
                       (0, -1), (1, -1)
        
        if color == "white":
            self.start = "e1"
        elif color == "black":
            self.start = "e8"
        else:
            die("Impossibility in King class!")

        self.current = self.start
