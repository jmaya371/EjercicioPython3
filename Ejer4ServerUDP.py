import socket as ServUDP


class ServerUDP():
    __ServerSocketUDP = None

    def __init__(self, Port):
        self.__ServerSocketUDP = ServUDP.socket(ServUDP.AF_INET, ServUDP.SOCK_DGRAM)
        Addr = '127.0.0.1', Port
        self.__ServerSocketUDP.bind(Addr)

    def SendMsg(self, Msg, Addr):
        self.__ServerSocketUDP.sendto(Msg.encode(), Addr)

    def ReadMsg(self):
        DataAndAddr = self.__ServerSocketUDP.recvfrom(1024)
        return DataAndAddr

    def PrintMsg(self, Msg, Addr):
        print(f'Nuevo mensaje de: {Addr}\n'
                f'Mensaje:\n'
                f'{Msg}')


if __name__ == '__main__':
    ConxServUDP = ServerUDP(12345)
    salir = False
    while not salir:
        Msg, Addr = ConxServUDP.ReadMsg()
        ConxServUDP.PrintMsg(Msg.decode(), Addr)
        ConxServUDP.SendMsg('Mensaje recibido!', Addr)
