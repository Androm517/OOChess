

class UserInput:
    def getMsg(self):
        while True:
            msg = input(">>> ")
            msg = msg.split()
            if len(msg) == 1:
                return msg[0]
            elif len(msg) == 3:
                return msg
            else:
                print('Måste ge 1 eller 3 argument.')
        return msg[0], msg[1], msg[2]