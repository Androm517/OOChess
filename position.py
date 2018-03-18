


class Position:
    def __init__(self, coordinates):
        self.coordinates = (ord(coordinates[0]) - ord('a'), ord(coordinates[1]) - ord('1') )

    def changePositionTo(self, position):
        col, row = position.coordinates
        self.coordinates = (col, row)

    def subtract(self, position):
        x = self.coordinates[0] - position.coordinates[0]
        y = self.coordinates[1] - position.coordinates[1]
        return Position( (x, y))

    def dot(self, position):
        dot_product = 0
        for i in [0, 1]:
            dot_product = self.coordinates[i] + position.coordinates[i]
        return dot_product

    def isColumnRowCoordinatesDifferent(self):
        col, row = self.coordinates
        if col != row:
            return True
        else:
            return False

    def isColumnOrRowCoordinateZero(self):
        col, row = self.coordinates
        if col == 0 or row == 0:
            return True
        else:
            return False

    def __eq__(self, other):
        col, row = self.coordinates
        col_other, row_other = other.coordinates
        if col == col_other and row == row_other:
            return True
        else:
            return False

    def __str__(self):
        col, row = self.coordinates
        col, row = chr( col + ord('a')), chr( row + ord('1'))
        return col + row
