import userinput
import gameboard
import piece
import validate


class Program:
    def __init__(self):
        self.ui = userinput.UserInput()
        self.gameboard = gameboard.Gameboard()
        self.validator = validate.Validate()
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
        passive_piece = self.gameboard.getPieceAtPosition(to_position)
        if passive_piece is not None:
            if passive_piece.hasColor('white'):
                self.white_pieces.remove(passive_piece)
            elif passive_piece.hasColor('black'):
                self.black_pieces.remove(passive_piece)
            self.captured_pieces.append(passive_piece)

    def moveAtPositionToPositionAndCapture(self, at_position, to_position):
        self.capture(to_position)
        active_piece = self.gameboard.getPieceAtPosition(at_position)
        active_piece.changePositionTo(to_position)

    def validateMove(self, color, at_position, to_position):
        active_piece = self.gameboard.getPieceAtPosition(at_position)
        passive_piece = self.gameboard.getPieceAtPosition(to_position)
        if active_piece is None or not active_piece.hasColor(color):
            return False
        if passive_piece is not None and passive_piece.hasColor(color):
            return False
        if self.validator.validateMove(active_piece, at_position, to_position, self.gameboard):
            return True
        else:
            return False

    def updateAndViewBoard(self):
        self.updateBoardState()
        print(self.viewBoard())
        print()

    def updateBoardState(self):
        self.gameboard.updateBoardState(self.white_pieces + self.black_pieces)

    def viewBoard(self):
        return self.gameboard.viewBoard()

    def validateSpecialRuleCommandAndMovePiece(self, msg):
        if msg == 'short castle':
            if self.validator.validateShortCastle(self.color, self.gameboard):
                castle_king = self.gameboard.getWhiteKing() if self.color == 'white' else self.gameboard.getBlackKing()
                move_rook = ['h1', 'f1'] if castle_king.hasColor('white') else ['h8', 'f8']
                move_king = ['e1', 'g1'] if castle_king.hasColor('white') else ['e8', 'g8']
                self.moveAtPositionToPositionAndCapture(move_rook[0], move_rook[1])
                self.moveAtPositionToPositionAndCapture(move_king[0], move_king[1])
                self.validator.setShortCastleFlagToFalse(castle_king)
                return True
        elif msg == 'long castle':
            if self.validator.validateLongCastle(self.color, self.gameboard):
                castle_king = self.gameboard.getWhiteKing() if self.color == 'white' else self.gameboard.getBlackKing()
                move_rook = ['a1', 'd1'] if castle_king.hasColor('white') else ['a8', 'd8']
                move_king = ['e1', 'c1'] if castle_king.hasColor('white') else ['e8', 'c8']
                self.moveAtPositionToPositionAndCapture(move_rook[0], move_rook[1])
                self.moveAtPositionToPositionAndCapture(move_king[0], move_king[1])
                self.validator.setLongCastleFlagToFalse(castle_king)
                return True
        elif 'en passant' in msg:
            msg = msg.split()
            active_piece = self.gameboard.getPieceAtPosition(msg[2])
            if self.validator.validateEnPassant(active_piece):
                passive_piece = self.validator.en_passant_white if active_piece.hasColor('white') else self.validator.en_passant_black
                target_row = '6' if active_piece.hasColor('white') else '3'
                target = passive_piece.getPosition()[0] + target_row
                self.moveAtPositionToPositionAndCapture(active_piece.getPosition(), target)
                self.capture(passive_piece.getPosition())
                return True
        return False

    def validateMoveAndMovePiece(self, color, at_position, to_position):
        if self.validateMove(color, at_position, to_position):
            active_piece = self.gameboard.getPieceAtPosition(at_position)
            if active_piece.hasName('pawn') and '2' in at_position and '4' in to_position:
                self.validator.en_passant_black = active_piece
            if active_piece.hasName('pawn') and '7' in at_position and '5' in to_position:
                self.validator.en_passant_white = active_piece
            self.moveAtPositionToPositionAndCapture(at_position, to_position)
            return True
        else:
            return False

    def quitProgram(self, quit_command):
        if quit_command == 'q' or quit_command == 'quit':
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
            if self.color == 'white':
                if self.validator.isWhiteCheckMate(self.gameboard):
                    print('White is check mate!!!')
                    break
            else:
                if self.validator.isBlackCheckmate(self.gameboard):
                    print('Black is check mate!!!')
                    break
            msg = self.ui.getMsg()
            if len(msg) == 1:
                command = msg[0]
                if self.quitProgram(command):
                    break
                change_player_color = self.validateSpecialRuleCommandAndMovePiece(command)
            elif len(msg) == 2:
                at_position, to_position = msg
                change_player_color = self.validateMoveAndMovePiece(self.color, at_position, to_position)
            if change_player_color:
                if self.color == 'white':
                    self.validator.en_passant_white = None
                else:
                    self.validator.en_passant_black = None
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
