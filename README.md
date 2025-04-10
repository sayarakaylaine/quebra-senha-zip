# Quebra de Senha de Arquivos ZIP com Wordlist

Este projeto tem como objetivo desenvolver um script em Python que utiliza uma **wordlist** para tentar quebrar a senha de um arquivo ZIP protegido. A ferramenta realiza tentativas de senha sequenciais e, quando encontra a senha correta, a exibe no console.

## Funcionalidades

- **Varredura de Senhas**: O programa tenta várias senhas de uma **wordlist** e verifica se consegue extrair o conteúdo do arquivo ZIP.
- **Exibição de Progresso**: Durante a execução, o programa exibe informações sobre as senhas que estão sendo tentadas e o progresso das tentativas.
- **Interface de Linha de Comando**: A interação com o usuário ocorre via terminal, onde ele fornece o caminho do arquivo ZIP e da wordlist.

## Tecnologias Utilizadas

- **Python**: A linguagem principal para o desenvolvimento da ferramenta.
- **Módulo `zipfile`**: Usado para trabalhar com arquivos ZIP e tentar extrair os arquivos usando a senha.
- **Wordlist**: Uma lista de senhas possíveis a ser testada pelo programa.

## Requisitos

Para rodar o programa, você precisa ter o Python instalado em seu computador. Caso não tenha, siga as instruções no [site oficial do Python](https://www.python.org/downloads/) para instalar.

---

## Instalar Dependências

O script utiliza apenas bibliotecas padrão do Python, como o módulo zipfile, então não há necessidade de instalar pacotes adicionais.

## Clonar o Repositório

Clone este repositório para sua máquina local utilizando o comando:

```bash
git clone https://github.com/seu-usuario/quebra-zip.git
```
## Executar o Script

```bash
python zip_craker.py
```

---

## Usabilidade

1. **Preparando o Arquivo ZIP:** Certifique-se de ter um arquivo ZIP protegido por senha para testar. Você pode criar um arquivo ZIP protegido por senha utilizando programas como WinRAR ou 7-Zip.
2. **Preparando a Wordlist:** Crie ou baixe uma wordlist com senhas comuns. Cada linha da wordlist deve conter uma senha.
3. **Executando o Script:** O script irá percorrer todas as senhas da wordlist, tentando extrair os arquivos do ZIP. Quando encontrar a senha correta, o script exibirá a senha encontrada.

Exemplo de uma execução no terminal:

```bash
Caminho do arquivo ZIP: /caminho/do/arquivo.zip
Caminho da wordlist: /caminho/da/wordlist.txt
Tentando senha: 12345
Tentando senha: password123
Tentando senha: minhaSenha
✅ Senha encontrada: minhaSenha
```

---

# Como Funciona o Código
O código foi desenvolvido para realizar uma busca de senha no arquivo ZIP com base em uma wordlist. Abaixo está um resumo do funcionamento do script:

1. Abertura do Arquivo ZIP:
- O script usa o módulo zipfile para abrir e tentar extrair os conteúdos do arquivo ZIP.

2. Leitura da Wordlist:
- O arquivo de wordlist é aberto linha por linha, e cada senha é testada no arquivo ZIP.

3. Tentativas de Senha:
- A cada tentativa de senha, o script tenta extrair o conteúdo do ZIP usando a senha fornecida.
- Se a senha estiver correta, o conteúdo será extraído e o programa exibirá a senha correta no console.

4. Exibição de Progresso:
- O programa mostra o progresso das tentativas e exibe a senha correta assim que for encontrada.

# Considerações Finais
Este programa foi desenvolvido com fins educativos para demonstrar como a segurança de arquivos ZIP pode ser vulnerável se senhas fracas ou comuns forem utilizadas. Não utilize este script para fins ilícitos. Este programa deve ser utilizado apenas em arquivos de sua própria autoria ou com permissão explícita para realizar testes de segurança.

