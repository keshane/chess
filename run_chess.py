#!/usr/bin/env python
from __future__ import print_function
import chess

a = chess.Pawn("black", 'g')
b = chess.Rook("white", 'h')
c = chess.Knight("black", 'g')
d = chess.Bishop("black", 'c')
e = chess.Queen("white")
f = chess.King("black")

c.current = "a2"

print(c.__dict__)


