import time

class Vehiculo:
    def __init__(self, velocidad_maxima, capacidad_gasolina, conductor):
        self.velocidad_maxima = velocidad_maxima
        self.capacidad_gasolina = capacidad_gasolina
        self.conductor = conductor
        self.velocidad_actual = 0
        self.gasolina_actual = capacidad_gasolina
        self.kilometraje = 0
        self.puntos = 0

    def acelerar(self):
        pass

    def frenar(self):
        pass

    def recorrido(self, tiempo):
        pass

    def repostar_gasolina(self):
        self.gasolina_actual = self.capacidad_gasolina

class Coche(Vehiculo):
    def acelerar(self):
        if self.gasolina_actual > 0:
            self.velocidad_actual += 10
            self.gasolina_actual -= 1

    def frenar(self):
        if self.velocidad_actual > 0:
            self.velocidad_actual -= 10

    def recorrido(self, tiempo):
        return self.velocidad_actual * tiempo

class Moto(Vehiculo):
    def acelerar(self):
        if self.gasolina_actual > 0:
            self.velocidad_actual += 5
            self.gasolina_actual -= 0.5

    def frenar(self):
        if self.velocidad_actual > 0:
            self.velocidad_actual -= 5

    def recorrido(self, tiempo):
        return self.velocidad_actual * tiempo

class Carrera:
    def __init__(self, distancia_pista, duracion_carrera):
        self.distancia_pista = distancia_pista
        self.duracion_carrera = duracion_carrera
        self.vehiculos = []
        self.ranking = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def iniciar_carrera(self):
        tiempo_inicio = time.time()

        while time.time() - tiempo_inicio < self.duracion_carrera:
            for vehiculo in self.vehiculos:
                vehiculo.acelerar()
                vehiculo.frenar()
                distancia_recorrida = vehiculo.velocidad_maxima * (time.time() - tiempo_inicio)
                vehiculo.kilometraje += distancia_recorrida
                if vehiculo.kilometraje >= self.distancia_pista and vehiculo.puntos == 0:
                    vehiculo.puntos = time.time() - tiempo_inicio
                    self.ranking.append((vehiculo.conductor, vehiculo.puntos))

            time.sleep(1)

        for vehiculo in self.vehiculos:
            if vehiculo.kilometraje >= self.distancia_pista and vehiculo.puntos == 0:
                vehiculo.puntos = time.time() - tiempo_inicio
                self.ranking.append((vehiculo.conductor, vehiculo.puntos))

coche1 = Coche(1000, 50, "Daniel")
coche2 = Coche(180, 40, "Antonio")
moto1 = Moto(150, 30, "Rodrigo")

carrera = Carrera(1000, 3)
carrera.agregar_vehiculo(coche1)
carrera.agregar_vehiculo(coche2)
carrera.agregar_vehiculo(moto1)

carrera.iniciar_carrera()

for i, (conductor, tiempo) in enumerate(carrera.ranking):
    print(f"Lugar {i+1} --> Corredor: {conductor}, Tiempo de Carrera: {tiempo}")
