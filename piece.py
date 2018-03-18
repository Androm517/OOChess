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

    def getName(self):
        return self.name_representation

    def __eq__(self, other):
        """Two pieces are equal if they belong to the same team and stand at the same position"""
        if self.color == other.color and self.position == other.position:
            return True
        else:
            return False

    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True

    def __str__(self):
        return str(self.position) + ' ' + self.color + ' ' + self.name
