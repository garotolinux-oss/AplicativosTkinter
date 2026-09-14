import customtkinter as ctk

#configuração aparência
ctk.set_appearance_mode("dark")

#criacao das funcoes
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    #verificar
    if usuario == "joao" and senha == "123":
        resultadp_login.configure(text="Login valido", text_color="green")
    else:
         resultadp_login.configure(text="Login invalido", text_color="red")

#criação da janela principal
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("300x300")

#criação dos campos:

#1.label
label_usuario = ctk.CTkLabel(app, text="Usuário")
label_usuario.pack(pady=10)
#2.entry
campo_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário")
campo_usuario.pack(pady=10)

#1.label
label_senha = ctk.CTkLabel(app, text="Senha")
label_senha.pack(pady=10)
#2.entry
campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua Senha")
campo_senha.pack(pady=10)
#3.butoon
button = ctk.CTkButton(app, text="Login", command=validar_login)
button.pack(pady = 10)
#campo feedback
resultadp_login = ctk.CTkLabel(app, text="")
resultadp_login.pack(pady=10)

#iniciar a aplicação
app.mainloop()