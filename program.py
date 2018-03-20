import userinput
import gameboard
import piece
import validate


class Program:
    def __init__(self):
        self.ui = userinput.UserInput()
        self.gb = gameboard.Gameboard()
        self.vm = validate.Validate()
        self.color = 'white'

        self.captured_pieces = []
        self.white_pieces = []
        self.black_pieces = []
        for i in 'abcdefgh':
            self.white_pieces.append(piece.Piece(i + '2', name='pawn', color='white', name_representation='\u2659'))
            self.black_pieces.append(piece.Piece(i + '7', name='pawn', color='black', name_representation='\u265F'))
        for i in 'ah':
            self.white_pieces.append(piece.Piece(i + '1', name='rook', color='white', name_representation='\u2656'))
            self.black_pieces.append(piece.Piece(i + '8', name='rook', color='black', name_representation='\u265C'))
        for i in 'bg':
            self.white_pieces.append(piece.Piece(i + '1', name='knight', color='white', name_representation='\u2658'))
            self.black_pieces.append(piece.Piece(i + '8', name='knight', color='black', name_representation='\u265E'))
        for i in 'cf':
            self.white_pieces.append(piece.Piece(i + '1', name='bishop', color='white', name_representation='\u2657'))
            self.black_pieces.append(piece.Piece(i + '8', name='bishop', color='black', name_representation='\u265D'))

        self.white_pieces.append(piece.Piece('d1', name='queen', color='white', name_representation='\u2655'))
        self.black_pieces.append(piece.Piece('d8', name='queen', color='black', name_representation='\u265B'))
        self.white_pieces.append(piece.Piece('e1', name='king', color='white', name_representation='\u2654'))
        self.black_pieces.append(piece.Piece('e8', name='king', color='black', name_representation='\u265A'))

    def capture(self, to_position):
        passive_piece = self.gb.getPieceAtPosition(to_position)
        if passive_piece is not None:
            if passive_piece.hasColor('white'):
                self.white_pieces.remove(passive_piece)
            elif passive_piece.hasColor('black'):
                self.black_pieces.remove(passive_piece)
            self.captured_pieces.append(passive_piece)

    def moveAtPositionToPositionAndCapture(self, at_position, to_position):
        self.capture(to_position)
        active_piece = self.gb.getPieceAtPosition(at_position)
        active_piece.changePositionTo(to_position)

    def validateMove(self, color, at_position, to_position):
        active_piece = self.gb.getPieceAtPosition(at_position)
        passive_piece = self.gb.getPieceAtPosition(to_position)
        if active_piece is None or not active_piece.hasColor(color):
            return False
        if passive_piece is not None and passive_piece.hasColor(color):
            return False
        if self.vm.validateMove(active_piece, at_position, to_position, self.gb):
            return True
        else:
            return False

    def updateAndViewBoard(self):
        self.gb.updateBoardState(self.white_pieces + self.black_pieces)
        self.gb.viewBoard()
        print()

    def specialRuleMessage(self, msg):
        if msg == 'short castle':
            if self.vm.validateShortCastle(self.color, self.gb):
                castle_king = self.gb.getWhiteKing() if self.color == 'white' else self.gb.getBlackKing()
                move_rook = ['h1', 'f1'] if castle_king.hasColor('white') else ['h8', 'f8']
                move_king = ['e1', 'g1'] if castle_king.hasColor('white') else ['e8', 'g8']
                self.moveAtPositionToPositionAndCapture(move_rook[0], move_rook[1])
                self.moveAtPositionToPositionAndCapture(move_king[0], move_king[1])
                self.vm.setShortCastleFlagToFalse(castle_king)
                return True
        elif msg == 'long castle':
            if self.vm.validateLongCastle(self.color, self.gb):
                castle_king = self.gb.getWhiteKing() if self.color == 'white' else self.gb.getBlackKing()
                move_rook = ['a1', 'd1'] if castle_king.hasColor('white') else ['a8', 'd8']
                move_king = ['e1', 'c1'] if castle_king.hasColor('white') else ['e8', 'c8']
                self.moveAtPositionToPositionAndCapture(move_rook[0], move_rook[1])
                self.moveAtPositionToPositionAndCapture(move_king[0], move_king[1])
                self.vm.setLongCastleFlagToFalse(castle_king)
                return True
        elif 'en passant' in msg:
            msg = msg.split()
            active_piece = self.gb.getPieceAtPosition(msg[2])
            if self.vm.validateEnPassant(active_piece, self.color, self.gb):
                return True
        return False

    def moveMessage(self, at_position, to_position):
        piece_at_position = self.gb.getPieceAtPosition(at_position)
        if piece_at_position is not None:
            if self.validateMove(self.color, at_position, to_position):
                self.moveAtPositionToPositionAndCapture(at_position, to_position)
                return True
        return False

    def quitProgram(self, msg):
        if msg == 'q' or msg == 'quit':
            print(f'white_pieces: {    self.convertListToStr(self.white_pieces)}')
            print(f'black_pieces: {    self.convertListToStr(self.black_pieces)}')
            print(f'captured_pieces: { self.convertListToStr(self.captured_pieces)}')
            print('Hejdå')
            return True
        else:
            return False

    def run(self):
        self.updateAndViewBoard()
        while True:
            change_player_color = False
            msg = self.ui.getMsg()
            if len(msg) == 1:
                msg = msg[0]
                if self.quitProgram(msg):
                    break
                change_player_color = self.specialRuleMessage(msg)
            elif len(msg) == 2:
                at_position, to_position = msg
                change_player_color = self.moveMessage(at_position, to_position)
            if change_player_color:
                if self.color == 'white':
                    self.vm.en_passant_white[0] = False
                else:
                    self.vm.en_passant_black[0] = False
                self.color = 'black' if self.color == 'white' else 'white'
            self.updateAndViewBoard()
    
    def convertListToStr(self, item_list):
        s = ''
        for item in item_list:
           s += str(item) + '; '
        return s

if __name__ == '__main__':
    program = Program()
    program.run()
