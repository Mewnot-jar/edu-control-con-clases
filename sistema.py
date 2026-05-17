import alumno as Alumno

class Sistema:
    def __init__(self, colegio, admin):
        self.colegio = colegio
        self.admin = admin
        self.sesion_alumno = None

    def iniciar_aplicacion(self):
        while True:
            print("----------- EduControl -----------")
            print("1. Panel de administrador.")
            print("2. Panel de alumno.")
            print("3. Salir")
            opcion = input("A que panel deseas acceder: ")
            match opcion:
                case "1":
                    self.panel_admin()
                    continue
                case "2":
                    self.panel_alumno()
                    continue
                case "3":
                    print("Saliendo del sistema...")
                    break
                case _:
                    print("La opcion no es correcta.")
                    continue

    def validacion_clave(self, rut=""):
    #Validacion de identidad del alumno
        if rut:
            alumno = self.colegio.buscar_alumno_registro(rut)
            intentos = 3
            while intentos > 0:
                clave = input("Ingrese su clave: ")
                if alumno.validar_clave(clave):
                    return True
                intentos -= 1
                print(f"Clave incorrecta. Te quedan {intentos} intentos.")
                input("Pulsa ENTER para volver a intentar...")
            else:
                print("Demasiados intentos fallidos. Acceso denegado.")
                return False
        #Validacion de identidad del administrador
        else:
            intentos = 3
            while intentos > 0:
                clave = input("Ingrese la clave de administrador: ")
                if self.admin.validar_clave(clave):
                    return True
                intentos -= 1
                print(f"Clave incorrecta. Te quedan {intentos} intentos.")
                input("Pulsa ENTER para volver a intentar...")
            else:
                print("Demasiados intentos fallidos. Acceso denegado.")
                return False
    def panel_admin(self):
        #Funcion para validar la clave / "" = administrador
        if not self.validacion_clave():
            return
        while True:
            print("----------- Menu de administrador -----------")
            print("1. Registrar un nuevo alumno.")
            print("2. Buscar alumno por rut.")
            print("3. Salir")
            opcion = input("Ingrese la opcion que requiere realizar: ")
            match opcion:
                case "1":
                    #Llamamos a la funcion para registrar un alumno
                    self.registrar_alumno()
                case "2":
                    #Le entregamos el rut que queremos buscar
                    rut_a_buscar = input("Ingresa el rut que quieres buscar: ")
                    #Llamamos a la funcion para obtener la ficha
                    self.obtener_ficha_academica(rut_a_buscar)
                case "3":
                    #Salimos del menu de administrador
                    print("Saliendo del sistema...")
                    return
                case _:
                    #Validamos la opcion que no esta en nuestro menu
                    print("Opcion no valida")
                    continue
    def registrar_alumno(self):
        print("----------- Crear a nuevo alumno -----------")
        #Validacion para el RUT
        while True:
            rut = input("RUT del alumno: ").strip()
            if not rut:
                print("Error: El campo RUT no puede estar vacio.")
                continue
            if self.colegio.buscar_alumno_registro(rut):
                print("Error: El rut ingresado ya existe.")
                continue
            break
        #Validacion para el Nombre y el Apellido
        while True:
            nombre = input("Nombre: ").strip().capitalize()
            apellido = input("Apellido: ").strip().capitalize()
            if not nombre or not apellido:
                print("Error: El campo nombre y el campo apellido no puede estar vacio.")
                continue
            break
        #Seleccion de cursos
        while True:
            #Despliegue de los cursos
            for i, nivel in enumerate(self.colegio.obtener_cursos(), start=1):
                print(f"{i}. {nivel}")
            seleccion = input("Seleccione el numero del curso: ")
            #Validacion para el curso
            if seleccion != "" and seleccion.isnumeric():
                indice = int(seleccion) - 1
                if indice < 0 or indice >= len(self.colegio.obtener_cursos()):
                    print("Opcion no valida.")
                    input("Pulsa ENTER para volver a intentar...")
                    continue
                curso = self.colegio.obtener_cursos()[indice]
                break
            else:
                print("Opcion no valida.")
                input("Pulsa ENTER para volver a intentar...")
                continue
        #Instancia de la clase Alumno con sus propiedades
        alumno = Alumno.Alumno(rut, nombre, apellido, curso)
        #Agregamos al almuno al registro mediante el objeto registro_colegio
        self.colegio.agregar_registro(alumno)
        #Mostramos la ficha del alumno que creamos
        print("----------- Alumno Creado Exitosamente -----------")
        alumno.mostrar_ficha()
        input("Pulsa ENTER para continuar...")

    def obtener_ficha_academica(self, rut):
        #Buscamos al alumno mediante el rut
        alumno = self.colegio.buscar_alumno_registro(rut)
        if alumno:
            #Si encontramos al alumno mostramos su ficha
            print(f"----------- Ficha academica -----------")
            alumno.mostrar_ficha()
            input("Pulsa ENTER para continuar...")
        else:
            #Si no lo encontramos le avisamos
            print("Rut no encontrado en la base de datos.")
            input("Pulsa ENTER para continuar...")

    def panel_alumno(self):
        #le pedimos al alumno que ingrese su rut
        rut_ingreso = input("Ingrese su RUT: ")
        #Lo buscamos
        alumno = self.colegio.buscar_alumno_registro(rut_ingreso)
        #Validamos si lo encontramos o no
        if not alumno:
            print("El alumno no existe.")
            input("Pulsa ENTER para continuar...")
            return
        #Si lo encontramos validamos si cuenta con clave
        if not alumno.password:
            #Si no cuenta con clave la creamos
            self.gestionar_clave_alumno(alumno.rut)
        else:
            #Si cuenta con clave la validamos
            if not self.validacion_clave(alumno.rut):
                return
        #Logramos pasar al menu del alumno
        while True:
            print("----------- Menu de alumno -----------")
            print("1. Actualizar credenciales.")
            print("2. Ficha academica.")
            print("3. Certificado de matricula.")
            print("4. Salir")
            #Le preguntamos al alumno que opcion solicita
            opcion = input("Ingrese la opcion que requiere realizar: ")
            match opcion:
                case "1":
                    #Actualizamos sus credenciales (clave)
                    self.gestionar_clave_alumno(alumno.rut)
                    continue
                case "2":
                    #Mostramos su ficha academica
                    self.obtener_ficha_academica(alumno.rut)
                    continue
                case "3":
                    #Generamos su certificado de matricula
                    self.generar_certificado(alumno.rut)
                    continue
                case "4":
                    #Salimos del menu de alumno
                    print("Saliendo del sistema...")
                    break
                case _:
                    #Validamos la opcion que no se encuentra en nuestro menu
                    print("Opcion no valida.")
                    input("Pulsa ENTER para volver a intentar...")
    def gestionar_clave_alumno(self, rut):
        #Buscamos al alumno mediante el rut
        alumno = self.colegio.buscar_alumno_registro(rut)
        #Si no encontramos su clave
        if not alumno.password:
            #La crearemos
            while True:
                #El alumno ingresa su clave y la validamos dos veces con .strip() le quitamos los espacios al texto
                clave_alumno = input(f"Debes crear tu clave sin espacios: ").strip()
                clave_alumno2 = input("Repite la clave: ").strip()
                #Validamos si las claves no estan vacias y si coinciden
                if clave_alumno == clave_alumno2 and clave_alumno != "":
                    #Establecemos la clave del alumno
                    alumno.establecer_clave(clave_alumno)
                    print("Operacion completada con exito.")
                    input("Pulsa ENTER para continuar...")
                    return
                else:
                    #Le indicamos al alumno que hubo un error
                    print("Las claves no coinciden o estan vacias.")
                    input("Pulsa ENTER para continuar...")
                    
        #Por otro lado si encontramos que el alumno si cuenta con clave
        else:
            #La validaremos
            if not self.validacion_clave(rut):
                return
            #Si valida su clave con exito la modificaremos
            while True:
                #El alumno ingresa su clave y la validamos dos veces con .strip() le quitamos los espacios al texto
                clave_alumno = input(f"Debes modificar tu clave sin espacios: ").strip()
                clave_alumno2 = input("Repite la clave: ").strip()
                #Validamos si las claves no estan vacias y si coinciden
                if clave_alumno == clave_alumno2 and clave_alumno != "":
                    #Establecemos la clave del alumno
                    alumno.establecer_clave(clave_alumno)
                    print("Operacion completada con exito.")
                    input("Pulsa ENTER para continuar...")
                    return
                else:
                    #Le indicamos al alumno que hubo un error
                    print("Las claves no coinciden o estan vacias.")
                    input("Pulsa ENTER para continuar...")
                    continue
    def obtener_ficha_academica(self, rut):
        #Buscamos al alumno mediante el rut
        alumno = self.colegio.buscar_alumno_registro(rut)
        if alumno:
            #Si encontramos al alumno mostramos su ficha
            print(f"----------- Ficha academica -----------")
            alumno.mostrar_ficha()
            input("Pulsa ENTER para continuar...")
        else:
            #Si no lo encontramos le avisamos
            print("Rut no encontrado en la base de datos.")
            input("Pulsa ENTER para continuar...")
    def generar_certificado(self, rut):
        #Buscamos al alumno mediante el rut
        alumno = self.colegio.buscar_alumno_registro(rut)
        if alumno:
            #Si lo encontramos validamos su clave
            if not self.validacion_clave(rut):
                #Si no valida su clave volvemos al menu de alumno
                return
            #Si valida su clave generamos el certificado
            print(f"----------- Certificado de matricula -----------")
            alumno.generar_certificado()
            input("Pulsa ENTER para continuar...")
