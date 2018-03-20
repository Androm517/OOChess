

class UserInput:
    def __init__(self):
        self.keywords = ['short castle', 'long castle', 'en passant', 'q', 'quit']

    def getMsg(self):
        while True:
            msg = input(">>> ")
            if msg in self.keywords:
                if msg == 'en passant':
                    en_passant_square = input("Which square do you attack from: ")
                    return [msg + ' ' + en_passant_square]
                return msg
            msg = msg.split()
            if len(msg) == 2:
                return msg
            else:
                print('Måste ge commando - short/long castle, en passant - eller 2 argument.')
