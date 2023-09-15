import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def trabalho():
    nome = nomeEntry.get()
    mensagem = mensagemEntry.get()
    
    if nome and mensagem:
        mensagemjanela = tk.Toplevel(janela)
        mensagemjanela.title('Mensagem Enviada')
        Labelmensagem = tk.Label(mensagemjanela, text=f"{nome} diz {mensagem}")
        Labelmensagem.pack()
        janela.wait_window(mensagemjanela)
    else:
        messagebox.showerror("Erro", "Por favor, insira o nome e a mensagem")

janela = tk.Tk()
janela.title("Prova diagnóstica")
janela.geometry("250x250")

Nome = tk.Label(janela, text="Nome")
Nome.pack()
nomeEntry = tk.Entry(janela)
nomeEntry.pack()

mensagem = tk.Label(janela, text="Mensagem")
mensagem.pack()
mensagemEntry = tk.Entry(janela)
mensagemEntry.pack()

botaoenviar = tk.Button(janela, text="Enviar", command=trabalho)
botaoenviar.pack()

mensagemaguardando = tk.Label(janela, text="Aguardando mensagem do usuário")
mensagemaguardando.pack()

janela.mainloop()
