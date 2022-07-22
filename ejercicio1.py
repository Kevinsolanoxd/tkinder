#app para calcular el IVA
from tkinter import*
from tkinter.font import BOLD, ROMAN


ventana=Tk()
ventana.title('Calcular IVA')
ventana.geometry('800x500')
ventana.resizable(0,0)
ventana.config(bg='cadetblue3')

a=StringVar()

logo=PhotoImage(file='IVA.png')
etiq_logo=Label(ventana,image=logo)
etiq_logo.config (bg='cadetblue3')
etiq_logo.place(x=10,y=30)
etiq_logo.config(width=300,height=150)

titilo=Label(ventana,text='Colegio San José de Guanenta')
titilo.config(bg='cadetblue3' ,fg='steelblue4',font=('Arial',20,BOLD))
titilo.place(x=290,y=10)


subtitulo=Label(ventana,text='El precio mas el IVA')
subtitulo.config(bg='cadetblue3', fg='steelblue4',font=('Arial',20, BOLD))
subtitulo.place(x=350,y=50)

etiq_a=Label(ventana, text='Ingrese El Valor Del Producto: ')
etiq_a.config(bg='cadetblue3',fg='white',font=('Arial',20,BOLD), anchor=CENTER)
etiq_a.place(x=200,y=180)

entry_a=Entry(ventana,width=4,textvariable= a )
entry_a.config(font=('Arial',20))
entry_a.place(x=572,y=180)

boton=Button(ventana,width=8,height=1,text='Calcular',fg='white',font=('Arial',20,BOLD))
boton.config(bg='')
boton.place(x=350,y=250)









# aportex = int ( "ingrese el precio" ))

# Procesandoy =  x * 0.19z = x + y

# producciónprint ( str ( x ) +  " pesos"  +  " mas el precio del iva que es el 19% queda en "  +  str ( z ) +  " pesos" )


























































ventana.mainloop()