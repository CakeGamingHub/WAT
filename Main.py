from Board import *
from HumanPlayer import *

GameBoard = Board()

#GB = Board()
#GB.OutputBoard()
#print("------------------------")
#GB.MakeMove(0, 1)
#GB.OutputBoard()
#print("------------------------")
#GB.MakeMove(3, 2)
#GB.OutputBoard()

Player1 = HumanPlayer()
CurrentMove = Player1.GetMove(Board)
Board.MakeMove(Board, CurrentMove[0], CurrentMove[1])
Board.OutputBoard(Board)
Player2 = "Blind"

