import numpy as np
from tabulate import tabulate
from colorama import Fore, Style, init

# Inicializa o Colorama para Windows (se necessário)
init(autoreset=True)

def print_colored_table(table, pivot_row=None, pivot_col=None):
    # Função para imprimir o tableau com cores aplicadas ao pivot_row e pivot_col
    table_str = ""
    for i, row in enumerate(table):
        for j, elem in enumerate(row):
            if i == pivot_row and j == pivot_col:
                table_str += f"{Fore.RED}{elem:.2f}{Style.RESET_ALL}\t"
            elif i == pivot_row or j == pivot_col:
                table_str += f"{Fore.YELLOW}{elem:.2f}{Style.RESET_ALL}\t"
            else:
                table_str += f"{elem:.2f}\t"
        table_str += "\n"
    print(table_str)

def simplex(c, A, b):
    # Número de variáveis de decisão e restrições
    num_vars = len(c)
    num_constraints = len(b)

    # Monta o tableau inicial
    tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))

    # Configura a matriz das restrições (A) e dos termos independentes (b) no tableau
    tableau[:-1, :num_vars] = A
    tableau[:-1, num_vars:num_vars + num_constraints] = np.eye(num_constraints)
    tableau[:-1, -1] = b

    # Configura a função objetivo no tableau
    tableau[-1, :num_vars] = -np.array(c)  # Função objetivo negada para maximização

    print("Tabela inicial:")
    print_colored_table(tableau)

    # Executa o algoritmo Simplex
    step = 1
    while True:
        # Passo 1: Identificar a coluna de entrada (a variável que entra na base)
        pivot_col = np.argmin(tableau[-1, :-1])
        if tableau[-1, pivot_col] >= 0:
            # Se todos os coeficientes da linha da função objetivo são >= 0, encontramos a solução ótima
            break

        # Passo 2: Identificar a linha de saída (a variável que sai da base)
        with np.errstate(divide='ignore', invalid='ignore'):
            ratios = np.where(tableau[:-1, pivot_col] > 0, tableau[:-1, -1] / tableau[:-1, pivot_col], np.inf)
        pivot_row = np.argmin(ratios)

        # Se não existe um valor positivo, a solução é ilimitada
        if np.isinf(ratios[pivot_row]):
            print("A solução é ilimitada.")
            return None

        # Pivotamento
        pivot_element = tableau[pivot_row, pivot_col]
        print(f"\nEtapa {step}: Pivotamento")
        print(f"Elemento pivot: {pivot_element} (Linha {pivot_row}, Coluna {pivot_col})")

        # Normaliza a linha do pivot
        tableau[pivot_row] /= pivot_element
        print("Tabela após normalizar linha do pivot:")
        print_colored_table(tableau, pivot_row, pivot_col)

        # Atualiza as outras linhas para zerar a coluna do pivot
        for i in range(len(tableau)):
            if i != pivot_row:
                factor = tableau[i, pivot_col]
                original_row = tableau[i].copy()  # Salva a linha original para cálculo detalhado
                tableau[i] -= factor * tableau[pivot_row]
                print(f"\nAtualizando linha {i} usando fator {factor}")
                print(f"Cálculo: {original_row} - ({factor}) * {tableau[pivot_row]}")
                print_colored_table(tableau, pivot_row, pivot_col)

        step += 1  # Incrementa o contador de etapas

        print(f"\nTabela após a Etapa {step - 1}:")
        print_colored_table(tableau)

    # Resultado: obter as variáveis básicas
    solution = np.zeros(num_vars)
    for i in range(num_vars):
        # Se a coluna correspondente é canônica, adiciona o valor à solução
        col = tableau[:-1, i]
        if np.count_nonzero(col) == 1 and np.any(col == 1):
            solution[i] = tableau[np.where(col == 1)[0][0], -1]

    # Lucro máximo (último elemento da última linha)
    max_profit = tableau[-1, -1]

    print("\nSolução ótima encontrada:")
    print("Valores das variáveis:", solution)
    print("Lucro total máximo =", max_profit)

    return solution, max_profit

# Dados do problema
c = [0.35, 0.12]  # Lucro por quilo de carne de boi e grão, respectivamente
A = [
    [1, 1],          # Restrição de peso total
    [0.2, 0.4],      # Restrição de volume total
    [1, 0],          # Disponibilidade máxima de carne de boi
    [0, 1]           # Disponibilidade máxima de grão
]
b = [160000, 70000, 85000, 100000]  # Restrições de capacidade e disponibilidade

# Executa o método Simplex
solution, max_profit = simplex(c, A, b)
