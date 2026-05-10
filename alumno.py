class Alumno:
    def __init__(self, rut, nombre, apellido, curso):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.password = None
    
    def establecer_clave(self, clave):
        self.password = clave
        return True
    
    def validar_clave(self, clave):
        if self.password == clave:
            return True
        else:
            return False
        
    def mostrar_ficha(self):
        print(f"Nombre del alumno: {self.nombre} {self.apellido}")
        print(f"RUT del alumno: {self.rut}")
        print(f"Curso del alumno: {self.curso}")

    def generar_certificado(self):
        print(f"El alumno {self.nombre} {self.apellido} se encuentra regularizado en el nivel {self.curso}")
