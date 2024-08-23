import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Inicialização das variáveis globais
linhas, colunas = 0, 0
reservas = []
total_poltronas = 0

def atualizar_total_poltronas():
    global total_poltronas
    total_poltronas = linhas * colunas

def criar_matriz(lin, col):
    return [["Disponível" for _ in range(col)] for _ in range(lin)]

def cadastrar_poltronas():
    global linhas, colunas, reservas, total_poltronas

    try:
        # Mostrar entrada para linhas e colunas
        lin = int(entry_linhas.get())
        col = int(entry_colunas.get())
        
        if lin < 1 or lin > 30 or col < 1 or col > 10:
            messagebox.showwarning("Cadastro", "Valores inválidos! Linhas: 1-30, Colunas: 1-10")
            return
        
        if lin != linhas or col != colunas:
            linhas, colunas = lin, col
            atualizar_total_poltronas()
            reservas = criar_matriz(linhas, colunas)
            atualizar_interface()
            messagebox.showinfo("Cadastro", "Quantidade de poltronas cadastrada com sucesso!")
        else:
            messagebox.showinfo("Cadastro", "Nenhuma alteração detectada.")
    except ValueError:
        messagebox.showwarning("Cadastro", "Por favor, insira números válidos.")

def realizar_reserva():
    global reservas

    try:
        linha = int(entry_linha_reserva.get())
        coluna = int(entry_coluna_reserva.get())

        if linha < 0 or linha >= linhas or coluna < 0 or coluna >= colunas:
            messagebox.showwarning("Reserva", "Linha ou coluna inválida!")
            return

        if reservas[linha][coluna] != "Disponível":
            messagebox.showwarning("Reserva", "Poltrona já reservada!")
            return

        nome = entry_nome_reserva.get()
        idade = int(entry_idade_reserva.get())

        if idade < 0:
            messagebox.showwarning("Reserva", "Idade inválida!")
            return

        reservas[linha][coluna] = f"{nome} ({idade})"
        atualizar_interface()
        messagebox.showinfo("Reserva", "Reserva realizada com sucesso!")
    except ValueError:
        messagebox.showwarning("Reserva", "Por favor, insira dados válidos.")

def atualizar_interface():
    global reservas

    for widget in frame_poltronas.winfo_children():
        widget.destroy()

    if linhas > 0 and colunas > 0:
        for i in range(linhas):
            for j in range(colunas):
                info = reservas[i][j]
                btn = tk.Button(frame_poltronas, text=f"{i}-{j}", width=6, height=3, 
                                command=lambda i=i, j=j: exibir_info(i, j),
                                font=("Helvetica", 10))
                if info == "Disponível":
                    btn.config(bg="lightgreen")
                else:
                    btn.config(bg="salmon", fg="white")
                btn.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

        # Configura a expansão das colunas e linhas
        for i in range(linhas):
            frame_poltronas.grid_rowconfigure(i, weight=1)
        for j in range(colunas):
            frame_poltronas.grid_columnconfigure(j, weight=1)

def exibir_info(linha, coluna):
    info = reservas[linha][coluna]
    messagebox.showinfo("Informação da Poltrona", f"Poltrona {linha}-{coluna}: {info}")

def visualizar_totais():
    global reservas

    if linhas == 0 or colunas == 0:
        messagebox.showwarning("Visualizar", "Você precisa cadastrar as poltronas primeiro!")
        return

    try:
        total_reservados = sum(1 for linha in reservas for poltrona in linha if poltrona != "Disponível")
        porcento_res = (total_reservados * 100) / total_poltronas if total_poltronas > 0 else 0
        total_disponiveis = total_poltronas - total_reservados
        porcento_disp = 100 - porcento_res
        messagebox.showinfo("Totais",
                            f"O TOTAL DE POLTRONAS É: {total_poltronas}\n"
                            f"Número de Reservas Feitas: {total_reservados} ({porcento_res:.2f}%)\n"
                            f"Poltronas Disponíveis: {total_disponiveis} ({porcento_disp:.2f}%)")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def sair():
    if messagebox.askyesno("Sair", "Deseja realmente sair do Sistema?"):
        root.quit()

def mostrar_tela_entrada():
    global gif_label, gif_frames, gif_index

    root.title("Sweet Flight - Tela de Introdução")
    root.geometry("800x600")
    root.configure(bg="#87CEEB")  # Cor de fundo azul claro

    # Slogan
    slogan = tk.Label(root, text="Sweet Flight", font=("Helvetica", 36, "bold"), bg="#87CEEB")
    slogan.pack(pady=20)

    # Adiciona uma imagem animada (por exemplo, um GIF do avião)
    gif_label = tk.Label(root, bg="#87CEEB")
    gif_label.pack(pady=20)

    # Carregar o GIF animado usando Pillow
    try:
        gif_path = "aviao.gif"  # Ajuste o caminho do arquivo conforme necessário
        gif_image = Image.open(gif_path)
        gif_frames = []

        for frame in range(gif_image.n_frames):
            gif_image.seek(frame)
            frame_image = ImageTk.PhotoImage(gif_image.copy())
            gif_frames.append(frame_image)

        gif_index = 0
        atualizar_gif()
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")

    # Fechar a tela de entrada após 5 segundos e abrir a tela principal
    root.after(5000, fechar_tela_entrada)

def atualizar_gif():
    global gif_index
    try:
        gif_frame = gif_frames[gif_index]
        gif_label.config(image=gif_frame)
        gif_label.image = gif_frame
        gif_index = (gif_index + 1) % len(gif_frames)
        root.after(100, atualizar_gif)  # Atualiza a cada 100 ms
    except Exception as e:
        print(f"Erro ao atualizar a animação do GIF: {e}")

def fechar_tela_entrada():
    global gif_label, frame_controls, frame_poltronas

    # Limpar a tela de introdução
    gif_label.destroy()

    # Configurar a interface principal
    frame_controls = tk.Frame(root, bg="#f0f0f0")
    frame_controls.pack(pady=20, fill='x')

    tk.Button(frame_controls, text="Cadastrar Poltronas", command=mostrar_formulario_cadastro, font=("Helvetica", 14), bg="#4CAF50", fg="white").pack(pady=5, fill='x')
    tk.Button(frame_controls, text="Realizar Reserva", command=mostrar_formulario_reserva, font=("Helvetica", 14), bg="#2196F3", fg="white").pack(pady=5, fill='x')
    tk.Button(frame_controls, text="Visualizar Totais", command=visualizar_totais, font=("Helvetica", 14), bg="#FFC107", fg="black").pack(pady=5, fill='x')
    tk.Button(frame_controls, text="Sair", command=sair, font=("Helvetica", 14), bg="#f44336", fg="white").pack(pady=20, fill='x')

    frame_poltronas = tk.Frame(root, bg="lightgrey")
    frame_poltronas.pack(expand=True, fill='both', padx=10, pady=10)

    # Ajusta o tamanho da janela para tela cheia
    root.attributes("-fullscreen", True)

    # Configurar o layout
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

def mostrar_formulario_cadastro():
    global entry_linhas, entry_colunas

    clear_form()

    # Formulário de cadastro de poltronas
    tk.Label(root, text="Cadastro de Poltronas", font=("Helvetica", 18), bg="#f0f0f0").pack(pady=10)
    
    tk.Label(root, text="Quantidade de Linhas:", bg="#f0f0f0").pack()
    entry_linhas = tk.Entry(root)
    entry_linhas.pack(pady=5)

    tk.Label(root, text="Quantidade de Colunas:", bg="#f0f0f0").pack()
    entry_colunas = tk.Entry(root)
    entry_colunas.pack(pady=5)

    tk.Button(root, text="Cadastrar", command=cadastrar_poltronas, font=("Helvetica", 14), bg="#4CAF50", fg="white").pack(pady=10)

def mostrar_formulario_reserva():
    global entry_linha_reserva, entry_coluna_reserva, entry_nome_reserva, entry_idade_reserva

    clear_form()

    # Formulário de reserva de poltronas
    tk.Label(root, text="Reserva de Poltronas", font=("Helvetica", 18), bg="#f0f0f0").pack(pady=10)
    
    tk.Label(root, text="Número da Linha:", bg="#f0f0f0").pack()
    entry_linha_reserva = tk.Entry(root)
    entry_linha_reserva.pack(pady=5)

    tk.Label(root, text="Número da Coluna:", bg="#f0f0f0").pack()
    entry_coluna_reserva = tk.Entry(root)
    entry_coluna_reserva.pack(pady=5)

    tk.Label(root, text="Nome:", bg="#f0f0f0").pack()
    entry_nome_reserva = tk.Entry(root)
    entry_nome_reserva.pack(pady=5)

    tk.Label(root, text="Idade:", bg="#f0f0f0").pack()
    entry_idade_reserva = tk.Entry(root)
    entry_idade_reserva.pack(pady=5)

    tk.Button(root, text="Reservar", command=realizar_reserva, font=("Helvetica", 14), bg="#2196F3", fg="white").pack(pady=10)

def clear_form():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Entry) or isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
            widget.destroy()

# Criação da janela principal
root = tk.Tk()
mostrar_tela_entrada()
root.mainloop()
