from colorama import Fore, init
init(autoreset=True)

def menu():
    print(Fore.CYAN + "\n=== SISTEMA MATRIZES ===")
    opcoes = ["Criar Matriz A", "Criar Matriz B", "Somar (A+B)", "Subtrair (A-B)", "Multiplicar (A×B)", "Mostrar", "Sair"]
    for i, op in enumerate(opcoes, 1): print(Fore.YELLOW + f"{i}. {op}")
    return input(Fore.WHITE + "Opção: ")

def criar_matriz(nome):
    try:
        l, c = int(input("Linhas: ")), int(input("Colunas: "))
        print(f"Elementos {l}x{c}:")
        return [[float(input(f"[{i}][{j}]: ")) for j in range(c)] for i in range(l)]
    except:
        print(Fore.RED + "Erro! Digite números.")
        return None

def mostrar_matriz(m, nome):
    if not m: print(Fore.RED + f"{nome} vazia!"); return
    print(Fore.YELLOW + f"\n{nome}:")
    for linha in m: print(" ".join(f"{x:6.1f}" for x in linha))

def operar(m1, m2, op):
    if not m1 or not m2: print(Fore.RED + "Crie as matrizes!"); return None
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]): print(Fore.RED + "Dimensões diferentes!"); return None
    ops = {'+': lambda a,b: a+b, '-': lambda a,b: a-b}
    return [[ops[op](m1[i][j], m2[i][j]) for j in range(len(m1[0]))] for i in range(len(m1))]

def multiplicar(m1, m2):
    if not m1 or not m2: print(Fore.RED + "Crie as matrizes!"); return None
    if len(m1[0]) != len(m2): print(Fore.RED + "Dimensões incompatíveis!"); return None
    return [[sum(m1[i][k] * m2[k][j] for k in range(len(m2))) for j in range(len(m2[0]))] for i in range(len(m1))]

# Programa principal
A, B = [], []
while True:
    op = menu()
    if op == '1': A = criar_matriz("Matriz A")
    elif op == '2': B = criar_matriz("Matriz B")
    elif op == '3': mostrar_matriz(operar(A, B, '+'), "A+B")
    elif op == '4': mostrar_matriz(operar(A, B, '-'), "A-B")
    elif op == '5': mostrar_matriz(multiplicar(A, B), "A×B")
    elif op == '6': mostrar_matriz(A, "A"); mostrar_matriz(B, "B")
    elif op == '7': print(Fore.CYAN + "Saindo!"); break
    else: print(Fore.RED + "Opção inválida!")