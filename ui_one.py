import tkinter as tk

def salvar_dados():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    if nome and endereco:
        with open("dados.txt", "a") as arquivo:
            arquivo.write(f"Nome: {nome} | Endereco: {endereco}\n")
        label_status.config(text=f'Dados salvos com sucesso!', fg="green")
        entry_nome.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)
    else:
        label_status.config(text="Digite o nome e o endereço.", fg="red")

root = tk.Tk()
root.title("Cadastro de Nomes e Endereços")
root.geometry("350x250")

label_instrucao_nome = tk.Label(root, text="Digite um nome:")
label_instrucao_nome.pack(pady=5)
entry_nome = tk.Entry(root)
entry_nome.pack(pady=5)

label_instrucao_endereco = tk.Label(root, text="Digite um endereço:")
label_instrucao_endereco.pack(pady=5)
entry_endereco = tk.Entry(root)
entry_endereco.pack(pady=5)

botao_salvar = tk.Button(root, text="Salvar", command=salvar_dados)
botao_salvar.pack(pady=10)

label_status = tk.Label(root, text="")
label_status.pack(pady=5)

root.mainloop()
