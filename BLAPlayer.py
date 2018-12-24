from Player import *
from random import randint

class BLAPlayer(Player):
    UnwantedStates = []

    def GetMove(self, Board):
        try:
            Move = []
            Move.append(randint(0, 3))
            Move.append(randint(0, Move[0]+4))

            if not Board.ValidateMove(Board, Move[0], Move[1]): raise ValueError
            return Move
        except Exception as e:
            return self.GetMove(Board)
