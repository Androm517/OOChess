import position


class Piece:
    def __init__(self, board_position, name, color, name_representation=None):
        self.position = position.Position(board_position)
        self.name = name
        self.color = color
        self.name_representation = name_representation
        self.start_position = True

    def changePositionTo(self, board_position):
        self.position = position.Position(board_position)
        self.start_position = False

    def getPosition(self):
        return str(self.position)

    def getPieceSymbol(self):
        return self.name_representation

    def getPieceName(self):
        return self.name

    def isAtPosition(self, board_position):
        if self.getPosition() == board_position:
            return True
        else:
            return False

    def hasColor(self, color):
        if self.color == color:
            return True
        return False

    def hasName(self, name):
        if self.name == name:
            return True
        return False

    def __str__(self):
        return str(self.position) + ' ' + self.color + ' ' + self.name
