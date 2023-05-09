from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import pandas as pd

bgColor = "#242424"
fontColor = "#dce4ee"

mainWindow = Tk()
mainWindow.title("Controle de Caixa")
mainWindow.geometry("600x350")
mainWindow.configure(background=bgColor)
mainWindow.resizable(width=False, height=False)

mainLabel = Label(mainWindow, text="Controle de Caixa", font=("Century Gothic", 30), bg=bgColor, fg=fontColor)
mainLabel.place(x=120, y=30)

userLabel = Label(mainWindow, text="Usuário: ", font=("Century Gothic", 20), bg=bgColor, fg=fontColor)
userLabel.place(x=70, y=125)
userEntry = Entry(mainWindow, width=55)
userEntry.place(x=180, y=139)

passwLabel = Label(mainWindow, text="Senha: ", font=("Century Gothic", 20), bg=bgColor, fg=fontColor)
passwLabel.place(x=70, y=185)
passwEntry = Entry(mainWindow, width=55, show="•")
passwEntry.place(x=180, y=199)

entryDesc = Entry(mainWindow, width=75, font=("Century Gothic", 10))
entryValor = Entry(mainWindow, width=75, font=("Century Gothic", 10))
entryData = Entry(mainWindow, width=45, font=("Century Gothic", 10))
cbTipo = ttk.Combobox(mainWindow, values=['Entrada', 'Saida'], width=24, font=("Century Gothic", 10))


def clearEntry(entry):
    entry.delete(0, END)
    entry.insert(0, "")

def add():
    if entryDesc.get() != "" and entryData.get() != "" and entryValor.get() != "" and cbTipo.get() != "":
        try:
            df = pd.read_csv("df.csv")
            df.loc[len(df)] = [entryDesc.get(), entryValor.get(), entryData.get(), cbTipo.get()]
            df.to_csv("df.csv", index=False)

            clearEntry(entryDesc)
            clearEntry(entryValor)
            clearEntry(entryData)

            tkinter.messagebox.showinfo(title="Sucesso", message="Movimentação Adicionada com Sucesso!")
        except:
            df = pd.DataFrame(columns=["Descrição", "Valor", "Data", "Tipo"])
            df.loc[0] = [entryDesc.get(), entryValor.get(), entryData.get(), cbTipo.get()]
            df.to_csv("df.csv", index=False)

            clearEntry(entryDesc)
            clearEntry(entryValor)
            clearEntry(entryData)

            tkinter.messagebox.showinfo(title="Sucesso", message="Movimentação Adicionada com Sucesso!")

    else:
        tkinter.messagebox.showinfo(title="Erro", message="Preencha os dados corretamente!")


def vm():
    try:
        df_movs = pd.read_csv("df.csv")
        movs = df_movs.values.tolist()

        vmWindow = Toplevel()
        vmWindow.title("Movimentações")
        vmWindow.resizable(width=False, height=False)

        frame = Frame(vmWindow)
        frame.pack()
        scroll = Scrollbar(frame)
        scroll.pack(side="right", fill="y")

        treeview = tkinter.ttk.Treeview(frame, selectmode="browse", columns=("Descrição", "Valor", "Data", "Tipo"), show="headings",
                                        yscrollcommand=scroll.set)
        style = tkinter.ttk.Style()
        style.theme_use("default")
        scroll.configure(command=treeview.yview)
        style.configure("Treeview", background="#242424", foreground="#dce4ee", fieldbackground="#242424")

        treeview.column('Descrição', width=150, minwidth=15, stretch=NO)
        treeview.heading("#1", text="Descrição")

        treeview.column('Valor', width=120, minwidth=10, stretch=NO)
        treeview.heading("#2", text="Valor")

        treeview.column('Data', width=100, minwidth=10, stretch=NO)
        treeview.heading("#3", text="Data")

        treeview.column('Tipo', width=100, minwidth=10, stretch=NO)
        treeview.heading("#4", text="Tipo")

        for i, row in enumerate(movs):
            treeview.insert("", i, values=row)

        treeview.pack()

    except:
        tkinter.messagebox.showinfo(title="Erro", message="Não há Movimentações Registradas!")

addButton = ttk.Button(mainWindow, text="Adicionar", width=20, command=add)
vmButton = ttk.Button(mainWindow, text="Ver Movimentações", width=20, command=vm)

def login():
    if userEntry.get() == "user56" and passwEntry.get() == "1234":
        mainLabel.destroy()
        userLabel.destroy()
        userEntry.destroy()
        passwLabel.destroy()
        passwEntry.destroy()
        loginButton.destroy()

        mainWindow.title("Adicionar Movimentação")
        mainWindow.geometry("600x300")

        labelDesc = Label(mainWindow, text="Descrição", font=("Century Gothic", 11), bg=bgColor, fg=fontColor)
        labelDesc.place(y=25, x=35)
        entryDesc.place(y=55, x=35)

        labelValor = Label(mainWindow, text="Valor", font=("Century Gothic", 11), bg=bgColor, fg=fontColor)
        labelValor.place(y=90, x=35)
        entryValor.place(y=120, x=35)

        labelData = Label(mainWindow, text="Data", font=("Century Gothic", 11), bg=bgColor, fg=fontColor)
        labelData.place(y=150, x=35)
        entryData.place(y=185, x=35)

        labelTipo = Label(mainWindow, text="Tipo", font=("Century Gothic", 11), bg=bgColor, fg=fontColor)
        labelTipo.place(y=150, x=375)
        cbTipo.place(y=183, x=375)

        addButton.place(y=243, x=130)
        vmButton.place(y=243, x=340)

    else:
        tkinter.messagebox.showinfo(title="Erro de Login", message="Usuário não existe!")
        clearEntry(userEntry)
        clearEntry(passwEntry)


loginButton = ttk.Button(mainWindow, text="Entrar", width=30, command=login)
loginButton.place(x=200, y=265)

mainWindow.mainloop()