class Motor:

    def __init__(self, numeroCilindros = None, tipo = None, registro = None):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        if type(registro) is int:
            self.registro = registro

    def asignarTipo(self, tipo):
        if tipo in ["electrico", "gasolina"]:
            self.tipo = tipo