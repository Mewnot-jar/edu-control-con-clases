#Clase Alumno
class Alumno:
    def __init__(self, rut, nombre, apellido, curso):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.password = None

#Diccionario con los registros de alumnos
registro_global = {
    "1ro Basico": {},
    "2do Basico": {},
    "3ro Basico": {},
    "4to Basico": {},
    "5to Basico": {},
    "6to Basico": {},
    "7mo Basico": {},
    "8vo Basico": {},
    "1ro Medio": {},
    "2do Medio": {},
    "3ro Medio": {},
    "4to Medio": {},
}

#Cursos validos
cursos = [
    "1ro Basico",
    "2do Basico", 
    "3ro Basico", 
    "4to Basico",
    "5to Basico", 
    "6to Basico", 
    "7mo Basico", 
    "8vo Basico",
    "1ro Medio", 
    "2do Medio", 
    "3ro Medio", 
    "4to Medio",
]

clave_maestra = "edu2026"

#Funcion para saber si el alumno existe y devolverlo
def buscar_alumno_por_rut(rut):
    for alumno in registro_global.values():
        if rut in alumno:
            return alumno[rut]
    return None

#Funcion que despliega el menu de administrador
def panel_admin():

    #Validacion de intentos
    intentos = 3
    while intentos > 0:
        clave = input("Ingresa la clave del administrador: ")
        if clave == clave_maestra:
            break
        intentos -= 1
        print(f"Clave incorrecta. Te quedan {intentos} intentos.")
    else:
        print("Demasiados intentos fallidos. Acceso denegado.")
        return
    

    while True:
        print("----------- Menu de administrador -----------")
        print("1. Registrar un nuevo alumno.")
        print("2. Buscar alumno por rut.")
        print("3. Salir")
        opcion = input("Ingrese la opcion que requiere realizar: ")
        match opcion:
            case "1":
                registrar_alumno()
            case "2":
                print("----------- Buscar alumno por RUT -----------")
                rut_buscar = input("Ingresa el rut del alumno que quieres buscar: ")
                alumno_encontrado = buscar_alumno_por_rut(rut_buscar)
                if alumno_encontrado:
                    print(f"RUT del alumno: {alumno_encontrado.rut}")
                    print(f"Nombre del alumno: {alumno_encontrado.nombre} {alumno_encontrado.apellido}")
                    print(f"Curso del alumno: {alumno_encontrado.curso}")
                    input("Pulsa cualquier tecla para continuar...")
                else:
                    print("Alumno no encontrado.")
                    input("Pulsa ENTER para continuar...")
            case "3":
                print("Saliendo del sistema...")
                return
            case _:
                print("Opcion no valida")
                continue

    #Validacion pasada - Aqui iran las funciones que despliegan los otros menus
    
#Funcion de registrar alumno nuevo
def registrar_alumno():
    print("----------- Registrar a nuevo alumno -----------")
    #Validacion para el RUT
    while True:
        rut = input("RUT del alumno: ").strip()
        if not rut:
            print("Error: El campo RUT no puede estar vacio.")
            continue
        if buscar_alumno_por_rut(rut):
            print("Error: El rut ingresado ya existe.")
            continue
        break

    #Validacion para el Nombre y el Apellido
    while True:
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        if not nombre or not apellido:
            print("Error: El campo nombre y el campo apellido no puede estar vacio.")
            continue
        break
    
    
    while True:
        #Despliegue de los cursos
        for i, nivel in enumerate(cursos, start=1):
            print(f"{i}. {nivel}")
        seleccion = input("Seleccione el numero del curso: ")
        #Validacion para el curso
        if seleccion != "":
            indice = int(seleccion) - 1
            if indice < 0 or indice >= len(cursos):
                raise ValueError
            curso = cursos[indice]
            break
        else:
            print("El curso no puede estar vacio!")
            input("Pulsa ENTER para volver a intentar...")
            continue
    
    #Creacion del objeto alumno de la clase Alumno
    alumno = Alumno(rut, nombre, apellido, curso)
    registro_global[curso][rut] = alumno

    print("----------- Alumno Creado Exitosamente -----------")
    print(f"RUT Alumno: {alumno.rut}")
    print(f"Nombre Alumno: {alumno.nombre}")
    print(f"Apellido Alumno: {alumno.apellido}")
    print(f"Curso Alumno: {alumno.curso}")
    input("Pulsa ENTER para continuar...")

#Funcion que despliega el menu de alumno
def panel_alumno():
    rut_ingreso = input("Ingrese su RUT: ")
    alumno_encontrado = buscar_alumno_por_rut(rut_ingreso)
    if not alumno_encontrado:
        print("El alumno no existe.")
        input("Pulsa ENTER para continuar...")
        return
    if not alumno_encontrado.password:
        while True:
            clave_alumno = input("Debes crear una clave sin espacios: ").strip()
            clave_alumno2 = input("Repite la clave: ").strip()
            if clave_alumno == clave_alumno2 and clave_alumno != "":
                alumno_encontrado.password = clave_alumno
                break
            else:
                print("Las claves no coinciden o estan vacias.")
                input("Pulsa ENTER para continuar...")
                continue
    else:
        while True:
            clave_sesion = input("Ingresa tu clave: ")
            if clave_sesion == alumno_encontrado.password:
                break
    
    while True:
        print("----------- Menu de alumno -----------")
        print("1. Actualizar credenciales.")
        print("2. Ficha academica.")
        print("3. Certificado de matricula.")
        print("4. Salir")
        opcion = input("Ingrese la opcion que requiere realizar: ")
        match opcion:
            case "1":
                panel_admin()
                continue
            case "2":
                panel_alumno()
                continue
            case "3":
                print("Saliendo del sistema...")
                continue
            case "4":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opcion no valida.")
                input("Pulsa ENTER para volver a intentar...")

#Funcion que despliega el menu de principal
def panel_principal():
    while True:
        print("----------- EduControl -----------")
        print("1. Panel de administrador.")
        print("2. Panel de alumno.")
        print("3. Salir")
        opcion = input("A que panel deseas acceder: ")
        match opcion:
            case "1":
                panel_admin()
                continue
            case "2":
                panel_alumno()
                continue
            case "3":
                print("Saliendo del sistema...")
                break




panel_principal()
