class Trabajador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horas = [0] * 31  # Inicializa un array con 31 días (para el mes más largo)

    def sumar_horas(self, horas, fecha):
        dia = fecha.day  # Obtenemos el día de la fecha
        self.horas[dia-1] += horas  # Sumamos las horas al día correspondiente
    
    def get_horas_dia(self, fecha):
        dia = fecha.day  # Obtenemos el día de la fecha
        return self.horas[dia - 1] # Sumamos las horas al día correspondiente

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'horas': self.horas
        }

    def __str__(self):
        return f'Trabajador: {self.nombre}, Horas: {self.horas}'