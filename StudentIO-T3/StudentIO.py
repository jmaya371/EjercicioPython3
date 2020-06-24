import ClassStudent
import shelve
try:
    import cpickle as pickle
except ImportError:
    import pickle


def SaveStudentPickle(StudentInfo):
    file = open('Student.txt', 'wb')
    pickle.Pickler(file, 4).dump(StudentInfo)
    file.close()


def SaveStudentShelve(StudentInfo):
    with shelve.open('Student') as shelf:
        shelf[str(StudentInfo.GetNoCuenta())] = StudentInfo


def ReadStudentPickle(key):
    file = open('Student.txt', 'rb')
    Unpickler = pickle.Unpickler(file)
    ReadInfo = Unpickler.load()
    file.close()
    for i in ReadInfo:
        if i.GetNoCuenta() == key:
            print(i)


def ReadStudentShelve(Key):
    with shelve.open('Student') as shelf:
        print(shelf[str(Key)])


def UpdateStudentPickle(key):
    file = open('Student.txt', 'rb')
    Unpickler = pickle.Unpickler(file)
    ReadInfo = Unpickler.load()
    file.close()
    for i in ReadInfo:
        if i.GetNoCuenta() == key:
            i.UpdateName()
            i.UpdateApellido()
            i.UpdateEmail()
            i.UpdateContraseña()
    SaveStudentPickle(ReadInfo)

def UpdateStudentShelve(key):
    with shelve.open('Student') as shelf:
        ObjClassShelf = shelf[key]
        ObjClassShelf.UpdateName()
        ObjClassShelf.UpdateApellido()
        ObjClassShelf.UpdateEmail()
        ObjClassShelf.UpdateContraseña()
        shelf[key] = ObjClassShelf


if __name__ == '__main__':
    InfoStudent = []
    NoCuenta = [20115111, 20126222, 20137333, 20148444, 20159555]
    Name = ['Josue', 'David', 'Katya', 'Denisse', 'Leidy']
    LastName = ['Maya', 'Padilla', 'Ortega', 'Luna', 'Palomera']
    Email = ['jmaya@python.com', 'dpadilla@python.com', 'kortega@python.com',
             'dluna@python.com', 'lpalomera@python.com']
    Password = ['jmaya5111', 'dpadilla6222', 'kortega7333', 'dluna8444', 'lpalomera9555']

    for NC, Na, LN, E, P in zip(NoCuenta, Name, LastName, Email, Password):
        Student = ClassStudent.Estudiante(NC, Na, LN, E, P)
        SaveStudentShelve(Student)
        InfoStudent.append(Student)

    SaveStudentPickle(InfoStudent)

    for i in NoCuenta:
        ReadStudentShelve(i)
    for i in NoCuenta:
        ReadStudentPickle(i)

    UpdateStudentShelve('20115111')
    ReadStudentShelve('20115111')

    UpdateStudentPickle(20115111)
    ReadStudentPickle(20115111)

    pass
