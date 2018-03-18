import userinput
import gameboard
import piece
import movevalidationfunctions


ui = userinput.UserInput()
gb = gameboard.Gameboard()

captured_pieces = []
white_pieces = []
black_pieces = []
for i in 'abcdefgh':
    white_pieces.append(piece.Piece(i + '2', name='pawn', color='white', name_representation='\u2659'))
    black_pieces.append(piece.Piece(i + '7', name='pawn', color='black', name_representation='\u265F'))
for i in 'ah':
    white_pieces.append(piece.Piece(i + '1', name='rook', color='white', name_representation='\u2656'))
    black_pieces.append(piece.Piece(i + '8', name='rook', color='black', name_representation='\u265C'))
for i in 'bg':
    white_pieces.append(piece.Piece(i + '1', name='knight', color='white', name_representation='\u2658'))
    black_pieces.append(piece.Piece(i + '8', name='knight', color='black', name_representation='\u265E'))
for i in 'cf':
    white_pieces.append(piece.Piece(i + '1', name='bishop', color='white', name_representation='\u2657'))
    black_pieces.append(piece.Piece(i + '8', name='bishop', color='black', name_representation='\u265D'))

white_pieces.append(piece.Piece('d1', name='queen', color='white', name_representation='\u2655'))
black_pieces.append(piece.Piece('d8', name='queen', color='black', name_representation='\u265B'))
white_pieces.append(piece.Piece('e1', name='king', color='white', name_representation='\u2654'))
black_pieces.append(piece.Piece('e8', name='king', color='black', name_representation='\u265A'))



def capture():
    passive_piece = gb.getPieceAtPosition(to_position)
    if passive_piece is not None:
        if passive_piece.color == 'white':
            white_pieces.remove(passive_piece)
        elif passive_piece.color == 'black':
            black_pieces.remove(passive_piece)
        captured_pieces.append(passive_piece)

def moveAtPositionToPositionAndCapture():
    capture()
    active_piece = gb.getPieceAtPosition(at_position)
    active_piece.changePositionTo(to_position)

def validateMove():
    active_piece = gb.getPieceAtPosition(at_position)
    if active_piece.color != color:
        return False
    if movevalidationfunctions.validateMove(active_piece, at_position, to_position, gb):
        return True
    else:
        return False


def updateAndViewBoard():
    gb.updateBoardState(white_pieces + black_pieces)
    gb.viewBoard()


updateAndViewBoard()
print()
while True:
    msg = ui.getMsg()
    if msg == 'q':
        print('Hejdå')
        break
    color, at_position, to_position = msg
    if validateMove():
        moveAtPositionToPositionAndCapture()
    updateAndViewBoard()
    print()

def convertListToStr(l):
    s = ''
    for item in l:
        s += str(item) + '; '
    return s
print(f'white_pieces: {convertListToStr(white_pieces)}')
print(f'black_pieces: {convertListToStr(black_pieces)}')
print(f'captured_pieces: {convertListToStr(captured_pieces)}')
