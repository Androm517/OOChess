


class Position:
    def __init__(self, coordinates):
        self.coordinates = (ord(coordinates[0]) - ord('a'), ord(coordinates[1]) - ord('1') )

    def changePositionTo(self, position):
        col, row = position.coordinates
        self.coordinates = (col, row)

    def subtract(self, position):
        x = self.coordinates[0] - position.coordinates[0]
        y = self.coordinates[1] - position.coordinates[1]
        tmp = self.createPositionWithCoordinates(x, y)
        return tmp

    def add(self, position):
        x = self.coordinates[0] + position.coordinates[0]
        y = self.coordinates[1] + position.coordinates[1]
        tmp = self.createPositionWithCoordinates(x, y)
        return tmp

    def invert(self):
        x = -self.coordinates[0]
        y = -self.coordinates[1]
        tmp = self.createPositionWithCoordinates(x, y)
        return tmp

    def equals(self, chessboard_position):
        if str(self) == chessboard_position:
            return True
        else:
            return False

    def length(self):
        return int(abs(self.coordinates[0]) + abs(self.coordinates[1]))

    def unit(self):
        col, row = self.coordinates
        tmp = Position('a1')
        tmp.coordinates = (13, 17)
        if self.rowLength() == self.columnLength():
            tmp.coordinates = (int(col / abs(col)), int(row / abs(row)))
        elif col == 0:
            tmp.coordinates = (0, int(row / abs(row)))
        elif row == 0:
            tmp.coordinates = (int(col / abs(col)), 0)
        return tmp

    def rowLength(self):
        col, row = self.coordinates
        return int(abs(row))


    def columnLength(self):
        col, row = self.coordinates
        return int(abs(col))

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

    def createPositionWithCoordinates(self, x, y):
        tmp = Position('a1')
        tmp.coordinates = (x, y)
        return tmp
