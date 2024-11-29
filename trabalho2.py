carga_acidental = {
    'depósitos de livros': 4,
    'edificios residenciais:dormitórios ,salas,copa,cozinha e banheiro': 1.5,
    'edificios residenciais:despensa,área de serviço e lavanderia': 2,
    'forros': 0.5,
    'escadas e lajes de garagem': 3
}

carga_permanente = {
    'concreto armado': 25,
    'concreto simples': 24,
    'alvenaria de tijolos de barro maciço': 18,
    'alvenaria de tijolos furados': 13,
    'alvenaria de blocos de concreto': 14,
    'argamassa de cimento e areia': 21
}

def volume_laje(laje):
    """list --> float"""
    vollaje = 1
    for dim in laje:
        vollaje *= dim
    return vollaje

def volume_revestimento(revestimento):
    """list --> float"""
    vollrevest = 1
    for dim in revestimento:
        vollrevest *= dim
    return vollrevest

def volume_viga(viga):
    """list --> float"""
    volvig = 1
    for dim in viga:
        volvig *= dim
    return volvig

def volume_pilar(pilar):
    """list --> float"""
    volpil = 1
    for dim in pilar:
        volpil *= dim
    return volpil

def peso_pilar(pilar, piso_pilar):
    """list, string --> float"""
    return volume_pilar(pilar) * carga_permanente[piso_pilar]

def peso_viga(viga, piso_viga):
    """list, string --> float"""
    return volume_viga(viga) * carga_permanente[piso_viga]

def peso_laje(laje, piso_laje):
    """list, string --> float"""
    return volume_laje(laje) * carga_permanente[piso_laje]

def peso_revestimento(revestimento, piso_revestimento):
    """list, string --> float"""
    return volume_revestimento(revestimento) * carga_permanente[piso_revestimento]

def peso_acidental_laje(laje, acidental_laje):
    """list, string --> float"""
    return laje[0] * laje[1] * carga_acidental[acidental_laje]

def carga_vigas(laje, acidental_laje, revestimento, piso_revestimento, piso_laje):
    """list, string, list, string, string --> float"""
    return (
        peso_acidental_laje(laje, acidental_laje)
        + peso_revestimento(revestimento, piso_revestimento)
        + peso_laje(laje, piso_laje)
    ) / 4

def carga_pilares(laje, acidental_laje, revestimento, piso_revestimento, piso_laje, viga, piso_viga):
    """list, string, list, string, string, list, string --> float"""
    return carga_vigas(laje, acidental_laje, revestimento, piso_revestimento, piso_laje) + peso_viga(viga, piso_viga)

def carga_cada_fundação(laje, acidental_laje, revestimento, piso_revestimento, piso_laje, viga, piso_viga, pilar, piso_pilar):
    """list, string, list, string, string, list, string, list, string --> float"""
    return carga_pilares(laje, acidental_laje, revestimento, piso_revestimento, piso_laje, viga, piso_viga) + peso_pilar(pilar, piso_pilar)


def pede_dimensao():
    valores=str.split(input('digite separado por espaço: '))
    v_float=[]
    for v in valores:
        v_float.append(float(v))
    return v_float

def calcular_volume(elemento):
    '''recebe uma lista com as dimensões do objeto do tipo float e calcula o volume do objeto
list(float)->float'''
    volume = 1
    for dim in elemento:
        volume *= dim
    return volume

def main():
    print('Dimensão da laje')
    laje=pede_dimensao()
    volume_laje=calcular_volume(laje)
    print(volume_laje)
    #pode fazer isso para os outros volumes

def pratos(pressao,grauAPI):
    prato=0
    while prato<6:
        if pressao<0 and grauAPI==44:
            pressao-=100
            prato+=1
        if 0<pressao<500 and grauAPI==39:
            pressao-=100
            prato+=1
        return prato

print(pratos(100,39))
