import zipfile

def crack_zip(zip_path, wordlist_path):
    try:
        # Abrindo o arquivo ZIP
        with zipfile.ZipFile(zip_path) as zip_file:
            # Abrindo a wordlist
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
                total_lines = sum(1 for _ in wordlist)  # Contagem total de linhas na wordlist
                wordlist.seek(0)  # Voltar ao início após contagem

                for index, line in enumerate(wordlist, start=1):
                    password = line.strip()  # Remover espaços ou quebras de linha

                    # Exibir a senha sendo tentada
                    print(f"Tentando senha: {password}")  # Depuração

                    try:
                        # Tentando extrair o conteúdo usando a senha da wordlist
                        zip_file.extractall(pwd=password.encode())  # Removendo codificação 'utf-8' e tentando outra
                        print(f"\n✅ Senha encontrada: {password}")
                        return  # Se a senha for correta, termina o programa
                    except RuntimeError:
                        pass
                    
                    # Exibe progresso a cada 10 tentativas
                    if index % 10 == 0:
                        print(f"[-] Tentando: {password} | Tentativas: {index}/{total_lines}")
        
        print("\n❌ Nenhuma senha da wordlist funcionou.")
    
    except FileNotFoundError:
        print("Erro: Arquivo ZIP ou wordlist não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    zip_path = input("Caminho do arquivo ZIP: ").strip().strip('"')
    wordlist_path = input("Caminho da wordlist: ").strip().strip('"')
    crack_zip(zip_path, wordlist_path)
