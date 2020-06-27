import re

# Correo electronico
#   dominio + 1 extensión: jmaya@dominio.com
#   dominio + 2 extensión: jmaya@dominio.com.mx


def OneExt():
    print("Ingresa correo electronico con un dominio")
    Text = input()
    PatternOneExt = r"@+[\w]+\.[a-zA-Z]{2,4}$"
    if re.findall(PatternOneExt, Text):
        print("correo valido")
    else:
        print("correo invalido")


def TwoExt():
    print("Ingresa correo electronico con dos dominios")
    Text = input()
    PatternTwoExt = r"@+[\w]+(\.[a-zA-Z]{2,4}){2}$"
    if re.findall(PatternTwoExt, Text):
        print("correo valido")
    else:
        print("correo invalido")


def SubDomOneExt():
    print("Ingresa correo electronico con sub dominio y un dominio")
    Text = input()
    PatternSubDom = r"@+[\w\.-]+\.[a-zA-Z]{2,4}$"
    if re.findall(PatternSubDom, Text):
        print("correo valido")
    else:
        print("correo invalido")

# numero telefonico
#   10 digitos
#   lada en parentesis (2 a 3 numero)
#       espacios o guines como separador
#       Los separadores deben ser iguales


def NumTo10Dig():
    print("Ingresa cnumero de telefono a 10 digitos")
    Text = input()
    PatternOnlyNum = '[0-9]{10}$'
    if re.match(PatternOnlyNum, Text):
        print("numero valido")
    else:
        print("numero invalido")


def NumWithLada():
    print("Ingresa cnumero de telefono a 10 digitos")
    Text = input()
    PatternIdArea = '([(]+([0-9]{2})+[)]+[0-9]{8}|[(]+([0-9]{3})+[)]+[0-9]{7})$'
    if re.match(PatternIdArea, Text):
        print("numero valido")
    else:
        print("numero invalido")


def NumSepHyp():
    print("Ingresa numero de telefono a 10 digitos, puede separar con (-)")
    Text = input()
    PatternSepHyphen = r"^(\([\d]{2,3}\)[\-]?(([\d][\-]?)*))$"
    if (re.findall(PatternSepHyphen, Text)) and (len(re.findall("[0-9]", Text)) == 10):
        print("numero valido")
    else:
        print("numero invalido")


def NumSepSpa():
    print("Ingresa numero de telefono a 10 digitos, puede separar con espacio")
    Text = input()
    PatternSepSpace = r"^(\([\d]{2,3}\)[\s]?(([\d][\s]?)*))$"
    if (re.findall(PatternSepSpace, Text)) and (len(re.findall("[0-9]", Text)) == 10):
        print("numero valido")
    else:
        print("numero invalido")


def NumSepSpaAndHyp():
    print("Ingresa numero de telefono a 10 digitos, puede separar con espacio y (-)")
    Text = input()
    PatternSepHyphen = r"^(\([\d]{2,3}\)[\-|\s]?(([\d][\-|\s]?)*))$"
    if (re.findall(PatternSepHyphen, Text)) and (len(re.findall("[0-9]", Text)) == 10):
        print("numero valido")
    else:
        print("numero invalido")


# validar RFC
def ValidRFC():
    print("Ingresa RFC")
    Text = input()
    PatternRFC = r'^[A-Z]{4}[\d]{6}[A-Z\d]{3}$'
    if re.findall(PatternRFC, Text):
        print("RFC valido")
    else:
        print("RFC invalido")


# validar CURP
def ValidCURP():
    print("Ingresa CURP")
    Text = input()
    PatternCURP = r'^[A-Z]{4}[\d]{6}[A-Z]{6}[A-Z\d]{2}$'
    if re.findall(PatternCURP, Text):
        print("CURP valido")
    else:
        print("CURP invalido")


if __name__ == '__main__':
    OneExt()
    TwoExt()
    SubDomOneExt()
    NumTo10Dig()
    NumWithLada()
    NumSepHyp()
    NumSepSpa()
    NumSepSpaAndHyp()
    ValidRFC()
    ValidCURP()
