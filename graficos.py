import matplotlib.pyplot
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#import math
#math.sin(math.radians(a)) - Seno
#math.cos(math.radians(a)) - Cosseno

janela = Tk()

def gra():
    try:
        if en.get() != '' and en1.get() != '' and en2.get() != '':
            x = [] # Eixo X
            y = [] # Eixo Y
            a = 0
            while len(x) < 10:
                x.append(a)
                y.append(float(en.get())**a + float(en1.get())*a + float(en2.get())) # Aqui é onde vai a função do gráfico
                a += 1

            # Declarando o gráfico e o canvas que é onde ele vai ficar
            fig = Figure(figsize=(15, 12), dpi=100)
            fig.add_subplot(111).plot(x, y)

            canvas = FigureCanvasTkAgg(fig, master=janela)
            canvas.draw()
            canvas.get_tk_widget().pack()
        else:
            messagebox.showinfo('Erro', 'Não há como gerar um gráfico sem nenhuma variável')
    except:
        messagebox.showinfo('Erro', 'Ocorreu um erro')

# Fazendo os inputs para pegar a função do gráfico

en = Entry(janela, width=3)
en.place(x=10, y=10)

lb = Label(janela, text='x² + ')
lb.place(x=35, y=10)

en1 = Entry(janela, width=3)
en1.place(x=65, y=10)

lb2 = Label(janela, text='x + ')
lb2.place(x=90, y=10)

en2 = Entry(janela, width=3)
en2.place(x=115, y=10)

bt = Button(janela, text='Fazer Gráfico', command=gra)
bt.place(x=50, y=50)

janela.mainloop()
