import zipfile
import time
import os
import argparse
from tkinter import Tk, Label, Entry, Button, Text, filedialog, END, ttk
from colorama import Fore, init

# Inicializa o colorama para colorir textos no terminal
init(autoreset=True)

# Função principal que tenta quebrar a senha do arquivo ZIP
def crack_zip(zip_path, wordlist_path, show_attempts=True, gui_log_callback=None, gui_progress_callback=None):
    # Verifica se o arquivo ZIP existe
    if not os.path.isfile(zip_path):
        msg = f"Arquivo ZIP não encontrado: {zip_path}"
        print(Fore.RED + msg)
        if gui_log_callback:
            gui_log_callback(f"❌ {msg}")
        if gui_progress_callback:
            gui_progress_callback(0, "red")
        return None

    # Verifica se a wordlist existe
    if not os.path.isfile(wordlist_path):
        msg = f"Wordlist não encontrada: {wordlist_path}"
        print(Fore.RED + msg)
        if gui_log_callback:
            gui_log_callback(f"❌ {msg}")
        if gui_progress_callback:
            gui_progress_callback(0, "red")
        return None

    try:
        with zipfile.ZipFile(zip_path) as zip_file:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
                passwords = wordlist.readlines()
                total = len(passwords)
                start_time = time.time()

                for idx, line in enumerate(passwords):
                    password = line.strip()
                    try:
                        # Tenta extrair com a senha atual
                        zip_file.extractall(pwd=password.encode('utf-8'))

                        # Se conseguiu extrair, calcula o tempo e exibe sucesso
                        elapsed = time.time() - start_time
                        success = f"\n✅ Senha encontrada: {password}"
                        tempo = f"⏱ Tempo decorrido: {elapsed:.2f} segundos"
                        if gui_log_callback:
                            gui_log_callback(success)
                            gui_log_callback(tempo)
                        else:
                            print(Fore.GREEN + success)
                            print(Fore.CYAN + tempo)
                        if gui_progress_callback:
                            gui_progress_callback(100, "green")
                        return password
                    except:
                        # Se a senha estiver errada, mostra a tentativa
                        if show_attempts:
                            tentativa = f"Tentando senha: {password}"
                            if gui_log_callback:
                                gui_log_callback(tentativa)
                            else:
                                print(Fore.YELLOW + tentativa)

                    # Atualiza a barra de progresso na GUI
                    if gui_progress_callback:
                        progresso = int((idx + 1) / total * 100)
                        gui_progress_callback(progresso, "blue")

        # Se não encontrou a senha
        msg_final = "❌ Nenhuma senha da wordlist funcionou."
        if gui_log_callback:
            gui_log_callback(msg_final)
        else:
            print(Fore.RED + msg_final)
        if gui_progress_callback:
            gui_progress_callback(100, "red")
        return None

    except zipfile.BadZipFile:
        erro = "Erro: O arquivo fornecido não é um ZIP válido."
        print(Fore.RED + erro)
        if gui_log_callback:
            gui_log_callback(erro)
        if gui_progress_callback:
            gui_progress_callback(0, "red")
        return None

# Função auxiliar para selecionar arquivos via janela
def browse_file(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, END)
    entry.insert(0, file_path)

# Interface gráfica com Tkinter
def run_gui():
    # Atualiza o valor e cor da barra de progresso
    def update_progress(value, color):
        style_name = f"{color}.Horizontal.TProgressbar"
        progress_bar.config(style=style_name)
        progress_bar['value'] = value
        root.update_idletasks()

    # Inicia o processo de quebra de senha
    def start_crack():
        zip_path = zip_entry.get().strip()
        wordlist_path = wordlist_entry.get().strip()
        output_text.delete(1.0, END)
        progress_bar['value'] = 0
        update_progress(0, "blue")
        crack_zip(
            zip_path,
            wordlist_path,
            gui_log_callback=lambda msg: output_text.insert(END, msg + '\n'),
            gui_progress_callback=update_progress
        )

    # Limpa todos os campos e a barra de progresso
    def clear_fields():
        zip_entry.delete(0, END)
        wordlist_entry.delete(0, END)
        output_text.delete(1.0, END)
        update_progress(0, "blue")

    # Criação da janela principal
    root = Tk()
    root.title("Quebrador de ZIP")
    root.geometry("500x480")
    root.resizable(False, False)

    # Estilos para cores da barra de progresso
    style = ttk.Style()
    style.theme_use('default')
    style.configure("blue.Horizontal.TProgressbar", foreground='blue', background='blue')
    style.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
    style.configure("red.Horizontal.TProgressbar", foreground='red', background='red')

    # Campos de entrada e botões
    Label(root, text="Arquivo ZIP:").pack(pady=5)
    zip_entry = Entry(root, width=50)
    zip_entry.pack()
    Button(root, text="Selecionar ZIP", command=lambda: browse_file(zip_entry)).pack(pady=5)

    Label(root, text="Arquivo Wordlist:").pack(pady=5)
    wordlist_entry = Entry(root, width=50)
    wordlist_entry.pack()
    Button(root, text="Selecionar Wordlist", command=lambda: browse_file(wordlist_entry)).pack(pady=5)

    Button(root, text="🔓 Quebrar Senha", command=start_crack, bg="#28a745", fg="white").pack(pady=10)

    # Barra de progresso
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
    progress_bar.pack(pady=5)

    # Área de saída dos resultados
    output_text = Text(root, height=10, width=60)
    output_text.pack(pady=10)

    # Botão de limpar
    Button(root, text="🧹 Limpar Campos", command=clear_fields, bg="#dc3545", fg="white").pack(pady=5)

    root.mainloop()

# Versão para terminal
def run_cli():
    print(Fore.CYAN + "\n=== Quebrador de Senha ZIP ===\n")
    zip_path = input("Caminho do arquivo ZIP: ").strip().strip('"')
    wordlist_path = input("Caminho da wordlist: ").strip().strip('"')
    print(Fore.BLUE + "\n🔍 Iniciando tentativa de quebra...\n")
    crack_zip(zip_path, wordlist_path)

# Ponto de entrada principal do programa
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quebra de senha de arquivos ZIP com wordlist")
    parser.add_argument("--gui", action="store_true", help="Executar com interface gráfica")
    args = parser.parse_args()

    if args.gui:
        run_gui()
    else:
        run_cli()
