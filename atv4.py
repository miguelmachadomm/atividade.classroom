class Cabeça:
    def _init_(self, cor):
        self.cor = cor

    def _str_(self):
        return f"Cabeça da cor {self.cor}"

class Boneco:
    def _init_(self, nome, cor_cabeça):
        self.nome = nome
        self.cabeça = Cabeça(cor_cabeça)

    def destruir(self):
        
        del self.cabeça

    def _str_(self):
        return f"Boneco {self.nome} com {self.cabeça}"


boneco1 = Boneco("Boneco A", "azul")
print(boneco1)

boneco2 = Boneco("Boneco B", "vermelho")
print(boneco2)

boneco1.destruir()

print(boneco1.cabeça)