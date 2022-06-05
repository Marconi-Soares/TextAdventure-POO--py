import pytest

from Seres import Animais
#lobo
#hp
def test_hp_lobo_nivel_0():
    lobo = Animais.Lobo(0)
    return

def test_hp_lobo_nivel_30():
    lobo = Animais.Lobo(30)
    assert lobo.hp == 90

#ataque
def test_atk_lobo_nivel_0():
    lobo = Animais.Lobo(0)
    return

def test_atk_lobo_nivel_30():
    lobo = Animais.Lobo(30)
    assert lobo.atk == 60

#recompensa
def test_recompensa_lobo_nivel_0():
    lobo = Animais.Lobo(0)
    return

def test_recompensa_lobo_nivel_30():
    lobo = Animais.Lobo(30)
    assert lobo.recompensa == 60


#lobo alfa
#hp
def test_hp_loboAlfa_nivel_0():
    loboAlfa = Animais.LoboAlfa(0)
    return

def test_hp_loboAlfa_nivel_30():
    lobo = Animais.LoboAlfa(30)
    assert lobo.hp == 180

#atk
def test_atk_loboAlfa_nivel_0():
    lobo = Animais.LoboAlfa(0)
    return

def test_atk_loboAlfa_nivel_30():
    lobo = Animais.LoboAlfa(30)
    assert lobo.atk == 120

#recompensa
def test_recompensa_loboAlfa_nivel_0():
    pass

def test_recompensa_loboAlfa_nivel_30():
    lobo = Animais.LoboAlfa(30)
    assert lobo.recompensa == 120


#aranha
#hp
def test_hp_aranha_nivel_0():
    pass

def test_hp_aranha_nivel_30():
    aranha = Animais.Aranha(30)
    assert aranha.hp == 60

#ataque
def test_atk_aranha_nivel_0():
    pass

def test_atk_aranha_nivel_30():
    aranha = Animais.Aranha(30)
    assert aranha.atk == 90

#recompensa
def test_recompensa_aranha_nivel_0():
    pass

def test_recompensa_aranha_nivel_30():
    aranha = Animais.Aranha(30)
    assert aranha.recompensa == 30

#aranha alfa
#hp
def test_hp_aranhaAlfa_nivel_0():
    pass

def test_hp_aranhaAlfa_nivel_30():
    aranha = Animais.AranhaAlfa(30)
    assert aranha.hp == 120

#ataque
def test_atk_aranhaAlfa_nivel_0():
    pass

def test_atk_aranhaAlfa_nivel_30():
    aranha = Animais.AranhaAlfa(30)
    assert aranha.atk == 180

#recompensa
def test_recompensa_aranhaAlfa_nivel_0():
    pass

def test_recompensa_aranhaAlfa_nivel_30():
    aranha = Animais.AranhaAlfa(30)
    assert aranha.recompensa == 60




