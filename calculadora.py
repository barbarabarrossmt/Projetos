# Código de uma calculadora simples em python

# num1, num2, op, result

num1 = 0
num2 = 0 
result = 0 
op  = ''

while True:
    num1 = float (input('Digite o primeiro número: ')) #ler o número
    op = input('Digite a operação matemática a ser feita: ')
    num2 = float (input('Digite o segundo número: '))

    if op == '+':
        result = num1 + num2

    elif op == '-':
        result = num1 - num2

    elif op == '/':
        result = num1 / num2

    elif op == '*':
        result = num1 * num2

    else:
        print('Operação não reconhecida!')

    print ('{} {} {} = {}'.format(num1, op, num2, result))


# Calculadora Simples em Python

Uma calculadora de linha de comando desenvolvida em Python puro.

## 🚀 Funcionalidades

- [x] Adição (+)
- [x] Subtração (-)
- [x] Multiplicação (*)
- [x] Divisão (/)
- [x] Interface simples no terminal
- [x] Tratamento de erros básico

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/calculadora-python.git

# Entre no diretório
cd calculadora-python

# Execute a calculadora
python src/calculadora.py
