from tkinter import *
#criação da janela na biblioteca tkinter
janela = Tk()
janela.title('Cotação Atual das Moedas')
janela.geometry('400x400')

texto_orientacao = Label(janela, text='Clique no botão para realizar a conversão das moedas')
texto_orientacao.grid(column=0, row=0)
#texto_orientacao.configure(Label, justify=CENTER)#
botao = Button(janela, text='Buscar cotações')
janela.mainloop()
