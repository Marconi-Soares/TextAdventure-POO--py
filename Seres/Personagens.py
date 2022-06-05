class Jogador:
    def __init__(self, nome, nivel=1):
        '''
        Uma pessoa, uai...
        :param nome: nome kkk
        '''
        self.__classe = self.__class__.__name__

        self._nivel = nivel

        self._xp = 0
        self._rating = (5 * (self.nivel - 1) * self.nivel) + (self.nivel * (1 + 30 / 100) * 10)

        self._nome = nome

        self._hp = None
        self._maxHP = self.nivel
        self._baseHP = None

        self._atk = None
        self._baseATK = None

        self._defesa = 0

        self._inv = {}
        self._usavel = {}
        self._equip = {}

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

    @property
    def defesa(self):
        return self._defesa

    @property
    def usavel(self):
        return self._usavel


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

    @defesa.setter
    def defesa(self, valor):
        self.defesa = valor

    @usavel.setter
    def usavel(self, valor):
        self._usavel = valor


    #METODOS

    #GERAIS
    def status(self):
        print(f'+{"-" * 39}+\n'
              f'| Nome: {self.nome:>31} |\n'
              f'| Classe: {self.classe:>29} |\n'
              f'|{"-" * 39}|\n'
              f'| Nivel: {self.nivel:>30} |\n'
              f'| Prox Nível: {f"[{self.xp:.0f} / {self.rating:.0f}]":>25} |\n'
              f'| Saúde: {f"[{self.hp:.0f} / {self.maxHP:.0f}]":>30} |\n'
              f'| Ataque: {self.atk:>29} |\n'
              f'+{"-" * 39}+\n')

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
            self.rating = (5 * (self.nivel - 1) * self.nivel)  + (self.nivel * (1 + 30 / 100) * 10)

    #ITENS
    def inventario(self):
        print(f'{"INVENTÁRIO":^50}')
        for item in self.inv.keys():
            print(f'+{"-" * 50}+\n'
                  f'|{" " * 5}{item:<45}|')
        print(f'+{"-" * 50}+')

    def pegar(self, item):
        if not item.nome in self.inv.keys():
            self.inv.update({item.nome: item})
        else:
            print('Você não já tem este item...')

    def destruir(self, item):
        if item in self.inv.keys():
            while True:
                opcao = input(f'Digite SiM para destruir {item.nome} PERMANENTEMENTE\nou N para não destruí-lo.: ')
                if opcao == 'SiM':
                    del self.inv[item]

                    print(item, ' destruido para sempre.')
                    break

                elif opcao == 'N':
                    print(item.nome, 'não foi destruido.')
                    break

                else:
                    print(opcao, 'não é uma escolha válida.')
        else:
            print('Parece que você não tem esse item.\n(DIGITE EXATAMENTE O NOME DO ITEM QUE DESEJA LARGAR)')

    def equipar(self, item):
        #Se o item está no inventário
        if item in self.inv.keys():
            item = self.inv[item]

            #Se a classe pode utilizar o item.
            if item.tipo in self.usavel.keys():

                #Se não estiver usando um item do tipo.
                if not self.usavel[item.tipo]:
                    self.usavel[item.tipo] = True
                    print('Equipando', item.nome)
                    self.ativarItem(item)


                else:
                    print('Você já está usando', item.tipo)

            else:
                print('Esta classe não pode utilizar este item.')

        else:
            print('Você não possui este item. (VERIFIQUE O NOME DIGITADO)')

    def retirar(self, item):
        if self.usavel[item]:
            print(item, 'retirado com sucesso.')
            self.usavel[item] = False

        else:
            print('Não há', item, 'para retirar')

    def ativarItem(self, item):
        if item.tipo_de_efeito == '+ HP':
            self.maxHP += item.efeito

        if item.tipo_de_efeito == '+ ATK':
            self.atk += item.efeito

        if item.tipo_de_efeito == '+ DFS':
            self.defesa += self.defesa


class Guerreiro(Jogador):
    def __init__(self, nome, nivel=1):
        super().__init__(nome, nivel)
        self.setUtilizaveis()

        #HP
        self.baseHP = 10
        self.hp = 50 + (self.baseHP * self.nivel)
        self.maxHP = self.hp

        #ATK
        self.baseATK = 2
        self.atk = 0 + (self.baseATK * self.nivel)


    #METODOS
    def setUtilizaveis(self):
        self.usavel.update({'Helmo': False})
        self.usavel.update({'Peitoral': False})
        self.usavel.update({'Braceletes': False})
        self.usavel.update({'Calças': False})
        self.usavel.update({'Caneleiras': False})
        self.usavel.update({'Botas': False})
        self.usavel.update({'Espada': False})
        self.usavel.update({'Escudo': False})


    #ATAQUES
    def ataque_basico(self, alvo):
        alvo.hp -= self.atk
        if alvo.hp <= 0:
            print(f'{alvo.nome} foi derrotado(a).')





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
        self.baseHP = 4
        self.hp = 45 + (self.baseHP * self.nivel)
        self.maxHP = self.hp

        #ATK
        self.baseATK = 8
        self.atk = 5 + (self.baseATK * self.nivel)
