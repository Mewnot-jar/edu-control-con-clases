class Alumno:
    def __init__(self, rut, nombre, apellido, curso):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.password = None

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

def buscar_alumno_por_rut(rut):
    for alumno in registro_global.values():
        if rut in alumno:
            return alumno[rut]
    return None

def panel_admin():
    password = "edu2026"
    intento = input("Ingresa la clave del administrador: ")

    if intento != password:
        print("Acceso denegado.")
        return
    print("------------- Registro de alumnos -------------")
    rut = input("RUT: ")
    if buscar_alumno_por_rut(rut):
        print("Error: El rut ingresado ya existe!")
        return

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    
    for i, nivel in enumerate(cursos, start=1):
        print(f"{i}. {nivel}")
    seleccion = input("  Seleccione el numero del curso: ")

    try:
        indice = int(seleccion) - 1
        if indice < 0 or indice >= len(cursos):
            raise ValueError
        curso = cursos[indice]
    except ValueError:
        print("Seleccion de curso no valida.")
        return
    
    print(rut)
    print(nombre)
    print(apellido)
    print(curso)
panel_admin()