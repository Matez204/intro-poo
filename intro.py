

class animal:
    def __init__(self,nombre,raza):
        self.nombre = nombre
        self.raza = raza

    def pasear(self):
        pass
    def alimentar(self):
        pass
    def info(self):
        return self.nombre + " de raza " + self.raza

class mascota(animal):
    def __init__(self,nombre, raza, propietario):
        self.propietario=propietario
        super(mascota,self).__init__(nombre,raza)

class gato(animal):
    def pasear(self):
        print("Paseando al gato " + self.info())
    def alimentar(self):
        print("Alimentando al gato " + self.info())

class perro(animal):
    def pasear(self):
        print("Paseando al perro " + self.info())
    def alimentar(self):
        print("Alimentando al perro " + self.info())

class pejelagarto(animal):
    def pasear(self):
        print("Paseando al pejelagarto " + self.info())
    def alimentar(self):
        print("Alimentando al pejelagarto " + self.info())

if __name__== '__main__':
    m=[gato("Juan","Meztio"),perro("fifas", "Chaclon"),pejelagarto("alfredo","verde")]
    for i in m:
        i.pasear()
        i.alimentar()