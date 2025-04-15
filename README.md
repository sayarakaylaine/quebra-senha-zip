# Quebra de Senha de Arquivos ZIP com Wordlist

Este projeto é um script em Python desenvolvido para quebrar a senha de arquivos ZIP protegidos utilizando uma **wordlist** com senhas comuns. Ideal para fins **educacionais** e para testar a segurança de arquivos ZIP com senhas fracas ou conhecidas. Ela pode ser executada tanto por linha de comando quanto por uma interface gráfica intuitiva feita com Tkinter.

## 🛠 Funcionalidades
- **Quebra de senha de arquivos ZIP** utilizando uma lista de senhas (Wordlist)
- **Interface gráfica** simples e funcional (Tkinter)
- **Versão em terminal** com feedback colorido (Via Colorama)
- **Barra de progresso** para acompanhar a tentativa de quebra (na GUI)
- Validação de arquivos e tratamento de erros
- Botão para limpar todos os campos na GUI
- **Exibe o andamento** das tentativas no terminal e na GUI
- **Exibição da senha encontrada** assim que o arquivo for extraído com sucesso

## 💻 Tecnologias Utilizadas
- [Python 3](https://www.python.org/)
- **zipfile** – Módulo nativo do Python para manipulação de arquivos ZIP
- **CLI (Interface de Linha de Comando)** – Interação com o usuário via terminal
- **GUI (Interface Gráfica)** – Interação com o usuário atráves da interface gráfica
- **Wordlist** – Lista de senhas comuns utilizadas na quebra de senhas ZIP

## 🧾 Requisitos
- Python 3.7 ou superior
- Arquivo ZIP protegido por senha, certifique-se de que o arquivo realmente está protegido
- Uma **wordlist** contendo possíveis senhas
- A eficácia depende da qualidade da wordlist utilizada.

## 📦 Clonando o Repositório

Clone este repositório para sua máquina local utilizando o comando:

```bash
git clone https://github.com/seu-usuario/quebra-zip.git
cd quebra-zip
```

---

## 🛂 Instalação das Dependências
Antes de executar, certifique-se de ter os seguintes itens instalados:

**Passo 1:** Instalar o Python
Se ainda não tiver o Python 3 instalado, baixe e instale-o a partir do seguinte link: [Python 3](https://www.python.org/)

**Passo 2:** Instalar o Colorama
```bash
pip install colorama
```

---

## 🚀 Como Executar
### Modo Linha de Comando (CLI)
Para rodar o script, digite no terminal:

```bash
python zip_craker.py
```
Você será solicitado a fornecer o caminho do arquivo ZIP e o caminho da sua wordlist. O script começará a testar as senhas da wordlist até encontrar a senha correta ou esgotar as tentativas.

**Exemplo de uma execução no terminal:**

```bash
Caminho do arquivo ZIP: /caminho/do/arquivo.zip
Caminho da wordlist: /caminho/da/wordlist.txt
---Iniciando quebra de senha---
Tentando senha: 12345
Tentando senha: password123
Tentando senha: minhaSenha
✅ Senha encontrada: minhaSenha
```

### Modo Gráfico (GUI)
Para rodar a interface gráfica, execute o mesmo comando acima adicionando o parâmetro --gui no final:
```bash
python zip_craker.py --gui
```

**Para executar a quebra de senha na interface, siga os seguintes passos:**

1. Selecione o arquivo ZIP
2. Selecione a wordlist
3. Clique em "Quebrar Senha"
4. Use o botão "Limpar Campos" para reiniciar os campos
   
A barra de progresso e o log de tentativas serão atualizados em tempo real.
  
---

## ⚠ Aviso Legal
Este script foi desenvolvido para fins educacionais e para demonstrar como senhas fracas podem tornar arquivos ZIP vulneráveis. Não use este programa em arquivos de terceiros sem autorização explícita. O uso indevido pode ser considerado ilegal segundo as leis locais.

## 👩🏻‍💻 Autora
Desenvolvido por **`Sayara Kaylaine Oliveira Silva`**, sob orientação do professor **`Karan Luciano`**, no Instituto Federal de Rondônia (IFRO) - Campus Ji-Paraná.
