class Colegio:
    def __init__(self):
        self.registro_global = {
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
    def obtener_registro(self):
        return self.registro_global
    
    def obtener_cursos(self):
        return list(self.registro_global.keys())
    
    def agregar_registro(self, alumno):
        self.registro_global[alumno.curso][alumno.rut] = alumno

    def buscar_alumno_registro(self, rut):
        for alumno in self.registro_global.values():
            if rut in alumno:
                return alumno[rut]

