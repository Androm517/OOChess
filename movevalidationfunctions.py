import position


def validateMove(active_piece, at_position, to_position, gameboard):
    at_position, to_position = convertStrPositionToObjPosition(at_position, to_position)
    if active_piece.hasName('pawn'):
        return validatePawn(active_piece, at_position, to_position, gameboard)
    else:
        return True

def validatePawn(active_piece, at_position, to_position, gameboard):
    unit_difference = at_position.subtract(to_position).unit()
    step = to_position.subtract(at_position)
    one_step, two_step, capture = convertStrPositionToObjPosition('a2', 'a3', 'b2')
    capture_left = capture.subtract(position.Position('c1'))
    capture_right = capture.subtract(position.Position('a1'))
    passive_piece = gameboard.getPieceAtPosition(str(to_position))
    if active_piece.hasColor('black'):
        one_step = one_step.invert()
        two_step = two_step.invert()
        capture_left = capture_right.invert()
        capture_right = capture_left.invert()
    if (step == capture_left or step == capture_right) and passive_piece is not None:
        return True
    elif step == one_step and passive_piece is None:
        return checkSquaresForBlockingPiecesRecursive(at_position, to_position.add(unit_difference), gameboard,
                                                      unit_difference)
    elif active_piece.start_position and step == two_step and passive_piece is None:
        return checkSquaresForBlockingPiecesRecursive(at_position, to_position.add(unit_difference), gameboard,
                                                      unit_difference)
    else:
        return False

def convertStrPositionToObjPosition(*arg):
    positions = []
    for board_position in arg:
        positions.append(position.Position(board_position))
    return positions


def checkSquaresForBlockingPiecesRecursive(at_position, check_position, gameboard, unit_difference):
    if check_position == at_position:
        return True
    passive_piece = gameboard.getPieceAtPosition(str(check_position))
    if passive_piece is not None:
        return False
    return checkSquaresForBlockingPiecesRecursive(at_position, check_position.add(unit_difference), gameboard, unit_difference)

