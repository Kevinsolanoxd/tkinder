#hallar raiz

from tkinter import*
from tkinter.font import BOLD, ROMAN


ventana=Tk()
ventana.title('Hallar Raiz')
ventana.geometry('800x500')
ventana.resizable(0,0)
ventana.config(bg='cadetblue3')

n=StringVar()
x=DoubleVar()
z=IntVar()


titilo=Label(ventana,text='Colegio San José de Guanenta')
titilo.config(bg='cadetblue3' ,fg='steelblue4',font=('Arial',20,BOLD))
titilo.place(x=200,y=10)

def sumar():
    z=pow(int(n.get()),1/int(x.get()))
    resultado.insert(INSERT,'la raiz del numero insertado es: ' + str(z))

subtitulo=Label(ventana,text='Hallar la raiz de un número ')
subtitulo.config(bg='cadetblue3', fg='steelblue4',font=('Arial',20, BOLD))
subtitulo.place(x=220,y=50)

etiq_a=Label(ventana, text='Ingrese El Número: ')
etiq_a.config(bg='cadetblue3',fg='white',font=('Arial',20,BOLD), anchor=CENTER)
etiq_a.place(x=200,y=130)

entry_a=Entry(ventana,width=4,textvariable= x)
entry_a.config(font=('Arial',20))
entry_a.place(x=450,y=130)

etiq_b=Label(ventana, text='Ingrese El Número Subradical: ')
etiq_b.config(bg='cadetblue3',fg='white',font=('Arial',20,BOLD), anchor=CENTER)
etiq_b.place(x=200,y=190)

entry_b=Entry(ventana,width=4,textvariable= n)
entry_b.config(font=('Arial',20))
entry_b.place(x=590,y=190)

boton=Button(ventana,width=8,height=1,text='Calcular',fg='white',font=('Arial',20,BOLD), command=sumar)
boton.config(bg='cadetblue3')
boton.place(x=300,y=250)

resultado=Text(ventana,width=48,height=4, bg='plum1')
resultado.config(bg='cadetblue1', font=("Courier", 20,BOLD))
resultado.place(x=10,y=350)




ventana.mainloop()