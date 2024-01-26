# Personagem : classe mae
# Heroi : Controlado pelo usuario
# Inimigo: adversario do usuario

class Personagem:
    def __init__(self,nome,vida,nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Name: {self.get_nome()}\nHP: {self.get_vida()}\nLevel: {self.get_nivel()}"
    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel,habilidade) -> None:
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nSkill: {self.get_habilidade()}"
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel,tipo) -> None:
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nType: {self.get_tipo()}"

class Jogo:
    """ Classe orquestradora do jogo Python Hero """

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Main Hero", vida=100, nivel=5, habilidade="Super Strenght")
        self.inimigo = Inimigo(nome="Bat",vida=50,nivel=3,tipo="Flying")
    
    def iniciar_batalha(self):
        print("Iniciando batalha")
        while self.heroi.get_vida() >0 and self.inimigo.get_vida()>0:
            print("\n Characters:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Press [ENTER] to attack...")
            escolha = input("Available Actions: (1 - Attack , 2 - Skill)")

# Criar instância do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()

