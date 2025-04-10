# Quebra de Senha de Arquivos ZIP com Wordlist

Este projeto é um script em Python desenvolvido para quebrar a senha de arquivos ZIP protegidos utilizando uma **wordlist** com senhas comuns. Ideal para fins **educacionais** e para testar a segurança de arquivos ZIP com senhas fracas ou conhecidas.

## 🛠 Funcionalidades
- **Quebra de senha de arquivos ZIP** utilizando uma lista de senhas (wordlist)
- **Interface de linha de comando (CLI)** simples para interação com o usuário
- Exibe o progresso das tentativas no terminal
- **Exibição da senha encontrada** assim que o arquivo for extraído com sucesso

## 💻 Tecnologias Utilizadas
- [Python 3](https://www.python.org/)
- **zipfile** – Módulo nativo do Python para manipulação de arquivos ZIP
- **CLI (Interface de Linha de Comando)** – Interação com o usuário via terminal
- **Wordlist** – Lista de senhas comuns utilizadas na quebra de senhas ZIP

## 🧾 Requisitos
- Python 3.7 ou superior
- Arquivo ZIP protegido por senha
- Uma **wordlist** contendo possíveis senhas

## 📦 Clonando o Repositório

Clone este repositório para sua máquina local utilizando o comando:

```bash
git clone https://github.com/seu-usuario/quebra-zip.git
cd quebra-zip
```

---

## 🛂 Instalação das Dependências
Este projeto não possui dependências externas além das bibliotecas padrão do Python.

**Passo 1:** Instalar o Python
Se ainda não tiver o Python 3 instalado, baixe e instale-o a partir do site oficial do Python.

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
Tentando senha: 12345
Tentando senha: password123
Tentando senha: minhaSenha
✅ Senha encontrada: minhaSenha
```

---

## ⚠ Aviso Legal
Este script foi desenvolvido para fins educacionais e para demonstrar como senhas fracas podem tornar arquivos ZIP vulneráveis. Não use este programa em arquivos de terceiros sem autorização explícita. O uso indevido pode ser considerado ilegal segundo as leis locais.

## 👩🏻‍💻 Autora
Desenvolvido por **`Sayara Kaylaine Oliveira Silva`**, sob orientação do professor **`Karan Luciano`**, no Instituto Federal de Rondônia (IFRO) - Campus Ji-Paraná.
