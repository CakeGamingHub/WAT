from Player import *

class HumanPlayer(Player):
    def GetMove(self, Board):
        try:
            Move = []
            Move.append(int(input("Which row will you affect? ")))
            Move.append(int(input("How many pieces will you remove? ")))

            if not Board.ValidateMove(Board, Move[0], Move[1]): raise ValueError
            return Move
        except Exception as e:
            print(e)
            print("Please insert valid move.")
            return self.GetMove(Board)
