class Humano:
    def __init__ (self, nombre, armadura, ataque, nivel = 57, ojos=2, piernas=2, dientes=32, salud=100):
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel  
        self.ataque = ataque
        self.salud = salud

    def atacar(self, orco):
        ataque = self.ataque - orco.armadura
        orco.salud = orco.salud - self.ataque
        print (f'la vida restante del {orco.nombre} es: {orco.salud}')
        return orco.salud

    def novivo(self):
        if self.salud <= 0:
            return True
        else:
            return False

    def mostrar(self):
        print (f' Nombre: {self.nombre} | ojos: {self.ojos}| dientes: {self.dientes} | piernas: {self.piernas} | armadura: {self.armadura} | nivel: {self.nivel} | salud: {self.salud}| ataque: {self.ataque}')




C:\Users\ggarr\OneDrive\Escritorio\Data_Science\The Bridge\Gina\week3_course_python_III\day2_python_VIII\exercises\classes_import\object\ClaseHumano.py
	



        