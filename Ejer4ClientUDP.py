import socket as ClntUDP


class ClientUDP():
    __ClientSocketUDP = None
    __Addr = None

    def __init__(self, Port):
        self.__ClientSocketUDP = ClntUDP.socket(ClntUDP.AF_INET, ClntUDP.SOCK_DGRAM)
        self.__Addr = '127.0.0.1', Port

    def SendMsg(self, Msg):
        self.__ClientSocketUDP.sendto(Msg.encode(), self.__Addr)

    def ReadMsg(self):
        DataAndAddr = self.__ClientSocketUDP.recvfrom(1024)
        return DataAndAddr

    def PrintMsg(self, Msg, Addr):
        print(f'Nuevo mensaje de: {Addr}\n'
                f'Mensaje:\n'
                f'{Msg}')


if __name__ == '__main__':
    ConxClientvUDP = ClientUDP(12345)
    ConxClientvUDP.SendMsg('Mensaje prueba de envio con UDP!')
    Msg, Addr = ConxClientvUDP.ReadMsg()
    ConxClientvUDP.PrintMsg(Msg.decode(), Addr)

