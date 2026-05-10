class Administrador:
    def __init__(self):
        self.password = "edu2026"
    
    def validar_clave(self, clave):
        if self.password == clave:
            return True
        else:
            return False