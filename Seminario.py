import math
import datetime
from datetime import datetime
import re
import sys

centro = '*'
numparticipante= 0


class Datos():
    def __init__(self,identificacion,nombre,sexo,email,codigo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.sexo = sexo
        self.email = email
        self.codigo = codigo

class Dprofesor(Datos):
    def __init__(self,identificacion,nombre,sexo,email,codigo,especialidad,departamento,aexperiencia,nivelestudios,ainteres):
        super().__init__(identificacion,nombre,sexo,email,codigo)
        self.especialidad = especialidad
        self.departamento = departamento
        self.aexperiencia = aexperiencia
        self.nivelestudios = nivelestudios
        self.ainteres = ainteres

class Destudiante(Datos):
    def __init__(self,identificacion,nombre,sexo,email,codigo,nombreuniversidad,acursa,ainteres):
        super().__init__(identificacion,nombre,sexo,email,codigo)
        self.nombreuniversidad = nombreuniversidad
        self.acursa = acursa
        self.ainteres = ainteres

class Dprofessional(Datos):
    def __init__(self,identificacion,nombre,sexo,email,codigo,empresa,cargo,areatrabajo,aexperiencia,nivelestudios,ainteres):
        super().__init__(identificacion,nombre,sexo,email,codigo)
        self.empresa =empresa
        self.cargo = cargo
        self.areatrabajo = areatrabajo
        self.aexperiencia = aexperiencia
        self.nivelestudios = nivelestudios
        self.ainteres = ainteres
class Seminario():
    def __init__(self):
        self.semi ={}

    def consultaInteres(self):

        while True:
            try:
                interes= int(input(
                    "Ingrese el área de interés del profesor (1 =  Ciberseguridad, 2 =  Computación en la Nube o 3 = Ciencia de Datos ):"))
                if interes == 1 or interes == 2 or interes == 3:
                    break
                else:
                    print("No es una de las opciones")
            except ValueError:
                print("Dato incorrecto; intente nuevamente")

        for participante in self.semi.values():
            if participante.ainteres == interes:
                print(participante.nombre)

            """ ESTA PARTE DEL CODIGO SE DEBE EXPORTAR A EXCEL POR EL MODELO DE LA PROFE"""

    def consultaProfesores(self):

            for participante in self.semi.values():
                if isinstance(participante, Dprofesor):
                    print(participante.nombre)

            """ ESTA PARTE DEL CODIGO SE DEBE EXPORTAR A EXCEL POR EL MODELO DE LA PROFE"""


    def consultaProfesoresEspecialidad(self):
        especialidad = str(input("Ingrese la especialidad que desea buscar: "))

        for participante in self.semi.values():
            if isinstance(participante, Dprofesor):
                if participante.especialidad==especialidad:
                    print(participante.nombre)

            """ ESTA PARTE DEL CODIGO SE DEBE EXPORTAR A EXCEL POR EL MODELO DE LA PROFE"""

    def consultaProfesionalExp(self):
        experiencia = int(input("Ingrese los años de experiencia: "))

        for participante in self.semi.values():

            if isinstance(participante, Dprofessional):
                if participante.aexperiencia==experiencia:
                    print(participante.nombre)
            """ ESTA PARTE DEL CODIGO SE DEBE EXPORTAR A EXCEL POR EL MODELO DE LA PROFE"""

    def consultaEu(self):
        universidad = str(input("Ingrese la universidad: "))

        for participante in self.semi.values():

            if isinstance(participante, Destudiante):
                if participante.nombreuniversidad == universidad:
                    print(participante.nombre)
            """ ESTA PARTE DEL CODIGO SE DEBE EXPORTAR A EXCEL POR EL MODELO DE LA PROFE"""

    def porcentajes(self):
        nProfesores=0
        nEstudiantes = 0
        nProfesionales=0

        for participante in self.semi.values():

            if isinstance(participante, Dprofesor):
                nProfesores +=1

            if isinstance(participante, Destudiante):
                nEstudiantes += 1

            if isinstance(participante, Dprofessional):
                nProfesionales += 1
        porcentajeProfesores = (nProfesores / len(self.semi)) * 100
        porcentajeEstudiantes=(nEstudiantes/len(self.semi))*100
        porcentajeProfesionales = (nProfesionales / len(self.semi)) * 100

        print(porcentajeProfesores)
        print(porcentajeEstudiantes)
        print(porcentajeProfesionales)


        """ ESTA PARTE DEL CODIGO SE DEBE EXPORTAR A EXCEL POR EL MODELO DE LA PROFE"""
    def validar_email(self,email):
        pattern = r'^([a-z0-9._%-]+)@([a-z0-9.-]+)\.[a-z]{2,4}$'
        if re.match(pattern, email):
            return True
        else:
            return False
    def validar_cedula(self,id):
        pattern = r'^(PE|E|N|[23456789](?:AV|PI)?|1[0123]?(?:AV|PI)?)-([0-9]{1,4})-([0-9]{1,6})$'
        if re.match(pattern,id):
            return True
        else:
            return False

    def registrar(self):

        global numparticipante

        while True:
            numparticipante += 1
            print("Favor Seleccionar el tipo de participante a registrar".center(70, '-'))
            print(centro.center(70, '*'))
            print("Menú".center(70, '-'))
            print(centro.center(70, '*'))
            print("1. Profesor")
            print("2. Estudiante")
            print("3. Profesional")
            while True:
                try:
                    opcion2 = int(input("Ingrese una opción: "))
                    #print(f"Wacala {opcion2}")
                    print("\n")
                    print(centro.center(70, '='))
                    if opcion2 == 1 or opcion2 == 2 or opcion2 == 3:
                        break
                    else:
                        print("Debe utilizar 1 para Profesor o 2 para Estudiante o 3 para profesional")
                except ValueError:
                    print("Dato incorrecto; intente nuevamente")

            match opcion2:
                case 1:
                    while True:
                        print("Favor Seleccionar el tipo de identificacion (Profesor)".center(70, '-'))
                        print(centro.center(70, '*'))
                        print("Menú".center(70, '-'))
                        print(centro.center(70, '*'))
                        print("1. Cedula")
                        print("2. Pasaporte")
                        opcion_valida = False
                        while True:
                            try:
                                opcion3 = int(input("Ingrese una opción: "))
                                break
                            except ValueError:
                                print("Tipo de dato incorrecto; intente nuevamente")
                        if opcion3 != 1 and opcion3 != 2:
                            print("Valor incorrecto")
                        elif opcion3 == 1:
                            while True:
                                identificacion = input("Ingrese la identificación del profesor (Cedula): ")
                                if self.validar_cedula(identificacion):
                                    break
                                else:
                                    print("Formato de cedula invalido")
                            opcion_valida = True
                        elif opcion3 == 2:
                            identificacion = input("Ingrese la identificación del profesor (Pasaporte): ")
                            opcion_valida = True
                        if opcion_valida:
                            break
                    nombreparticipante = input("Ingrese el nombre del profesor: ")
                    while True:
                        sexo = input("Ingrese el sexo del profesor (f para femenino y m para masculino): ")
                        if sexo.lower() != 'f' and sexo.lower() != 'm':
                            print("Valor incorrecto, intente de nuevo")
                        else:
                            break
                    while True:
                        email = input("Ingresar correo electronico del Profesor: ")
                        if self.validar_email(email):
                            break
                        else:
                            print("Cuenta de correo electronico en formato invalido")
                    especialidad = input("Ingrese la especialidad del profesor: ")
                    departamento = input("Ingrese el departamento para el cual trabaja el profesor: ")
                    while True:
                        try:
                            aexperiencia = int(input("Ingrese los años de experiencia del profesor: "))
                            if aexperiencia >=0:
                                break
                            else:
                                print("El valor debe ser mayor a cero (0)")
                        except ValueError:
                            print("Dato incorrecto; intente nuevamente")
                    while True:
                        try:
                            nivelestudios = int(input("Ingrese el nivel de estudio del profesor: 1 (Lic/Ing) o 2 (maestria/posgrado) "))
                            if nivelestudios == 1 or nivelestudios == 2:
                                break
                            else:
                                print("El dato debe ser 1 (Lic/Ing) o 2 (maestria/Doctorado) ")
                        except ValueError:
                            print("Dato incorrecto; intente nuevamente")
                    while True:
                        try:
                            ainteres = int(input("Ingrese el área de interés del profesor (1 =  Ciberseguridad, 2 =  Computación en la Nube o 3 = Ciencia de Datos ):"))
                            if ainteres == 1 or ainteres == 2 or ainteres == 3:
                                break
                            else:
                                print("No es una de las opciones")
                        except ValueError:
                            print("Dato incorrecto; intente nuevamente")
                    while True:
                        respuesta = input(f"Favor confirmar si va a guardar los datos del profesor "
                                          f" {nombreparticipante} (s para si y n para no)")
                        if respuesta.lower() != 's' and respuesta.lower() != 'n':
                            while respuesta.lower() != 's' and respuesta.lower() != 'n':
                                print("Valor incorrecto intente de nuevo")
                                respuesta = input("Desea registrar los datos  (s para si y n para no): ")
                        elif respuesta.lower() == 's':
                            profesor = Dprofesor(identificacion, nombreparticipante, sexo, email, opcion2, especialidad,
                                               departamento, aexperiencia, nivelestudios, ainteres)

                            self.semi[numparticipante] = profesor
                            print(f"Profesor{self.semi}")
                            print("El registro del participante fue exitoso(Profesor)")
                            break
                        else:
                            numparticipante=-1
                            break

                case 2:
                    while True:
                        print("Favor Seleccionar el tipo de identificacion (Estudiante)".center(70, '-'))
                        print(centro.center(70, '*'))
                        print("Menú".center(70, '-'))
                        print(centro.center(70, '*'))
                        print("1. Cedula")
                        print("2. Pasaporte")
                        opcion_valida = False
                        while True:
                            try:
                                opcion3 = int(input("Ingrese una opción: "))
                                break
                            except ValueError:
                                print("Tipo de dato incorrecto; intente nuevamente")
                        if opcion3 != 1 and opcion3 != 2:
                            print("Valor incorrecto")
                        elif opcion3 == 1:
                            while True:
                                identificacion = input("Ingrese la identificación del estudiante (Cedula): ")
                                if self.validar_cedula(identificacion):
                                    break
                                else:
                                    print("Formato de cedula invalido")
                            opcion_valida = True
                        elif opcion3 == 2:
                            identificacion = input("Ingrese la identificación del estudiante (Pasaporte): ")
                            opcion_valida = True
                        if opcion_valida:
                            break
                    nombreparticipante = input("Ingrese el nombre del estudiante: ")
                    while True:
                        sexo = input("Ingrese el sexo del estudiante (f para femenino y m para masculino): ")
                        if sexo.lower() != 'f' and sexo.lower() != 'm':
                            print("Valor incorrecto, intente de nuevo")
                        else:
                            break
                    while True:
                        email = input("Ingresar correo electronico del estudiante: ")
                        if self.validar_email(email):
                            break
                        else:
                            print("Cuenta de correo electronico en formato invalido")
                    nombreuneversidad = input("Favor ingresar el nombre de la universidad del estudiante")
                    while True:
                        try:
                            acursa= int(input("Ingrese el año que cursa el estudiante: (1=Primero,2=Segunto,3=Tercero,4=Cuarto,5=Quinto)"))
                            if acursa >= 1 and acursa <= 5:
                                break
                            else:
                                print("El valor debe estar entre 1 y 5")
                        except ValueError:
                            print("Tipo de dato incorrecto; intente nuevamente")
                    while True:
                        try:
                            ainteres = int(input(
                                "Ingrese el área de interés del profesor (1 =  Ciberseguridad, 2 =  "
                                "Computación en la Nube o 3 = Ciencia de Datos ):"))
                            if ainteres >= 1 and ainteres <= 3:
                                break
                            else:
                                print("No es una de las opciones")
                        except ValueError:
                            print("Dato incorrecto; intente nuevamente")
                    while True:
                        respuesta = input(f"Favor confirmar si va a guardar los datos del estudiante "
                                          f" {nombreparticipante} (s para si y n para no)")
                        if respuesta.lower() != 's' and respuesta.lower() != 'n':
                            while respuesta.lower() != 's' and respuesta.lower() != 'n':
                                print("Valor incorrecto intente de nuevo")
                                respuesta = input("Desea registrar los datos  (s para si y n para no): ")
                        elif respuesta.lower() == 's':
                            estudiante = Destudiante(identificacion, nombreparticipante, sexo,email,opcion2,nombreuneversidad,acursa,ainteres )

                            self.semi[numparticipante] = estudiante
                            print(f"Profesor{self.semi}")
                            print("El registro del participante fue exitoso(Estudiante)")
                            break
                        else:
                            numparticipante=-1
                            break

                case 3:
                    while True:
                        print("Favor Seleccionar el tipo de identificacion (Profesional)".center(70, '-'))
                        print(centro.center(70, '*'))
                        print("Menú".center(70, '-'))
                        print(centro.center(70, '*'))
                        print("1. Cedula")
                        print("2. Pasaporte")
                        opcion_valida = False
                        while True:
                            try:
                                opcion3 = int(input("Ingrese una opción: "))
                                break
                            except ValueError:
                                print("Tipo de dato incorrecto; intente nuevamente")
                        if opcion3 != 1 and opcion3 != 2:
                            print("Valor incorrecto")
                        elif opcion3 == 1:
                            while True:
                                identificacion = input("Ingrese la identificación del profesional (Cedula): ")
                                if self.validar_cedula(identificacion):
                                    break
                                else:
                                    print("Formato de cedula invalido")
                            opcion_valida = True
                        elif opcion3 == 2:
                            identificacion = input("Ingrese la identificación del profesional (Pasaporte): ")
                            opcion_valida = True
                        if opcion_valida:
                            break
                    nombreparticipante = input("Ingrese el nombre del profesional: ")
                    while True:
                        sexo = input("Ingrese el sexo del profesional (f para femenino y m para masculino): ")
                        if sexo.lower() != 'f' and sexo.lower() != 'm':
                            print("Valor incorrecto, intente de nuevo")
                        else:
                            break
                    while True:
                        email = input("Ingresar correo electronico del profesional: ")
                        if self.validar_email(email):
                            break
                        else:
                            print("Cuenta de correo electronico en formato invalido")
                    empresa = input("Favor ingresar la empresa del profesional")
                    cargo = input("Favor ingresar el cargo del profesional")
                    atrabajo = input("Favor ingresar el area de trabajo del profesional")
                    while True:
                        try:
                            aexperiencia = int(input("Favor ingresar los años de experiencia del profecional"))
                            if aexperiencia >= 0:
                                break
                            else:
                                print("El valor debe ser mayor igual a cero (0)")
                        except ValueError:
                            print("Tipo de dato incorrecto; intente nuevamente")
                    while True:
                        try:
                            nivelestudios = int(input("Favor ingresar el nivel estudio del profesional: (1 = Primaria, 2 = Secundaria, 3 = Superior"))
                            if nivelestudios >= 1 and nivelestudios <= 3:
                                break
                            else:
                                print("El valor no es valido")
                        except ValueError:
                            print("Tipo de dato incorrecto; intente nuevamente")
                    while True:
                        try:
                            ainteres = int(input(
                                "Ingrese el área de interés del profesional (1 =  Ciberseguridad, 2 =  "
                                "Computación en la Nube o 3 = Ciencia de Datos ):"))
                            if ainteres >= 1 and ainteres <= 3:
                                break
                            else:
                                print("No es una de las opciones")
                        except ValueError:
                            print("Dato incorrecto; intente nuevamente")
                    while True:
                        respuesta = input(f"Favor confirmar si va a guardar los datos del profesional "
                                          f" {nombreparticipante} (s para si y n para no)")
                        if respuesta.lower() != 's' and respuesta.lower() != 'n':
                            while respuesta.lower() != 's' and respuesta.lower() != 'n':
                                print("Valor incorrecto intente de nuevo")
                                respuesta = input("Desea registrar los datos  (s para si y n para no): ")
                        elif respuesta.lower() == 's':
                            profesional = Dprofessional(identificacion, nombreparticipante, sexo, email,opcion2,empresa,cargo,atrabajo,aexperiencia,nivelestudios,ainteres )
                            self.semi[numparticipante] = profesional
                            print(f"Profesional{self.semi}")
                            print("El registro del participante fue exitoso(profesional)")
                            break
                        else:
                            numparticipante=-1
                            break
                case _:
                    print("Opción inválida")

            respuestaf = input("Desea agregar otro participante (s para si y n para no):")
            if respuestaf.lower() != 's' and respuestaf.lower() != 'n':
                while respuestaf.lower() != 's' and respuestaf.lower() != 'n':
                    print("Valor incorrecto intente de nuevo")
                    respuesta = input("Desea agregar otro participante (s para si y n para no): ")
            elif respuestaf.lower() == 'n':
                break


class Menu():
    def menu(self):
        semi = Seminario()
        print(sys.version)
        while True:
            print("Bienvenido al mini proyecto 2 - seminario".center(70, '-'))
            # print("\n")
            print(centro.center(70, '*'))
            print("Menú".center(70, '-'))
            print(centro.center(70, '*'))
            print("1. Registrar asistentes.")
            print("2. Listar los asistentes inscritos con un área de interés X.")
            print("3. Listar los profesores inscritos.")
            print("4. Listar los profesores con una especialidad X.")
            print("5. Listar profesionales con X años de experiencia.")
            print("6. Listar los estudiantes inscritos de una Universidad X.")
            print("7. Porcentaje de estudiantes, profesores y profesionales participando del diplomado.")
            print("8. Salir")
            try:
                opcion = int(input("Ingrese una opción: "))
            except ValueError:
                print("Dato incorrecto; intente nuevamente")
            print("\n")
            print(centro.center(70, '='))

            match opcion:
                case 1:
                    semi.registrar()
                case 2:
                    semi.consultaInteres()

                case 3:
                    semi.consultaProfesores()

                case 4:
                    semi.consultaProfesoresEspecialidad()

                case 5:
                    semi.consultaProfesionalExp()
                case 6:
                    semi.consultaEu()
                case 7:
                    semi.porcentajes()
                case 8:
                    print("Gracias por utilizar las opciones, cerro:", datetime.now())
                    break
                case _:
                    print("Opción inválida")

menu=Menu()
menu.menu()