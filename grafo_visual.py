from graphviz import Digraph

# Função que gera o diagrama do AFD minimizado em formato .png


def desenhar_afd(afd, nome_arquivo='afd_minimizado'):
    dot = Digraph(format='png')

    # Adiciona estados (finais com dupla borda)
    for estado in afd['estados']:
        if estado in afd['finais']:
            dot.node(estado, shape='doublecircle')
        else:
            dot.node(estado, shape='circle')

    # Adiciona seta para o estado inicial
    dot.node('', shape='none')
    dot.edge('', afd['inicial'])

    # Agrupa transições iguais para o mesmo destino
    transicoes_por_estado = {}
    for (estado, simbolo), destino in afd['transicoes'].items():
        chave = (estado, destino)
        if chave in transicoes_por_estado:
            transicoes_por_estado[chave].append(simbolo)
        else:
            transicoes_por_estado[chave] = [simbolo]

    for (origem, destino), simbolos in transicoes_por_estado.items():
        label = ",".join(simbolos)
        dot.edge(origem, destino, label=label)

    dot.render(nome_arquivo, cleanup=True)
    print(f"\nDiagrama gerado como {nome_arquivo}.png")
