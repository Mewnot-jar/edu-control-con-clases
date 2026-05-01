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

    #Validacion pasada - Aqui iran las funciones que despliegan los otros menus
    registrar_alumno()


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
            print("Error: El rut ingresado ya existe!")
            continue
        break

    #Validacion para el Nombre y el Apellido
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    if not nombre or not apellido:
        print("Error: El campo nombre y el campo apellido no puede estar vacio.")
        return
    
    #Despliegue de los cursos
    for i, nivel in enumerate(cursos, start=1):
        print(f"{i}. {nivel}")
    seleccion = input("Seleccione el numero del curso: ")
    #Validacion para el curso
    try:
        indice = int(seleccion) - 1
        if indice < 0 or indice >= len(cursos):
            raise ValueError
        curso = cursos[indice]
    except ValueError:
        print("Seleccion de curso no valida.")
        return
    
    #Creacion del objeto alumno de la clase Alumno
    alumno = Alumno(rut, nombre, apellido, curso)
    registro_global[curso][rut] = alumno

    print("----------- Alumno Creado Exitosamente -----------")
    print(f"RUT Alumno: {alumno.rut}")
    print(f"Nombre Alumno: {alumno.nombre}")
    print(f"Apellido Alumno: {alumno.apellido}")
    print(f"Curso Alumno: {alumno.curso}")

panel_admin()
