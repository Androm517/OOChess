import position


def validateMove(active_piece, at_position, to_position, gameboard):
    if active_piece.hasName('pawn'):
        return validatePawn(active_piece, at_position, to_position, gameboard)
    else:
        return True

def validatePawn(active_piece, at_position, to_position, gameboard):
    return True
