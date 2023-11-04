class Monitor:
    def _init_(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho
        self.computador_conectado = None

    def conectar_a_computador(self, computador):
        self.computador_conectado = computador

    def desconectar_do_computador(self):
        self.computador_conectado = None

    def _str_(self):
        if self.computador_conectado:
            return f"Monitor {self.marca}, Tamanho {self.tamanho}, Conectado ao Computador: {self.computador_conectado.nome}"
        else:
            return f"Monitor {self.marca}, Tamanho {self.tamanho}, Não Conectado a um Computador"

class Computador:
    def _init_(self, nome):
        self.nome = nome

    def _str_(self):
        return f"Computador: {self.nome}"


computador1 = Computador("PC A")
monitor1 = Monitor("Marca X", 24)

monitor1.conectar_a_computador(computador1)

print(monitor1)
print(computador1)

monitor1.desconectar_do_computador()

print(monitor1)