class Auto:

    def __init__(self, modelo = None, precio = None, asientos = [], marca = None, motor = None, registro = None, cantidadCreados = None):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidad = cantidadCreados

    def cantidadAsientos(self):
        return len([asiento for asiento in self.asientos if asiento is not None])
    
    def verificarIntegridad(self):
        for asiento in self.asientos:
            if asiento is not None and asiento.registro != self.registro:
                return "Las piezas no son originales"
        if self.motor.registro != self.registro:
            return "Las piezas no son originales"
        return "Auto original"