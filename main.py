from parser import ler_afd
from validacao import validar_afd
from minimizador import minimizar_afd
from visualizacao import desenhar_afd

# Lê o AFD a partir do arquivo de entrada
afd = ler_afd('afd.txt')

# Imprime o conteúdo do AFD original
print("Alfabeto:", afd['alfabeto'])
print("Estados:", afd['estados'])
print("Inicial:", afd['inicial'])
print("Finais:", afd['finais'])
print("Transições:")
for (estado, simbolo), destino in afd['transicoes'].items():
    print(f"{estado} -- {simbolo} --> {destino}")

# Valida o AFD antes de aplicar o algoritmo
erros = validar_afd(afd)
if erros:
    print("\nErros encontrados no AFD:")
    for erro in erros:
        print(" -", erro)
    exit(1)  # Encerra o programa se houver erro

# Aplica o algoritmo de minimização
print("\nIniciando minimização do AFD...\n")
afd_minimizado, grupos = minimizar_afd(afd)

# Mostra os grupos de estados equivalentes
print("Grupos de estados equivalentes:")
for grupo in grupos:
    print(" -", grupo)

# Imprime o novo AFD minimizado
print("\nAFD Minimizado:")
print("Estados:", afd_minimizado['estados'])
print("Inicial:", afd_minimizado['inicial'])
print("Finais:", afd_minimizado['finais'])
print("Transições:")
for (estado, simbolo), destino in afd_minimizado['transicoes'].items():
    print(f"{estado} -- {simbolo} --> {destino}")

# Gera o diagrama visual
desenhar_afd(afd_minimizado)

# Salva o novo AFD em um arquivo txt


def salvar_afd_em_txt(afd, caminho_arquivo):
    with open(caminho_arquivo, 'w') as f:
        f.write("alfabeto:" + ",".join(afd['alfabeto']) + "\n")
        f.write("estados:" + ",".join(afd['estados']) + "\n")
        f.write("inicial:" + afd['inicial'] + "\n")
        f.write("finais:" + ",".join(afd['finais']) + "\n")
        f.write("transicoes\n")
        for (origem, simbolo), destino in afd['transicoes'].items():
            f.write(f"{origem},{destino},{simbolo}\n")


salvar_afd_em_txt(afd_minimizado, "afd_minimizado.txt")
print("Arquivo afd_minimizado.txt gerado!")
