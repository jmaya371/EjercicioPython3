class Estudiante():
    __NoCuente = ''
    __Nombre = ''
    __Apellido = ''
    __Email = ''
    __Contraseña = ''

    def __init__(self, NoCuenta, Nombre= 'Name', Apellido = 'LastName',
                 Email = 'correo@dominio.com', Password = 'Password'):
        self.__NoCuente = NoCuenta
        self.__Nombre = Nombre
        self.__Apellido = Apellido
        self.__Email = Email
        self.__Contraseña = Password

    def SetInformation(self):
        print("Ingresa numero de cuenta del alumno :")
        self.__NoCuente = input()
        print("Ingresa nombre del alumno :")
        self.__Nombre = input()
        print("Ingresa apellido del alumno :")
        self.__Apellido = input()
        print("Ingresa correo electronico del alumno :")
        self.__Email = input()
        print("Ingresa contraseña del alumno :")
        self.__Contraseña = input()

    def UpdateNoCuenta(self):
        print("Ingresa numero de cuenta del alumno :")
        self.__NoCuente = input()

    def UpdateName(self):
        print("Ingresa nombre del alumno :")
        self.__Nombre = input()

    def UpdateApellido(self):
        print("Ingresa apellido del alumno :")
        self.__Apellido = input()

    def UpdateEmail(self):
        print("Ingresa correo electronico del alumno :")
        self.__Email = input()

    def UpdateContraseña(self):
        print("Ingresa contraseña del alumno :")
        self.__Contraseña = input()

    def GetNoCuenta(self):
        return self.__NoCuente

    def GetName(self):
        return self.__Nombre

    def GetApellido(self):
        return self.__Apellido

    def GetEmail(self):
        return self.__Email

    def GetContraseña(self):
        return self.__Contraseña

    def GetInformation(self):
        print(f"No. de cuenta: {self.__NoCuente}")
        print(f"Nombre del alumno : {self.__Nombre}")
        print(f"Apellido del alumno : {self.__Apellido}")
        print(f"Correo electronico del alumno : {self.__Email}")
        print(f"Contraseña del alumno : {self.__Contraseña}")

    def __str__(self):
        return f"No. de cuenta: \t\t\t\t\t{self.__NoCuente}\n" \
               f"Nombre del alumno : \t\t\t{self.__Nombre}\n"\
               f"Apellido del alumno : \t\t\t{self.__Apellido}\n"\
               f"Correo electronico del alumno : {self.__Email}\n"\
               f"Contraseña del alumno : \t\t{self.__Contraseña}\n"\
