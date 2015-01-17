"""
This module contains players for a chess game
"""
from chess import *

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

        self.pawn_a = Pawn(color, "a")
        self.pawn_b = Pawn(color, "b")
        self.pawn_c = Pawn(color, "c")
        self.pawn_d = Pawn(color, "d")
        self.pawn_e = Pawn(color, "e")
        self.pawn_f = Pawn(color, "f")
        self.pawn_g = Pawn(color, "g")
        self.pawn_h = Pawn(color, "h")

        self.rook_a = Rook(color, "a")
        self.rook_h = Rook(color, "h")

        self.knight_b = Knight(color, "b")
        self.knight_g = Knight(color, "g")

        self.bishop_c = Bishop(color, "c")
        self.bishop_d = Bishop(color, "f")

        self.queen = Queen(color, "d")
        self.king = King(color, "e")
