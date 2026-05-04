Jogo de adivinhação via terminal: o computador sorteia um número secreto entre 1 e 100 e o jogador tenta acertá-lo com o auxílio de dicas "maior" ou "menor" a cada tentativa.

---

## 📋 Descrição

Script Python de linha de comando que exercita conceitos essenciais da linguagem:

- Geração de números aleatórios com o módulo `random`
- Laço `while` com condição de parada dinâmica
- Estruturas condicionais `if / elif`
- Entrada e conversão de dados com `input()` e `int()`
- Contagem de tentativas com variável acumuladora
- Formatação de saída com f-strings

---

## 🚀 Como usar

### Pré-requisitos

- Python 3.6 ou superior instalado

### Executando o script

```bash
python main.py
```

### Exemplo de execução

```
Tente acertar o número secreto de 1 a 100: 50
Você errou! O numero correto é maior, insira outro: 75
Você errou! O numero correto é menor, insira outro: 62
Você errou! O numero correto é menor, insira outro: 57
Parabens, você acertou em 4 tentativas.
```

---

## 🧠 Como funciona

1. O programa sorteia um número aleatório entre 1 e 100 com `random.randint()`
2. O jogador insere seu primeiro palpite
3. Um laço `while` continua enquanto o palpite for diferente do número secreto
4. A cada erro, o programa indica se o número correto é **maior** ou **menor**
5. O contador de tentativas é incrementado a cada rodada
6. Ao acertar, o programa parabeniza o jogador e exibe o total de tentativas

---

## ⚠️ Atenção — bug conhecido na versão original

Na versão original do script, o bloco `elif` não atribui o novo valor digitado à variável `num`, causando loop infinito:

```python
# ❌ bug — num nunca é atualizado
int(input("Você errou! O numero correto é maior, insira outro: "))

# ✅ correto
num = int(input("Você errou! O numero correto é maior, insira outro: "))
```

---

## 📁 Estrutura do projeto

```
number-guessing-game/
└── main.py
```

---

## 🛠️ Tecnologias

- **Python 3** — linguagem principal
- **random** — módulo da biblioteca padrão

---

## 📚 Conceitos demonstrados

| Conceito            | Aplicação no código                        |
|---------------------|--------------------------------------------|
| Módulo random       | `random.randint(1, 100)`                   |
| Laço while          | `while num != a:`                          |
| Condicionais        | `if num > a / elif num < a`                |
| Entrada de dados    | `int(input(...))`                          |
| Acumulador          | `chance += 1`                              |
| f-strings           | `f"você acertou em {chance} tentativas."`  |

---

## 💡 Possíveis melhorias

- Limitar o número máximo de tentativas (ex: modo difícil com 7 chances)
- Validar entradas fora do intervalo 1–100
- Exibir histórico de palpites anteriores
- Adicionar sistema de pontuação baseado no número de tentativas
- Permitir jogar novamente sem reiniciar o script

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

> Projeto didático para praticar lógica de programação e estruturas de controle em Python.
