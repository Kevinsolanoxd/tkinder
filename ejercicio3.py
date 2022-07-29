# invertir un umero 
from tkinter import*
from tkinter.font import BOLD, ROMAN


ventana=Tk()
ventana.title('Hallar Raiz')
ventana.geometry('800x500')
ventana.resizable(0,0)
ventana.config(bg='cadetblue3')

x=StringVar()
a=IntVar()
a1=IntVar()
a2=IntVar()

b=IntVar()
b1=IntVar()
b2=IntVar()

c=IntVar()
c1=IntVar()
c2=IntVar()

z=IntVar()


titilo=Label(ventana,text='Colegio San José de Guanenta')
titilo.config(bg='cadetblue3' ,fg='steelblue4',font=('Arial',20,BOLD))
titilo.place(x=200,y=10)

def sumar():
    a=int(x.get())%10
    a1=int(x.get())//10
    a2=a*1000
    b=a1%10
    b1=a1//10
    b2=b*100
    c=b1%10
    c1=b1//10
    c2=c*10
    z=a2+b2+c2+c1

    resultado.insert(INSERT,'El numero invertido es: ' + str(z))

subtitulo=Label(ventana,text='Invertir un numero  ')
subtitulo.config(bg='cadetblue3', fg='steelblue4',font=('Arial',20, BOLD))
subtitulo.place(x=270,y=50)

etiq_a=Label(ventana, text='Ingrese El Número: ')
etiq_a.config(bg='cadetblue3',fg='white',font=('Arial',20,BOLD), anchor=CENTER)
etiq_a.place(x=230,y=150)

entry_a=Entry(ventana,width=4,textvariable= x)
entry_a.config(font=('Arial',20))
entry_a.place(x=480,y=150)


boton=Button(ventana,width=8,height=1,text='Calcular',fg='white',font=('Arial',20,BOLD), command=sumar)
boton.config(bg='cadetblue3')
boton.place(x=300,y=250)

resultado=Text(ventana,width=48,height=4, bg='plum1')
resultado.config(bg='cadetblue1', font=("Courier", 20,BOLD))
resultado.place(x=10,y=350)




ventana.mainloop()