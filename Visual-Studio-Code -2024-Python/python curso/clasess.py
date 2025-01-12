class aHuman:
    def __init__(self, altura, edad, peso):
        self.altura = altura
        self.edad = edad
        self.peso = peso
        
    def comer(self):
        print(f" el humano de {self.edad} años esta comiendo")

human_1 = aHuman(1.80, 23, 87)

print(f"el humano 1 mide {human_1.altura}, pesa {human_1.peso}kg y tiene {human_1.edad} años")

human_1.comer()
