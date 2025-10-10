def media(lista_notas):
    """
    Recebe uma lista de notas e retorna a média.
    """
    if not lista_notas:
        return 0
    return sum(lista_notas) / len(lista_notas)

def maior(lista_notas):
    """
    Retorna a maior nota da lista.
    """
    if not lista_notas:
        return None
    return max(lista_notas)

def menor(lista_notas):
    """
    Retorna a menor nota da lista.
    """
    if not lista_notas:
        return None
    return min(lista_notas)