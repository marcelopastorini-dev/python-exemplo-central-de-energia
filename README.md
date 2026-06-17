# ⚡ Pastorini Energia - Gerador de Relatórios

Este programa em Python calcula o balanço de energia de uma unidade, avalia se a meta de economia foi atingida e gera um relatório automático em arquivo de texto.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3** (Linguagem de programação)
* **Manipulação de arquivos nativa** (Para gerar o arquivo `.txt`)

---

## 🚀 Como Utilizar o Programa

### 1. Pré-requisitos
Certifique-se de ter o **Python 3** instalado no seu computador.

### 2. Executando o Script
1. Abra o terminal ou prompt de comando na pasta onde está o arquivo do projeto.
2. Execute o comando abaixo para iniciar:
   ```bash
   python main.py
   ```
   *(Substitua `main.py` pelo nome exato do seu arquivo Python).*

### 3. Inserindo os Dados
O programa irá pedir três informações no terminal. Digite os valores e aperte **Enter**:
* O consumo atual da unidade (gasto em kWh).
* A energia gerada/injetada (em kWh).
* A meta de economia desejada (em Reais).

### 4. Resultado
Após inserir os dados, o programa criará automaticamente um arquivo chamado **`relatorio_fatura.txt`** na mesma pasta, contendo todo o resumo formatado.
