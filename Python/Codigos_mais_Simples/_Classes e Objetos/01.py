class Animal():
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, sou um(a) {self.especie} e tenho {self.idade} anos.")
    
    def fazer_som(self, som):
        if self.especie == "Cachorro":
            print(f"{self.especie}: Au Au!")
        elif self.especie == "Gato":
            print(f"{self.especie}: Miau!")
        elif self.especie == "Galinha":
            print(f"{self.especie}: PoPo!")
        else:
            print(f"{self.especie}: Esqueci o barulho que faço..")
        
    
p1 = Animal("Cabelinho", 1, "Cachorro")
p2 = Animal("Savana", 2, "Gato")

p1.apresentar()
p1.fazer_som("")
print()
p2.apresentar()
p2.fazer_som("")