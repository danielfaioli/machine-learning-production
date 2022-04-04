# Atividade ESBD 1.1

- [Atividade ESBD 1.1](#atividade-esbd-11)
- [Resposta à atividade ESBD 1.1](#resposta-à-atividade-esbd-11)
  - [1. Resultado dos Tests (tabela de performance)](#1-resultado-dos-tests-tabela-de-performance)
  - [2. Análises realizadas](#2-análises-realizadas)
  - [3. A função matemática que descreve a eficiência de cada função de busca.](#3-a-função-matemática-que-descreve-a-eficiência-de-cada-função-de-busca)
  - [Estrutura de dados implementadas nos Datasets](#estrutura-de-dados-implementadas-nos-datasets)


Título da Atividade: ESBD 1.1 - Funções de busca e análise de dimensionamento

Data de Abertura: 26/03/2021    Data de Entrega: 04/04/2021

Orientações:

O time deve ler com atenção o case da unidade 1, realizar os testes necessários para o preenchimento da tabela indicada e realizar as análises solicitadas.

Entrega: O arquivo deve conter um documento em PDF que inclua:

1. A tabela preenchida com os dados obtidos.
2. Um breve descritivo da análises realizadas.
3. A função matemática que descreve a eficiência de cada função de busca.
4. Uma estrutura de dados que pode estar implementada em cada função de busca


# Resposta à atividade ESBD 1.1

## 1. Resultado dos Tests (tabela de performance)

| Tam. do Conjunto | Tempo Func 1 (s) | Tempo Func 2 (s) | Tempo Func 3 (s) |
|------------------|------------------|------------------|------------------|
| 100              | 0.03880          | 0.02040          | 0.0054           |
| 1000             | 0.2940           | 0.03050          | 0.0050           |
| 10000            | 4.005            | 0.04300          | 0.0053           |
| 100000           | 61.9680          | 0.05740          | 0.0053           |
| 1000000          | 1908.5490        | 0.07860          | 0.0062           |

## 2. Análises realizadas

Escreveu-se uma classe de tests para realizar o *benchmarking* das funções. É notável a diferença de performance entre as funções, sendo a function_1 aquela de menor eficiência e a function_3 a de maior eficiência. A diferença de performance entre as funções se devem tanto às estruturas de dados (structure_1 é uma lista oredenada e structure_2 é um dicionário python, que é uma implementação de uma tabela hash), as formas de acesso de um item nestas e ao algoritmo de busca utilizado (caso da function_2).


## 3. A função matemática que descreve a eficiência de cada função de busca.

* function_1: 
    Seja `T` o tempo despendido para execução e `k` o número de elementos percorridos até uma busca:
    $$T(k)=constante*k$$
    O tempo de busca é proporcional ao número de elementos que devem ser percorridos até que se encontre o elemento buscado, ou seja, o tempo é proporcional à posição do elemento no array.
    Em notação big-O a complexidade da função function_1:
    $$O(n)$$
* function_2:
  A função dois implementa uma busca binária (binary search), a seguir a demostração da função que descreve o tempo de execução. 
  Seja `T` o tempo despendido para execução, `n` o número de elementos no array, `k` o número de iterações nescessárias para se encontrar o elemento buscado e `len` uma função que representa o tamanho do array em uma dada iteração:
  $$it_1: len(array) = n$$
  $$it_2: len(array) = n/2$$
  $$it_3: len(array) = (n/2)/2 = n/2ˆ2$$
  $$[...]$$
  $$it_k: len(array) = (n/2ˆ1)/2ˆ(k-1) = n/2ˆk = 1$$
  $$2ˆk = n => log_2 2ˆk = log_2 n$$
  $$k*log_2 2 = log_2 n, ~ since ~ log_a a = 1$$
  $$k=log_2 n$$
  Portanto, uma função matemática que descreve a eficiência da function_2 é:
  $$T(n) = constante*log_2 n$$
* function_3:
  A function_3 acessa os elementos de uma estrutura do tipo hash table ou hashmaping. A complexidade desta operação é unitária, sendo assim: 
  $$T(n)=1$$
  A complexidade é:
  $$O(1)$$

## Estrutura de dados implementadas nos Datasets
* Dataset structure_1: Lista ordenada: estrutura de dados: Array (vetor)
* Dataset structure_2: Dicionário: Hash table