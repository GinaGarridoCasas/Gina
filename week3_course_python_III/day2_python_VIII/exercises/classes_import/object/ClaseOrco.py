class Orco:
    def __init__ (self, nombre, armadura, ataque, nivel = 38, ojos=2, piernas=2, dientes=56, salud=100):
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.salud = salud

    def atacar(self, humano):
        ataque = self.ataque - humano.armadura
        humano.salud = humano.salud - self.ataque
        print (f'la vida restante del {humano.nombre} es: {humano.salud}')
        return humano.salud

    def novivo(self):
        if self.salud <= 0:
            return True
        else:
            return False

    def mostrar(self):
        print (f' Nombre: {self.nombre} | ojos: {self.ojos}| dientes: {self.dientes} | piernas: {self.piernas} | armadura: {self.armadura} | nivel: {self.nivel} | salud: {self.salud}| ataque: {self.ataque}')

