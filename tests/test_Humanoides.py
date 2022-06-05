from Seres import Humanoides

#Zumbi
#hp
def test_hp_zumbi_nivel_0():
    zumbi = Humanoides.Zumbi(0)
    pass

def test_hp_zumbi_nivel_30():
    zumbi = Humanoides.Zumbi(30)
    assert zumbi.hp == 600

#ataque
def test_atk_zumbi_nivel_30():
    zumbi = Humanoides.Zumbi(30)
    assert zumbi.atk == 30

#recompensa
def test_recompensa_zumbi_nivel_30():
    zumbi = Humanoides.Zumbi(30)
    assert zumbi.recompensa == 210


#ZumbiManiaco
#hp
def test_hp_zumbiManiaco_nivel_30():
    zumbi = Humanoides.ZumbiManiaco(30)
    assert zumbi.hp == 1200

#ataque
def test_atk_zumbiManiaco_nivel_30():
    zumbi = Humanoides.ZumbiManiaco(30)
    assert zumbi.atk == 60

#recompensa
def test_recompensa_zumbiManiaco_nivel_30():
    zumbi = Humanoides.ZumbiManiaco(30)
    assert zumbi.recompensa == 450


#ZumbiAterrorizante
#hp
def test_hp_zumbiAterrorizante_nivel_30():
    zumbi = Humanoides.ZumbiAterrorizante(30)
    assert zumbi.hp == 1800

#ataque
def test_atk_zumbiAterrorizante_nivel_30():
    zumbi = Humanoides.ZumbiAterrorizante(30)
    assert zumbi.atk == 150

#recompensa
def test_recompensa_zumbiAterrorizante_nivel_30():
    zumbi = Humanoides.ZumbiAterrorizante(30)
    assert zumbi.recompensa == 900


#Vampiro
#hp
def test_hp_Vampiro_nivel_30():
    vampiro = Humanoides.Vampiro(30)
    assert vampiro.hp == 210

#ataque
def test_atk_Vampiro_nivel_30():
    vampiro = Humanoides.Vampiro(30)
    assert vampiro.atk == 210

#recompensa
def test_recompensa_Vampiro_nivel_30():
    vampiro = Humanoides.Vampiro(30)
    assert vampiro.recompensa == 300


#VampiroMestre
#hp
def test_hp_VampiroMestre_nivel_30():
   vampiro = Humanoides.VampiroMestre(30)
   assert vampiro.hp == 420

#ataque
def test_atk_VampiroMestre_nivel_30():
    vampiro = Humanoides.VampiroMestre(30)
    assert vampiro.hp == 420

#recompensa
def test_recompensa_VampiroMestre_nivel_30():
    vampiro = Humanoides.VampiroMestre(30)
    assert vampiro.recompensa == 600


#VampiroAncestral
#hp
def test_hp_VampiroAncestral_nivel_30():
    vampiro = Humanoides.VampiroAncestral(30)
    assert vampiro.hp == 630

#ataque
def test_atk_VampiroAncestral_nivel_30():
    vampiro = Humanoides.VampiroAncestral(30)
    assert vampiro.atk == 630

#recompensa
def test_recompensa_VampiroAncestral_nivel_30():
    vampiro = Humanoides.VampiroAncestral(30)
    assert vampiro.recompensa == 900


#Lobisomen
#hp
def test_hp_Lobisomen_nivel_30():
    lobisomen = Humanoides.Lobisomem(30)
    assert lobisomen.hp == 120

#ataque
def test_atk_Lobisomen_nivel_30():
    lobisomen = Humanoides.Lobisomem(30)
    assert lobisomen.atk == 300

#recompensa
def test_recompensa_Lobisomen_nivel_30():
    lobisomen = Humanoides.Lobisomem(30)
    assert lobisomen.recompensa == 600


#LobisomenFeroz
#hp
def test_hp_LobisomenFeroz_nivel_30():
    lobisomen = Humanoides.LobisomemFeroz(30)
    assert lobisomen.hp == 240

#ataque
def test_atk_LobisomenFeroz_nivel_30():
    lobisomen = Humanoides.LobisomemFeroz(30)
    assert lobisomen.atk == 600

#recompensa
def test_recompensa_LobisomenFeroz_nivel_30():
    lobisomen = Humanoides.LobisomemFeroz(30)
    assert lobisomen.recompensa == 1200


#LobisomenBestial
#hp
def test_hp_LobisomenBestial_nivel_30():
    lobisomen = Humanoides.LobisomemBestial
    assert lobisomen.hp == 360

#ataque
def test_atk_LobisomenBestial_nivel_30():
    lobisomen = Humanoides.LobisomemBestial(30)
    assert lobisomen.atk == 900

#recompensa
def test_ataque_LobisomenBestial_nivel_30():
    lobisomen = Humanoides.LobisomemBestial(30)
    assert lobisomen.recompensa == 1800
