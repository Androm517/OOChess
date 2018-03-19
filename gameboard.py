"""
class: Gameboard
Beskrivning: Håller spelbrädets tillstånd.
"""

class Gameboard:
    def __init__(self):
        self.board_state = {}

    def updateBoardState(self, pieces):
        self.cleanBoardState()
        for piece in pieces:
            self.board_state[str(piece.position)] = piece

    def getPieceAtPosition(self, position):
        return self.board_state.get(position, None)

    def cleanBoardState(self):
        self.board_state = {}

    def getAllPiecesWithColor(self, color):
        pieces = []
        for _, p in self.board_state.items():
            if p.getColor() == color:
                pieces.append(p)
        return pieces

    def getKingWithColor(self, color):
        for _, p in self.board_state.items():
            if p.getColor() == color:
                return p

    def viewBoard(self):
        s = '  ABCDEFGH'
        for row in '87654321':
            s += '\n' + row + ' '
            for col in 'abcdefgh':
                tmp = self.board_state.get(col + row, None)
                if tmp is not None:
                    s += tmp.getPieceSymbol()
                else:
                    s += '#'
        print(s)
