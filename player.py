import threading
import sys


class Player(threading.Thread):
    def __init__(self, color=None, socket=None):
        super().__init__()
        self.socket = socket
        self.color = color
        self.opponent = None
        self.commands = None
        self.daemon = True

    def tell(self, message):
        self.socket.send(bytes(message, 'utf-8'))

    def run(self):
        while True:
            r = self.socket.recv(4096)
            if not r:
                break
            msg = r
            print(msg)
            msg = msg.decode('utf-8')
            msg = msg.split()
            print(msg)
            self.commands[msg[0]](self, msg[1:])
        sys.exit(-1)
