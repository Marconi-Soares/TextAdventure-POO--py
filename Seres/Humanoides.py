class Humanoide:
    def __init__(self, nivel):
        self._nome = None
        self.nivel = nivel

        self._hp = 0
        self._atk = 0

        self.__recompensa = nivel

    #GETTERS
    @property
    def nome(self):
        return self._nome

    @property
    def hp(self):
        return self._hp

    @property
    def atk(self):
        return self._atk

    @property
    def recompensa(self):
        return self.__recompensa

    #SETTERS
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @hp.setter
    def hp(self, valor):
        self._hp = valor

    @atk.setter
    def atk(self, valor):
        self._atk = valor

    @recompensa.setter
    def recompensa(self, valor):
        self.__recompensa = valor

#ZUMBI
class Zumbi(Humanoide):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.nome = 'Zumbi'

        self.hp = 20 * nivel
        self.atk = 1 * nivel

        self.recompensa *= 7


class ZumbiManiaco(Humanoide):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.nome = 'Zumbi Maníaco'

        self.hp = 40 * nivel
        self.atk = 2 * nivel

        self.recompensa *= 15


class ZumbiAterrorizante(Humanoide):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.nome = 'Zumbi Aterrorizante'
        self.hp = 60 * nivel
        self.atk = 5 * nivel

        self.recompensa *= 30


#VAMPIRO
class Vampiro(Humanoide):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.hp = 7 * nivel
        self.atk = 7 * nivel

        self.recompensa *= 10


class VampiroMestre(Humanoide):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.nome = 'Vampiro Mestre'

        self.hp = 14 * nivel
        self.atk = 14 * nivel

        self.recompensa *= 20


class VampiroAncestral(Humanoide):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.nome = 'Vampiro Ancestral'

        self.hp = 21 * nivel
        self.atk = 21 * nivel

        self.recompensa *= 30


#LOBISOMEM
class Lobisomem(Humanoide):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.nome = 'Lobisomem'

        self.hp = 4 * nivel
        self.atk = 10 * nivel

        self.recompensa *= 20


class LobisomemFeroz(Humanoide):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.nome = 'Lobisomem Feroz'

        self.hp = 8 * nivel
        self.atk = 20 * nivel

        self.recompensa *= 40


class LobisomemBestial(Humanoide):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.nome = 'Lobisomem Bestial'

        self.hp = 12 * nivel
        self.atk = 30 * nivel

        self.recompensa *= 60



