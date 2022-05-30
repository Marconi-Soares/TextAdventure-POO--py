from Seres import Personagens as P
from Seres import Humanoides as H
from Seres import Animais as Ani

from Items import ItemsGuerreiro as ItemGuerr

i = 3

guerreiro = P.Guerreiro('Marconi', i)
guerreiro.status()


helmo = ItemGuerr.Helmo('Trapos', i)
peitoral = ItemGuerr.Peitoral('Trapos', i)
braceletes = ItemGuerr.Braceletes('Trapos', i)
calcas = ItemGuerr.Calcas('Trapos', i)
caneleiras = ItemGuerr.Caneleiras('Trapos', i)
botas = ItemGuerr.Botas('Trapos', i)

guerreiro.pegar(helmo)
guerreiro.equipar('Helmo de Trapos Nível: 3')

guerreiro.pegar(peitoral)
guerreiro.equipar('Peitoral de Trapos Nível: 3')

guerreiro.retirar('Helmo')
guerreiro.retirar('Helmo')