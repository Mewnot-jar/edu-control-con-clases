import colegio as Colegio
import administrador as Administador
import sistema as Sistema
#Instancia de la clase Colegio
colegio = Colegio.Colegio()
#Instancia de la clase Administrador
admin = Administador.Administrador()

sistema = Sistema.Sistema(colegio, admin)

if __name__ == "__main__":
    sistema.iniciar_aplicacion()
