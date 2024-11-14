
# Problema de Otimização de Carga para Navio

Este projeto resolve um problema de otimização de carga para um navio utilizando o **método SIMPLEX**. O objetivo é determinar a quantidade ideal de carga para maximizar o lucro dentro das restrições de capacidade do navio.

## Premissas

1. O compartimento de carga do navio possui:
   - **Capacidade máxima de peso**: 160.000 kg.
   - **Capacidade máxima de volume**: 70.000 m³.
2. O navio transportará dois tipos de cargas: carne de boi e grãos, com as seguintes características:
   
   - **Carne de boi**:
     - Peso total disponível: 85.000 kg
     - Volume por massa: 0,2 m³/kg
     - Lucro: R$ 0,35/kg
     
   - **Grãos**:
     - Peso total disponível: 100.000 kg
     - Volume por massa: 0,4 m³/kg
     - Lucro: R$ 0,12/kg
     
3. O dono do navio pode aceitar toda ou parte da carga disponível para maximizar o lucro, sem exceder as restrições de capacidade do navio.

## Definição da Função Objetivo

A função objetivo é maximizar o lucro \( Z \), dado pela soma dos lucros das cargas de carne e grãos:

\[
Z = 0,35x_1 + 0,12x_2
\]

Onde:
- \( x_1 \): quantidade de carne de boi a ser transportada (em kg).
- \( x_2 \): quantidade de grãos a ser transportada (em kg).

## Restrições

O problema possui as seguintes restrições baseadas nas capacidades do navio:

1. **Restrição de Peso**: A soma dos pesos das cargas deve ser menor ou igual à capacidade máxima de peso do navio:
   \[
   x_1 + x_2 \leq 160.000
   \]

2. **Restrição de Volume**: A soma dos volumes das cargas deve ser menor ou igual à capacidade máxima de volume do navio:
   \[
   0,2x_1 + 0,4x_2 \leq 70.000
   \]

3. **Não-negatividade**: A quantidade de cada carga transportada deve ser maior ou igual a zero:
   \[
   x_1 \geq 0 \quad 	ext{e} \quad x_2 \geq 0
   \]

## Solução Ótima Encontrada

Após a implementação do método SIMPLEX, foi encontrada a seguinte solução ótima:

- **Quantidade de carne de boi a transportar**: 85.000 kg
- **Quantidade de grãos a transportar**: 75.000 kg
- **Lucro máximo**: R$ 38.750,00

## Instruções para Execução

Para rodar este projeto, utilize o código Python providenciado para o método SIMPLEX, que pode ser executado em um ambiente Google Colab ou outro IDE compatível com Python.

## Código Python para Resolução com Método Simplex

O código Python para resolver este problema pode ser encontrado [aqui](#) (adicione o link para o código Python).

