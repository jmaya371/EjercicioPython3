# Herencia/polimorfismo
# Clase Figura


class Figura():
    base = 0
    altura = 0
    area = 0
    perimetro = 0

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def GetArea(self):
        pass

    def GetPerimetro(self):
        pass


class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def GetArea(self):
        return self.base * self.altura

    def GetPerimetro(self):
        return (self.base * 2) + (self.altura * 2)


class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def GetArea(self):
        return (self.base * self.altura) / 2

    def GetPerimetro(self):
        return self.base * 3


# Encapsulamiento

class Estudiante():
    __Nombre = ''
    __Apellido = ''
    __Email = ''
    __Contraseña = ''

    def __init__(self, Nombre= 'Name', Apellido = 'LastName', Email = 'correo@dominio.com', Password = 'Password'):
        self.__Nombre = Nombre
        self.__Apellido = Apellido
        self.__Email = Email
        self.__Contraseña = Password

    def SetInformation(self):
        print("Ingresa nombre del alumno :")
        self.__Nombre = input()
        print("Ingresa apellido del alumno :")
        self.__Apellido = input()
        print("Ingresa correo electronico del alumno :")
        self.__Email = input()
        print("Ingresa contraseña del alumno del alumno :")
        self.__Contraseña = input()

    def GetInformation(self):
        print(f"Nombre del alumno : {self.__Nombre}")
        print(f"Apellido del alumno : {self.__Apellido}")
        print(f"Correo electronico del alumno : {self.__Email}")
        print(f"Contraseña del alumno del alumno : {self.__Contraseña}")


if __name__ == '__main__':

    print("Obtener area y perimetro de un rectangulo: ")
    print("Ingresar base")
    Base = int(input())
    print("ingresar altura: ")
    Altura = int(input())

    rectangulo = Rectangulo(Base, Altura)
    print("Area del rectangulo: ",rectangulo.GetArea())
    print(f"Perimetro del rectangulo: {rectangulo.GetPerimetro()}")

    print("\n\nObtener area y perimetro de un triangulo: ")
    print("Ingresar base")
    Base = int(input())
    print("ingresar altura: ")
    Altura = int(input())

    triangulo = Triangulo(Base, Altura)
    print(f"Area del triangulo: ", triangulo.GetArea())
    print(f"Perimetro del triangulo equilatero: {triangulo.GetPerimetro()}")

    Alumno = Estudiante()
    print("\n\nAñadir informacion de nuevo alumno")
    Alumno.SetInformation()
    print("\n\nObtener informacion de alumno")
    Alumno.GetInformation()