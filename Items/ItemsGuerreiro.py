class MateriaPrima:
    """
    Regra geral das armaduras:
    helmo protege = 2x
    bota protege = 2x

    calça protege = 3x
    peitoral protege = 5x
    """
    def __init__(self, material, nivel=1):
        self._nivel = nivel
        self._nome = None
        self._tipo = None
        self._tipo_de_efeito = None
        self._invstatus = ''
        self._material = material

        if material == 'Trapos':
            self._indice = 1
        elif material == 'Aço':
            self._indice = 3
        elif material == 'Aço Reforçado':
            self._indice = 5

        self._efeito = self.nivel * self.indice

    @property
    def indice(self):
        return self._indice

    @property
    def nome(self):
        return self._nome

    @property
    def invstatus(self):
        return self._invstatus

    @property
    def material(self):
        return self._material

    @property
    def tipo(self):
        return self._tipo

    @property
    def tipo_de_efeito(self):
        return self._tipo_de_efeito

    @property
    def efeito(self):
        return self._efeito

    @property
    def nivel(self):
        return self._nivel


    #Setter
    @nivel.setter
    def nivel(self, valor):
        self._nivel = valor

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @material.setter
    def material(self, valor):
        self._material = valor

    @efeito.setter
    def efeito(self, valor):
        self._efeito = valor

    @indice.setter
    def indice(self, valor):
        self._indice = valor

    @tipo.setter
    def tipo(self, valor):
        self._tipo = valor

    @tipo_de_efeito.setter
    def tipo_de_efeito(self, valor):
        self._tipo_de_efeito = valor

    @invstatus.setter
    def invstatus(self, valor):
        self._invstatus = valor



class Helmo(MateriaPrima):
    def __init__(self, material, nivel):
        super().__init__(material, nivel)
        self.tipo = 'Helmo'
        self.tipo_de_efeito = '+ HP'
        self.nome = 'Helmo de ' + material + ' Nível: ' + str(self.nivel)
        self.efeito *= 2


class Peitoral(MateriaPrima):
    def __init__(self, material, nivel):
        super().__init__(material, nivel)
        self.tipo = 'Peitoral'
        self.tipo_de_efeito = '+ HP'
        self.nome = 'Peitoral de ' + material + ' Nível: ' + str(self.nivel)
        self.efeito *= 5


class Braceletes(MateriaPrima):
    def __init__(self, material, nivel):
        super().__init__(material, nivel)
        self.tipo = 'Braceletes'
        self.tipo_de_efeito = '+ HP'
        self.nome = 'Braceletes de ' + material + ' Nível: ' + str(self.nivel)
        self.efeito *= 1


class Calcas(MateriaPrima):
    def __init__(self, material, nivel):
        super().__init__(material, nivel)
        self.tipo = 'Calças'
        self.tipo_de_efeito = '+ HP'
        self.nome = 'Calças de ' + material + ' Nível: ' + str(self.nivel)
        self.efeito *= 3


class Caneleiras(MateriaPrima):
    def __init__(self, material, nivel):
        super().__init__(material, nivel)
        self.tipo = 'Caneleiras'
        self.tipo_de_efeito = '+ HP'
        self.nome = 'Caneleiras de ' + material + ' Nível: ' + str(self.nivel)
        self.efeito *= 1


class Botas(MateriaPrima):
    def __init__(self, material, nivel):
        super().__init__(material, nivel)
        self.tipo = 'Botas'
        self.tipo_de_efeito = '+ HP'
        self.nome = 'Botas de ' + material + ' Nível: ' + str(self.nivel)
        self.efeito *= 2


class Espada(MateriaPrima):
    def __init__(self, material, nivel=1):
        super().__init__(material, nivel)
        self.tipo = 'Espada'
        self.tipo_de_efeito = '+ ATK'
        self.nivel = nivel
        self.nome = 'Espada de ' + material + ' Nível: ' + str(self.nivel)
        self.efeito *= 1


class Escudo(MateriaPrima):
    def __init__(self, material, nivel=1):
        super().__init__(material, nivel)
        self.tipo = 'Escudo'
        self.tipo_de_efeito = '+ DFS'
        self.nivel = nivel
        self.nome = 'Espada de ' + material + ' Nível: ' + str(self.nivel)
        self.efeito *= 3