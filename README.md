# 📚 Estrutura de Dados – Atividade Prática (UNINTER 2025)

Este repositório contém as implementações das duas questões propostas na atividade prática da disciplina **Estrutura de Dados / Programação III (2025)** do curso **UNINTER**.

---

## 🩺 Questão 1 – Lista Encadeada: Triagem Hospitalar

A **Questão 1** simula uma fila de espera com prioridade de atendimento em um hospital, utilizando uma **lista encadeada simples**.  

🟡 Pacientes com cartão **amarelo (A)** têm prioridade sobre os de cartão 🟢 **verde (V)**.  
📉 Dentro da mesma cor, os pacientes com **menor número** são atendidos primeiro.  
🔢 Cartões **verdes** iniciam em `1`, e os **amarelos** em `201`.

🧩 Funcionalidades:
- Inserção com e sem prioridade
- Impressão da fila de espera
- Atendimento (remoção do primeiro da fila)
- Menu interativo via terminal

📄 **Código-fonte:** `lista_encadeada/atendimento.py`

---

## 🚗 Questão 2 – Tabela Hash: Sistema de Emplacamento

A **Questão 2** implementa uma **tabela hash com encadeamento** para simular a distribuição de estados brasileiros em posições baseadas nas siglas das placas de veículos.  

🔢 A tabela possui **10 posições (0 a 9)** e a posição é calculada por:

```
(ord(sigla[0]) + ord(sigla[1])) % 10
```

📌 Exceção: a sigla **DF** sempre vai para a **posição 7**.  
📥 Inserções são feitas no **início da lista encadeada** da posição correspondente.

🧩 Funcionalidades:
- Impressão da tabela antes e depois das inserções
- Inserção dos **26 estados + Distrito Federal**
- Inserção de um **estado fictício** com as iniciais da autora (ex: `JS – Jamile Silva`)

📄 **Código-fonte:** `tabela_hash/emplacamento.py`

---

## 💻 Como Executar

Abra o terminal dentro da pasta correspondente e execute:

### ▶️ Questão 1:
```bash
cd lista_encadeada
python atendimento.py
```

### ▶️ Questão 2:
```bash
cd tabela_hash
python emplacamento.py
```

> ⚠️ Use `python3` no lugar de `python` se estiver no Linux ou Mac.

---

## 🌐 Futuras Funcionalidades

- [ ] Interface **frontend web** para visualização gráfica das estruturas:
  - Lista de espera (fila de triagem)
  - Tabela Hash (emplacamento por estado)

---

## 👩‍💻 Autora

**Jamile Santana da Silva**  
Estudante de Análise e Desenvolvimento de Sistemas  
📚 Universidade UNINTER – 2025

---

📌 *Este repositório faz parte da entrega oficial da atividade prática da disciplina Estrutura de Dados / Programação III.*

---

> ℹ️ Este arquivo README.md foi formatado com o auxílio de ferramentas de Inteligência Artificial para fins de organização e apresentação da atividade.
