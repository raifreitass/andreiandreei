def validar_afd(afd):
    erros = []
    if afd['inicial'] not in afd['estados']:
        erros.append(f"Estado inicial inválido: {afd['inicial']}")

    for estado_final in afd['finais']:
        if estado_final not in afd['estados']:
            erros.append(f"Estado final inválido: {estado_final}")

    for (estado, simbolo), destino in afd['transicoes'].items():
        if estado not in afd['estados']:
            erros.append(f"Estado de origem inválido na transição: {estado}")
        if destino not in afd['estados']:
            erros.append(f"Estado de destino inválido na transição: {destino}")
        if simbolo not in afd['alfabeto']:
            erros.append(f"Símbolo inválido na transição: {simbolo}")

    return erros


