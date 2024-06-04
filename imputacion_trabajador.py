class ImputacionTrabajador:
    def __init__(self, nombre, id_codigo, fecha, horas_imputadas):
        self.nombre = nombre
        self.id_codigo = id_codigo
        self.horas_imputadas = horas_imputadas
        self.fecha = fecha
    
    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"ID de Código: {self.id_codigo}\n"
                f"Horas Imputadas: {self.horas_imputadas}\n"
                f"Fecha: {self.fecha}")