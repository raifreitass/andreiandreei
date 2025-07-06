# Função para ler um arquivo de definição de AFD e retornar um dicionário com os dados
def ler_afd(caminho_arquivo):
    afd = {
        'alfabeto': [],
        'estados': [],
        'inicial': '',
        'finais': [],
        'transicoes': {}
    }

    # Lê todas as linhas não vazias
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = [linha.strip() for linha in arquivo if linha.strip()]

    i = 0
    while i < len(linhas):
        linha = linhas[i]
        if linha.startswith('alfabeto:'):
            afd['alfabeto'] = linha.split(':')[1].split(',')
        elif linha.startswith('estados:'):
            afd['estados'] = linha.split(':')[1].split(',')
        elif linha.startswith('inicial:'):
            afd['inicial'] = linha.split(':')[1]
        elif linha.startswith('finais:'):
            afd['finais'] = linha.split(':')[1].split(',')
        elif linha == 'transicoes':
            i += 1
            while i < len(linhas):
                origem, destino, simbolo = linhas[i].split(',')
                afd['transicoes'][(origem, simbolo)] = destino
                i += 1
            break
        i += 1

    return afd
