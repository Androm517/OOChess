import position


def validateMove(active_piece, at_position, to_position, gameboard):
    if active_piece.hasName('pawn'):
        return validatePawn(active_piece, at_position, to_position, gameboard)
    else:
        return True

def validatePawn(active_piece, at_position, to_position, gameboard):
    at_position = position.Position(at_position)
    to_position = position.Position(to_position)
    unit_difference = at_position.subtract(to_position).unit()
    print(f'unit_difference: {unit_difference.coordinates}')
    step = to_position.subtract(at_position)
    print(f'step: {str(step)}')
    passive_piece = gameboard.getPieceAtPosition(str(to_position))
    if active_piece.hasColor('white'):
        one_step = position.Position('a2')
        two_step = position.Position('a3')
        capture = position.Position('b2')
        capture_left = capture.subtract(position.Position('c1'))
        capture_right = capture.subtract(position.Position('a1'))

    else:
        start_position = position.Position('d8')
        one_step = position.Position('d7').subtract(start_position)
        two_step = position.Position('d6').subtract(start_position)
        capture = position.Position('d7')
        capture_left = capture.subtract(position.Position('e8'))
        capture_right = capture.subtract(position.Position('c8'))
    if (step == capture_left or step == capture_right) and passive_piece is not None:
        return True
    elif step == one_step and passive_piece is None:
        return checkSquaresForBlockingPiecesRecursive(at_position, to_position.add(unit_difference), gameboard,
                                                      unit_difference)
    elif active_piece.start_position and step == two_step and passive_piece is None:
        print('Make two steps with pawn')
        return checkSquaresForBlockingPiecesRecursive(at_position, to_position.add(unit_difference), gameboard,
                                                      unit_difference)
    else:
        return False

def checkSquaresForBlockingPiecesRecursive(at_position, check_position, gameboard, unit_difference):
    print(f'check_position: {check_position.coordinates}')
    print(f'check_position: {str(check_position)}')
    if check_position == at_position:
        return True
    passive_piece = gameboard.getPieceAtPosition(str(check_position))
    if passive_piece is not None:
        return False
    return checkSquaresForBlockingPiecesRecursive(at_position, check_position.add(unit_difference), gameboard, unit_difference)

