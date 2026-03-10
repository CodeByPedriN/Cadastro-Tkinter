import tkinter as tk

def cadastrar_produto():
    produto = entry_produto.get()
    preço = entry_preco.get()
    quantidade = entry_quantidade.get()
    if produto and preço and quantidade:
        with open("Produtos.txt", "a") as arquivo:
            arquivo.write(f"Produto: {produto} | Preco: R${preço} | Quantidade: {quantidade}\n")
        label_status.config(text=f'Produto cadastrado com sucesso!', fg="green")
        entry_produto.delete(0, tk.END)
        entry_preco.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
    else:
        label_status.config(text="Digite o produto, o preço e a quantidade.", fg="red")

root = tk.Tk()
root.title("Cadastro de Produtos")
root.geometry("350x250")

label_instrucao_produto = tk.Label(root, text="Digite o produto:")
label_instrucao_produto.pack(pady=5)
entry_produto = tk.Entry(root)
entry_produto.pack(pady=5)

label_instrucao_quantidade = tk.Label(root, text="Digite a quantidade:")
label_instrucao_quantidade.pack(pady=5)
entry_quantidade = tk.Entry(root)
entry_quantidade.pack(pady=5)

label_instrucao_preco = tk.Label(root, text="Digite o preço:")
label_instrucao_preco.pack(pady=5)
entry_preco = tk.Entry(root)
entry_preco.pack(pady=5)

botao_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar_produto)
botao_cadastrar.pack(pady=10)

label_status = tk.Label(root, text="")
label_status.pack(pady=5)

root.mainloop()
