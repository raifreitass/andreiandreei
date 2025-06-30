from itertools import combinations

# Função principal que aplica o algoritmo de minimização Myhill-Nerode


def minimizar_afd(afd):
    estados = afd['estados']
    finais = set(afd['finais'])
    trans = afd['transicoes']
    alfabeto = afd['alfabeto']

    # Etapa 1: criar pares de estados e marcar os distintamente finais
    tabela = {}
    pares = list(combinations(estados, 2))

    for (p, q) in pares:
        tabela[(p, q)] = (p in finais) != (q in finais)

    # Etapa 2: propaga distinções com base nas transições
    alterado = True
    while alterado:
        alterado = False
        for (p, q) in pares:
            if tabela[(p, q)]:
                continue
            for simbolo in alfabeto:
                p1 = afd['transicoes'].get((p, simbolo))
                q1 = afd['transicoes'].get((q, simbolo))
                if not p1 or not q1:
                    continue
                par = tuple(sorted((p1, q1)))
                if p1 != q1 and tabela.get(par, False):
                    tabela[(p, q)] = True
                    alterado = True
                    break

    # Etapa 3: agrupar estados não distinguidos (equivalentes)
    grupos = []
    for estado in estados:
        encontrado = False
        for grupo in grupos:
            if all(not tabela.get(tuple(sorted((estado, outro))), False) for outro in grupo):
                grupo.append(estado)
                encontrado = True
                break
        if not encontrado:
            grupos.append([estado])

    # Etapa 4: construir novo AFD com os grupos formados
    novo_estado = {}
    for grupo in grupos:
        nome = "_".join(sorted(grupo))
        for estado in grupo:
            novo_estado[estado] = nome

    novo_afd = {
        'alfabeto': alfabeto,
        'estados': list(set(novo_estado.values())),
        'inicial': novo_estado[afd['inicial']],
        'finais': list(set(novo_estado[e] for e in finais)),
        'transicoes': {}
    }

    for (origem, simbolo), destino in trans.items():
        novo_o = novo_estado[origem]
        novo_d = novo_estado[destino]
        novo_afd['transicoes'][(novo_o, simbolo)] = novo_d

    return novo_afd, grupos
