import socket as ServTCP


class ServerTCP():
    __ClientConx = 0
    __ClientAddr = 0
    __NoConx = 0
    __ServerSocketTCP = None

    def __init__(self, Port):
        self.__ServerSocketTCP = ServTCP.socket()
        addr = '127.0.0.1', Port
        self.__ServerSocketTCP.bind(addr)
        self.__ServerSocketTCP.listen()

    def AcceptConex(self):
        if self.__NoConx < 10:
            (self.__ClientConx, self.__ClientAddr) = self.__ServerSocketTCP.accept()
            self.__NoConx += 1
            print(f'Conexion {self.__NoConx} aceptada de {self.__ClientAddr}')

    def SendMsgClose(self, Msg):
        self.__ClientConx.send(Msg.encode())
        self.__ClientConx.close()
        self.__NoConx -= 1

    def SendMsg(self, Msg):
        self.__ClientConx.send(Msg.encode())

    def ReadMsg(self):
        Data = self.__ClientConx.recv(1024)
        return Data.decode()

    def PrintMsg(self, Msg):
        return f'Mensaje:\n' \
                f'{Msg}'


if __name__ == '__main__':
    ConxServTCP = ServerTCP(35491)
    while True:
        ConxServTCP.AcceptConex()
        while True:
            Msg = ConxServTCP.ReadMsg()
            ConxServTCP.PrintMsg(Msg)
            if Msg != '':
                ConxServTCP.SendMsg('Mensaje recibido')
                ConxServTCP.SendMsgClose('Fin de comunicacion')
                break
