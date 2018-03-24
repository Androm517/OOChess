"""
client.py: Connect the client to the server.
"""

import sys
import socket
import threading


def readerTask(sock):
    while True:
        r = sock.recv(4096)
        if not r:
            break
        print(r.decode('utf-8'))
    sys.exit(-1)


if __name__ == '__main__':
    # create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket
    try:
        # sock.connect(('192.168.1.192', 9999))
        sock.connect(('127.0.0.1', 9999))
    except OSError as e:
        print('connecting to server failed')
        sys.exit(e.errno)

    reader = threading.Thread(target=readerTask, args=(sock,))
    reader.daemon = True
    reader.start()

    while True:
        try:
            message = input('')
            if message == 'q':
                break
            sock.send(bytes(message, 'utf-8'))

        except KeyboardInterrupt:
            print()

        except OSError:
            print('connection with server lost...')
            break

        except EOFError:
            break

    print('\nBye!')
    sys.exit()
