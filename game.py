import socket
import threading
import logging
import random

from piece import Piece
from player import Player

WHITE = 'white'
BLACK = 'black'
COLORS = [WHITE, BLACK]

BIND_IP = '0.0.0.0'
BIND_PORT = 9999

logger = logging.getLogger(__name__)


class Server:
    """ Checks for incomming client connections. Creates players when clients connects. Initialized chessboard and
    when there is two players it starts the game."""
    def __init__(self):
        self.players = []
        self.boardLock = threading.Lock()
        self.started = False
        self.commands = {
            'move': self.makeMove,
            'surrender': self.give_up,
            'yield': self.give_up,
            'castle': self.castle,
            'say': self.say,
            'print': lambda p: str(self.board)
        }

    def makeMove(self, player, at, to):
        try:
            with self.boardLock:
                pass
            player.opponent.tell('{} made a move, your turn.'.format(player.color))
            player.opponent.tell()
            return None
        except Exception as e:
            logger.exception(e)
            return str(e)

    def give_up(self, player):
        raise NotImplemented()

    def castle(self, player, where):
        raise NotImplemented()

    def say(self, player, msg):
        print(f'say.msg: {msg}')
        player.opponent.tell(' '.join(msg))
        return None

    # start server and stuff... as someone connects add a player to the list of players
    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((BIND_IP, BIND_PORT))
        server.listen(5)  # max backlog of connections

        print('Listening on {}:{}'.format(BIND_IP, BIND_PORT))

        while True:
            try:
                client_sock, address = server.accept()
                print('Accepted connection from {}:{}'.format(address[0], address[1]))

                if len(self.players) == 2:
                    client_sock.close()
                    continue

                if self.players:
                    player = Player(WHITE if self.players[0].color == BLACK else BLACK, client_sock)
                    self.players[0].tell('another player connected, the game can start!')
                else:
                    player = Player(random.choice(COLORS), client_sock)
                player.tell('Welcome to the game! You are {}.'.format(player.color))
                player.commands = self.commands
                player.start()
                self.players.append(player)

                if len(self.players) == 2:
                    self.players[0].opponent = self.players[1]
                    self.players[1].opponent = self.players[0]
                    self.game_started = True

            except KeyboardInterrupt:
                break

        for p in self.players:
            p.disconnect()

        server.close()


if __name__ == '__main__':
    Server().run()
