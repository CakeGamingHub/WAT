class Board:
    Spaces =    [[True, True, True, True, True, True, True],
                [True, True, True, True, True, True, True],
                [True, True, True, True, True, True, True],
                [True, True, True, True, True, True, True]]

    def ValidateMove(self, Row, NumberOfPieces):
        try:
            print(NumberOfPieces)
            print(self.Spaces[Row].count(True))
            if self.Spaces[Row].count(True) < NumberOfPieces:
                return False
            else: return True
        except: return False

    def MakeMove(self, Row, NumPieces):
        try:
            if not self.ValidateMove(self, Row, NumPieces): return False
            # implicit else
            Count = 0
            while Count < NumPieces:
                TargetIndex = len(self.Spaces[Row])-Count
                self.Spaces[Row][len(self.Spaces[Row])-Count-1] = False
                Count += 1
        except Exception as e:
            #print(Count)
            print(e)

    def OutputBoard(self):
        for i in self.Spaces: print(i)
