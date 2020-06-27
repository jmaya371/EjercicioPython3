from mongoengine import *

connect('Padts')


class Estudiantes(Document):
    AccountNum = IntField(required=True)
    Name = StringField(required=True)
    LastName = StringField(required=True)
    Email = EmailField(required=True)
    Password = StringField(required=True)


def SaveStudent(Student):
    Student.save()


def ReadStudent(AccountNum):
    for Indx, student in enumerate(Estudiantes.objects):
        if student.AccountNum == AccountNum:
            StudentInfo = student
            break
    return StudentInfo


def UpdateStudent(AccountNum):
    for Indx, student in enumerate(Estudiantes.objects):
        if student.AccountNum == AccountNum:
            print("Ingresa nuevo nombre del alumno :")
            student.Name = input()
            print("Ingresa nuevo apellido del alumno :")
            student.LastName = input()
            print("Ingresa nuevo correo electronico del alumno :")
            student.Email = input()
            print("Ingresa nuevo contraseña del alumno :")
            student.Password = input()
            SaveStudent(student)
            StudentInfo = student
            break
    return StudentInfo


def DeleteStudent(AccountNum):
    for Indx, student in enumerate(Estudiantes.objects):
        if student.AccountNum == AccountNum:
            student.delete()
    return Estudiantes


def PrintStudent(Student):
    print(f"No. de cuenta: \t\t\t\t\t{Student.AccountNum}\n"
          f"Nombre del alumno: \t\t\t\t{Student.Name}\n"
          f"Apellido del alumno: \t\t\t{Student.LastName}\n"
          f"Correo electronico del alumno:\t{Student.Email}\n"
          f"Contraseña del alumno: \t\t\t{Student.Password}\n")


if __name__ == '__main__':
    AuxStudent = []
    AccountNum = [20115111, 20126222, 20137333, 20148444, 20159555]
    Name = ['Josue', 'David', 'Katya', 'Denisse', 'Leidy']
    LastName = ['Maya', 'Padilla', 'Ortega', 'Luna', 'Palomera']
    Password = ['jmaya5111', 'dpadilla6222', 'kortega7333', 'dluna8444', 'lpalomera9555']
    Email = ['jmaya@python.com', 'dpadilla@python.com', 'kortega@python.com',
             'dluna@python.com', 'lpalomera@python.com']

    for NC, Na, LN, E, P in zip(AccountNum, Name, LastName, Email, Password):
        AuxStudent = Estudiantes(AccountNum=NC, Name=Na, LastName=LN, Email=E,  Password=P)
        SaveStudent(AuxStudent)

    ReadStudent(20115111)
    PrintStudent(ReadStudent(20115111))

    PrintStudent(UpdateStudent(20115111))

    Students = DeleteStudent(20115111)
    print("Estudiantes actuales")
    for Indx, student in enumerate(Students.objects):
        PrintStudent(student)


