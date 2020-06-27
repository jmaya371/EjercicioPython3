import socket as ClntTCP


class ClientTCP():
    __ClientSocketTCP = None

    def __init__(self, Port):
        self.__ClientSocketTCP = ClntTCP.socket()
        addr = '127.0.0.1', Port
        self.__ClientSocketTCP.connect(addr)
        print(f'Conectado al servidor')

    def SendMsg(self, Msg):
        self.__ClientSocketTCP.send(Msg.encode())

    def CloseConx(self):
        self.__ClientSocketTCP.close()

    def ReadMsg(self):
        Data = self.__ClientSocketTCP.recv(1024)
        return Data.decode()


if __name__ == '__main__':
    ConxClientTCP = ClientTCP(35491)
    ConxClientTCP.SendMsg('Mensaje prueba de envio con TCP')
    while True:
        data = ConxClientTCP.ReadMsg()
        print(data)
        if data == '':
            ConxClientTCP.CloseConx()
            break
