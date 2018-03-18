import position

def validateMove(active_piece, at_position, to_position, gameboard):
    return True

def validateWhitePawn(from_position, to_position, gameboard):
    move_vector = to_position.subtract(from_position)
    distance = move_vector.dot(move_vector)
    if distance == 1 and move_vector == position.Position( (0, 1)):
        if gameboard.checkIsPositionEmpty(to_position):
            return True
        else:
            return False
