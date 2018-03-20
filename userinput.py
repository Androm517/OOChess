

class UserInput:
    def __init__(self):
        self.keywords = ['short castle', 'long castle', 'en passant', 'q', 'quit']

    def getMsg(self):
        while True:
            msg = input(">>> ")
            if msg in self.keywords:
                if msg == 'en passant':
                    en_passant_square = input("Which square do you attack from: ")
                    en_passant_square = self.getSquare()
                    return [msg + ' ' + en_passant_square]
                return [msg]
            msg = msg.split()
            if len(msg) == 2 and self.isSquareOnGameboard(msg[0]) and self.isSquareOnGameboard(msg[1]):
                return msg
            else:
                print('Måste ge commando - short/long castle, en passant - eller 2 argument. Positioner måste finnas på spelbrädet.')

    def getSquare(self):
        while True:
            square = input(">>> ")
            if self.isSquareOnGameboard(square):
                return square
            else:
                print('Ej en ruta på spelbrädet. Försök igen.')

    def isSquareOnGameboard(self, square):
        if square[0] in 'abcdefgh' and square[1] in '12345678':
            return True
        else:
            return False

