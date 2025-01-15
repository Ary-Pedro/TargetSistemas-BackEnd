# Desafio Back-End Proposto por [Target Sistemas](https://targetsistemas.com.br/)

Este repositório contém a solução para os desafios propostos pela vaga de Back-End na Target Sistemas. Abaixo estão os desafios e como resolvi cada um deles, utilizando Python e a interface customizada com `CustomTkinter`.

## Desafios

### 1) Soma de números
Dado o trecho de código abaixo:

```python
int INDICE = 13, SOMA = 0, K = 0;
while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
print(SOMA)
```

**Objetivo:** Calcular o valor de `SOMA` após a execução do loop. O valor final de `SOMA` será 91, pois a sequência soma os números de 1 a 13.

### 2) Sequência de Fibonacci
Escreva um programa que calcule a sequência de Fibonacci, onde o número informado será verificado para saber se pertence ou não à sequência.

```python
def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

n = int(input("Informe um número: "))
if fibonacci(n):
    print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} NÃO pertence à sequência de Fibonacci.")
```

### 3) Faturamento Diário
Dado um vetor com os valores de faturamento diário de uma distribuidora, calcule:

- O menor valor de faturamento ocorrido em um dia do mês;
- O maior valor de faturamento ocorrido em um dia do mês;
- O número de dias com faturamento superior à média mensal.

**Entrada:** JSON ou XML com os dados de faturamento.

```json
{
    "faturamento": [1500.00, 3200.00, 1800.00, 2200.00, 2900.00, 2500.00]
}
```

**Lógica de cálculo:** Ignorar dias sem faturamento (ex: finais de semana e feriados) e calcular a média mensal.

### 4) Percentual de Faturamento por Estado
Dado o faturamento mensal por estado, calcule o percentual de participação de cada estado no total de faturamento.

```python
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}
total = sum(faturamento.values())
percentual = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}
print(percentual)
```

### 5) Inversão de String
Escreva um programa que inverta os caracteres de uma string sem usar funções prontas como `reverse`.

```python
def inverter_string(s):
    return ''.join(reversed(s))

s = input("Informe uma string: ")
print(inverter_string(s))
```

## Solução Implementada

Para facilitar a interação com os desafios e proporcionar uma interface mais amigável, optei por utilizar a biblioteca `CustomTkinter`. A interface foi projetada para ter um visual mais moderno e fluido.

### Passo a Passo para Rodar o Projeto

#### 1. Criar o Ambiente Virtual (venv)

No Windows:
```powershell
py -m venv .venv
```

No macOS/Linux:
```bash
python3 -m venv .venv
```

#### 2. Ativar o Ambiente Virtual

No Windows:
```powershell
.venv\Scripts\activate
```

No macOS/Linux:
```bash
source .venv/bin/activate
```

#### 3. Instalar as Dependências do Projeto
```powershell
pip install -r requirements.txt
```

Certifique-se de ter o Python instalado em sua máquina. Para mais detalhes sobre a instalação do Python e como configurar um ambiente virtual, consulte a [documentação oficial do Python](https://docs.python.org/3/tutorial/venv.html).

## Repositório

para mais projetos e afins veja meu perfil
[GitHub - Ary-Pedro](https://github.com/Ary-Pedro)

## Conecte-se no LinkedIn

Se você quiser se conectar comigo ou discutir sobre este projeto, fique à vontade para me adicionar no [LinkedIn](https://www.linkedin.com/in/pedro-cézar-s-de-souza).

---

Essa solução foi desenvolvida com o objetivo de atender aos requisitos dos desafios propostos pela Target Sistemas, fornecendo uma aplicação prática com uma interface simplificada e de fácil uso.
