class Animal:
    def __init__(self, nivel):
        self.__nome = None
        self.nivel = nivel

        self._hp = 0
        self._atk = 0
        self.__recompensa = nivel

    #GETTERS
    @property
    def nome(self):
        return self.__nome

    @property
    def hp(self):
        return self._hp

    @property
    def atk(self):
        return self._atk

    @property
    def recompensa(self):
        return self.__recompensa

    #setters
    @hp.setter
    def hp(self, valor):
        self._hp = valor

    @atk.setter
    def atk(self, valor):
        self._atk = valor

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @recompensa.setter
    def recompensa(self, valor):
        self.__recompensa = valor


class Lobo(Animal):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.nome = 'Lobo'

        self.hp = 3 * self.nivel
        self.atk = 2 * self.nivel
        self.recompensa *= 2


class LoboAlfa(Animal):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.nome = 'Lobo Alfa'

        self.hp = 3 * self.nivel * 2
        self.atk = 2 * self.nivel * 2

        self.recompensa *= 4


class Aranha(Animal):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.nome = 'Aranha Gigante'

        self.hp = 2 * self.nivel
        self.atk = 3 * self.nivel

        self.recompensa *= 1


class AranhaAlfa(Animal):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.nome = 'Aranha Gigante Alfa'

        self.hp = 2 * self.nivel * 2
        self.atk = 3 * self.nivel * 2

        self.recompensa *= 2


def test(x):
    print('nome:      ', x.nome)
    print('nivel:     ', x.nivel)
    print('hp:        ', x.hp)
    print('atk:       ', x.atk)
    print('recompensa:', x.recompensa)
