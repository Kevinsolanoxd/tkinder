# hallar area y perimetro de un circulo

from tkinter import*
from tkinter.font import BOLD, ROMAN
import math


ventana=Tk()
ventana.title('Hallar el area y perimetro de un circulo')
ventana.geometry('800x500')
ventana.resizable(0,0)
ventana.config(bg='cadetblue3')

radio=StringVar()
area=IntVar()
perimetro=IntVar()

titilo=Label(ventana,text='Colegio San José de Guanenta')
titilo.config(bg='cadetblue3' ,fg='steelblue4',font=('Arial',20,BOLD))
titilo.place(x=200,y=10)

def sumar():
    area = math.pi* int(radio.get()) *int(radio.get())
    perimetro=2* int(radio.get())* math.pi
    resultado.insert(INSERT,'el area es: ' + str(area) + 'el perimetro es: ' + str(perimetro))

subtitulo=Label(ventana,text='Hallar el area y el perimetro de un circulo')
subtitulo.config(bg='cadetblue3', fg='steelblue4',font=('Arial',20, BOLD))
subtitulo.place(x=220,y=50)

etiq_a=Label(ventana, text='Ingrese El Radio: ')
etiq_a.config(bg='cadetblue3',fg='white',font=('Arial',20,BOLD), anchor=CENTER)
etiq_a.place(x=200,y=130)

entry_a=Entry(ventana,width=4,textvariable= radios)
entry_a.config(font=('Arial',20))
entry_a.place(x=450,y=130)

boton=Button(ventana,width=8,height=1,text='Calcular',fg='white',font=('Arial',20,BOLD), command=sumar)
boton.config(bg='cadetblue3')
boton.place(x=300,y=250)

resultado=Text(ventana,width=48,height=4, bg='plum1')
resultado.config(bg='cadetblue1', font=("Courier", 20,BOLD))
resultado.place(x=10,y=350)




ventana.mainloop()