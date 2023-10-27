def validar_numero_inteiro_maior_que_zero(numero):
    try:
        numero = int(numero)
        if numero > 0:
            return numero
        else:
            return None
    except ValueError:
        return None