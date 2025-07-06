from leitor_afd import ler_afd
from validacao import validar_afd
from minimizador import minimizar_afd
from grafo_visual import desenhar_afd

afd = ler_afd('afd.txt')

print("Alfabeto:", afd['alfabeto'])
print("Estados:", afd['estados'])
print("Inicial:", afd['inicial'])
print("Finais:", afd['finais'])
print("Transições:")
for (estado, simbolo), destino in afd['transicoes'].items():
    print(f"{estado} -- {simbolo} --> {destino}")

erros = validar_afd(afd)
if erros:
    print("\nErros encontrados no AFD:")
    for erro in erros:
        print(" -", erro)
    exit(1)  # Encerra o programa se houver erro

print("\nIniciando minimização do AFD...\n")
afd_minimizado, grupos = minimizar_afd(afd)

print("\nGrupos de estados equivalentes:")
for grupo in grupos:
    print("  -", ", ".join(grupo))

print("\nAFD Minimizado:")
print("Estados:", ", ".join(afd_minimizado['estados']))
print("Inicial:", afd_minimizado['inicial'])
print("Finais:", ", ".join(afd_minimizado['finais']))
print("\nTransições:")
for (estado, simbolo), destino in afd_minimizado['transicoes'].items():
    print(f"  {estado} -- {simbolo} --> {destino}")


desenhar_afd(afd_minimizado)
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
