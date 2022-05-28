class Jogador:
    def __init__(self, nome, nivel=1):
        '''
        Uma pessoa, uai...
        :param nome: nome kkk
        '''
        self.__classe = self.__class__.__name__

        self._nivel = nivel

        self._xp = 0
        self._rating = self.nivel * (1 + 30 / 100) * 10

        self._nome = nome

        self._hp = None
        self._maxHP = self.nivel
        self._baseHP = None

        self._atk = None
        self._baseATK = None
        self._inv = {}

    # GETTERS
    # Atributos gerais
    @property
    def classe(self):
        return self.__classe

    @property
    def nome(self):
        return self._nome

    #Atributos de Nível
    @property
    def nivel(self):
        return self._nivel

    @property
    def xp(self):
        return self._xp

    @property
    def rating(self):
        return self._rating

    # Atributos uteis
    @property
    def maxHP(self):
        return self._maxHP

    @property
    def hp(self):
        return self._hp

    @property
    def baseHP(self):
        return self._baseHP

    @property
    def inv(self):
        return self._inv

    @property
    def atk(self):
        return self._atk

    @property
    def baseATK(self):
        return self._baseATK


    #SETTERS
    #Atributos gerais
    @nome.setter
    def nome(self, valor: str):
        self._nome = valor

    #Atributos de Nivel
    @xp.setter
    def xp(self, valor: int):
        self._xp = valor

    @nivel.setter
    def nivel(self, valor: int):
        self._nivel = valor

    @rating.setter
    def rating(self, valor: int):
        self._rating = valor

    # Atributos uteis
    @hp.setter
    def hp(self, valor: int):
        self._hp = valor

    @maxHP.setter
    def maxHP(self, valor: int):
        self._maxHP = valor

    @baseHP.setter
    def baseHP(self, valor):
        self._baseHP = valor

    @inv.setter
    def inv(self, valor: dict):
        self._inv = valor

    @atk.setter
    def atk(self, valor: int):
        self._atk = valor

    @baseATK.setter
    def baseATK(self, valor: int):
        self._baseATK = valor


    #METODOS
    def status(self):
        print(f'+{"-" * 29}+\n'
              f'| Nome: {self.nome:>21} |\n'
              f'| Classe: {self.classe:>19} |\n'
              f'|{"-" * 29}|\n'
              f'| Nivel: {self.nivel:>20} |\n'
              f'| Prox Nível: {f"[{self.xp:.0f} / {self.rating:.0f}]":>15} |\n'
              f'| Saúde: {self.hp:>20} |\n'
              f'| Ataque: {self.atk:>19} |\n'
              f'+{"-" * 29}+\n')

    def uppar(self, pontos: int):

        self.xp += pontos

        #enquanto o personagem tiver xp o suficiente para upar, ele vai upar.
        while self.xp >= self.rating:

            #melhorias caso ele upe.
            if self.xp >= self.rating:
                self.nivel += 1

                self.maxHP += self.baseHP
                self.hp = self.maxHP #enche o hp do personagem

                self.atk += self.baseATK

            #resto do xp após upar.
            self.xp = pontos - self.rating
            pontos = self.xp

            #atualiza o rating para o nivel atual do personagem.
            self.rating = self.nivel * (1 + 30 / 100) * 10


class Guerreiro(Jogador):
    def __init__(self, nome, nivel=1):
        super().__init__(nome, nivel)
        #HP
        self.baseHP = 10
        self.hp = 60 + (self.baseHP * self.nivel)
        self.maxHP = self.hp

        #ATK
        self.baseATK = 2
        self.atk = 0 + (self.baseATK * self.nivel)


class Mago(Jogador):
    def __init__(self, nome, nivel=1):
        super().__init__(nome, nivel)
        #HP
        self.baseHP = 8
        self.hp = 50 + (self.baseHP * self.nivel)
        self.maxHP = self.hp

        #ATK
        self.baseATK = 4
        self.atk = 0 + (self.baseATK * self.nivel)


class Bestial(Jogador):
    def __init__(self, nome, nivel=1):
        super().__init__(nome, nivel)
        #HP
        self.baseHP = 2
        self.hp = 30 + (self.baseHP * self.nivel)
        self.maxHP = self.hp

        #ATK
        self.baseATK = 10
        self.atk = 5 + (self.baseATK * self.nivel)
