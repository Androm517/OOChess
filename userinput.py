

class UserInput:
    def getMsg(self):
        while True:
            msg = input(">>> ")
            msg = msg.split()
            if len(msg) == 1:
                return msg[0]
            elif len(msg) == 2:
                return msg[0], msg[1]
            else:
                print('Måste ge 1 eller 2 argument.')
