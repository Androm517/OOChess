

class ServerInput:
    def __init__(self):
        self.castle_keywords = ['short', 'long']
        self.square_keywords = [i + j for i in 'abcdefgh' for j in '12345678']
        self.en_passant_keyword = ['passant']

    def parse(self, msg):
        parsed = []
        msg = msg.strip()
        msg = msg.split()
        arg = msg.pop(0)
        if arg == 'castle':
            parsed.append(arg)
            arg = msg.pop(0)
            self.parseCastleKeywords(arg, parsed)
            return ' '.join(parsed)
        elif arg == 'move':
            parsed.append(arg)
            arg = msg.pop(0)
            self.parseSquareKeywords(arg, parsed)
            arg = msg.pop(0)
            self.parseSquareKeywords(arg, parsed)
            return ' '.join(parsed)
        elif arg == 'en':
            parsed.append(arg)
            arg = msg.pop(0)
            self.parseEnPassant(arg, parsed)
            arg = msg.pop(0)
            self.parseSquareKeywords(arg, parsed)
            return ' '.join(parsed)
        elif arg == 'say':
            parsed.append(arg)
            return parsed[0] + ' ' + ' '.join(msg)
        raise ValueError('Expected arguments from user. No arguments reciced')

    def parseEnPassant(self, arg, parsed):
        if arg in self.en_passant_keyword:
           parsed.append(arg)
        else:
            raise  ValueError('Expected one of "{}", got {}'.format(self.en_passant_keyword, arg))

    def parseCastleKeywords(self, arg, parsed):
        if arg in self.castle_keywords:
            parsed.append(arg)
        else:
            raise  ValueError('Expected one of "{}", got {}'.format(self.castle_keywords, arg))

    def parseSquareKeywords(self, arg, parsed):
        if arg in self.square_keywords:
            parsed.append(arg)
        else:
            raise  ValueError('Expected one of "{}", got {}'.format(self.square_keywords, arg))