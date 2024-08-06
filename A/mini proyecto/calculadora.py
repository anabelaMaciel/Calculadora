from tkinter import *
from tkinter import ttk
from operaciones import suma, resta, division, multiplicacion

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("+500+80")

#Ruta completa
#ventana.iconbitmap(r"\calc.ico")

def elegir_tecla(tecla):
    if tecla >= "0" and tecla <= "9" or tecla == "(" or tecla == ")" or tecla == ".":
        entrada2.set(entrada2.get() + tecla)

    if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
        if tecla == "*":
            entrada1.set(entrada2.get() + "*")
        elif tecla == "/":
            entrada1.set(entrada2.get() + "/")
        elif tecla == "+":
            entrada1.set(entrada2.get() + "+")
        elif tecla == "-":
            entrada1.set(entrada2.get() + "-")
        entrada2.set(' ')

    if tecla == "=":
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def elegir_tecla_teclado(event):
    tecla = event.char
    print(event)
    if tecla >= "0" and tecla <= "9" or tecla == "(" or tecla == ")" or tecla == ".":
        entrada2.set(entrada2.get() + tecla)

    if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
        if tecla == "*":
            entrada1.set(entrada2.get() + "*")
        elif tecla == "/":
            entrada1.set(entrada2.get() + "/")
        elif tecla == "+":
            entrada1.set(entrada2.get() + "+")
        elif tecla == "-":
            entrada1.set(entrada2.get() + "-")
        entrada2.set(' ')

    if tecla == "=":
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def borrar(*args):
    inicio = 0
    final = len(entrada2.get())
    entrada2.set(entrada2.get()[inicio:final-1])

def borrar_todo(*args):
    entrada1.set(' ')
    entrada2.set(' ')



estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure("mainframa.TFrame", background="#DBDBDB")

mainframa = ttk.Frame(ventana, style="mainframa.TFrame")
mainframa.grid(column=0, row=0)

#Estilos labels
estilos_label1 = ttk.Style()
estilos_label1.configure("Label1.TLabel", font="arial 30", anchor="e")

estilos_label2 = ttk.Style()
estilos_label2.configure("Labe2.TLabel", font="arial 50", anchor="e")

#Labels
entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframa, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, E))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframa, textvariable=entrada2, style="Label2.TLabel")
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, E))

#Estilos botones
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure("Botones_numeros.TButton", font="arial 18", width=5, background="#FFFFFF", relief="flat")

estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure("Botones_borrar.TButton", font="arial 20", width=5, relief= "flat", background="#87CEEB")
estilos_botones_borrar.map("Botones_borrar.TButton", foreground=[("active", "#FF0000")])


estilos_botones_restantes= ttk.Style()
estilos_botones_restantes.configure("Botones_restantes.TButton", font="arial 20", width=5, relief= "flat", background="#B0E0E6")


#Botones numeros 
botton0 = ttk.Button(mainframa, text="0", style="Botones_numeros.TButton", command=lambda: elegir_tecla("0"))
botton1 = ttk.Button(mainframa, text="1", style="Botones_numeros.TButton", command=lambda: elegir_tecla("1"))
botton2 = ttk.Button(mainframa, text="2", style="Botones_numeros.TButton", command=lambda: elegir_tecla("2"))
botton3 = ttk.Button(mainframa, text="3", style="Botones_numeros.TButton", command=lambda: elegir_tecla("3"))
botton4 = ttk.Button(mainframa, text="4", style="Botones_numeros.TButton", command=lambda: elegir_tecla("4"))
botton5 = ttk.Button(mainframa, text="5", style="Botones_numeros.TButton", command=lambda: elegir_tecla("5"))
botton6 = ttk.Button(mainframa, text="6", style="Botones_numeros.TButton", command=lambda: elegir_tecla("6"))
botton7 = ttk.Button(mainframa, text="7", style="Botones_numeros.TButton", command=lambda: elegir_tecla("7"))
botton8 = ttk.Button(mainframa, text="8", style="Botones_numeros.TButton", command=lambda: elegir_tecla("8"))
botton9 = ttk.Button(mainframa, text="9", style="Botones_numeros.TButton", command=lambda: elegir_tecla("9"))


#Botones genericos xd
botton_borrar = ttk.Button(mainframa, text=chr(9003), style="Botones_borrar.TButton", command=lambda: borrar())
botton_borrar_todo = ttk.Button(mainframa, text="C", style="Botones_borrar.TButton", command=lambda: borrar_todo())
botton_parentesis1 = ttk.Button(mainframa, text="(", style="Botones_restantes.TButton", command=lambda: elegir_tecla("("))
botton_parentesis2 = ttk.Button(mainframa, text=")", style="Botones_restantes.TButton", command=lambda: elegir_tecla(")"))
botton_punto = ttk.Button(mainframa, text=".", style="Botones_restantes.TButton", command=lambda: elegir_tecla("."))

#Botones operaciones
botton_division = ttk.Button(mainframa, text=chr(247), style="Botones_restantes.TButton", command=lambda: elegir_tecla("/"))
botton_multiplicacion = ttk.Button(mainframa, text="x", style="Botones_restantes.TButton", command=lambda: elegir_tecla("*"))
botton_suma = ttk.Button(mainframa, text="+", style="Botones_restantes.TButton", command=lambda: elegir_tecla("+"))
botton_resta = ttk.Button(mainframa, text="-", style="Botones_restantes.TButton", command=lambda: elegir_tecla("-"))
botton_igual = ttk.Button(mainframa, text="=", style="Botones_restantes.TButton", command=lambda: elegir_tecla("="))


'''
Mostrar por pantalla todo
'''

#Botones genericos xd
botton_parentesis1.grid(column=0, row=2)
botton_parentesis2.grid(column=1, row=2)
botton_borrar_todo.grid(column=2, row=2)
botton_borrar.grid(column=3, row=2)

#Botones numeros 
botton0.grid(column=0 , row=6, columnspan=2, sticky=(W, E))
botton1.grid(column=0 , row=5)
botton2.grid(column=1 , row=5)
botton3.grid(column=2 , row=5)
botton4.grid(column=0 , row=4)
botton5.grid(column=1 , row=4)
botton6.grid(column=2 , row=4)
botton7.grid(column=0 , row=3)
botton8.grid(column=1 , row=3)
botton9.grid(column=2 , row=3)

#Botones operaciones
botton_igual.grid(column=0, row=7, columnspan=4, sticky=(W, E))
botton_division.grid(column=3, row=3)
botton_multiplicacion.grid(column=3, row=4)
botton_suma.grid(column=3, row=6)
botton_resta.grid(column=3, row=5)
botton_punto.grid(column=2, row=6)

#Llamada desde el teclado
ventana.bind('<Key>', elegir_tecla_teclado)
ventana.bind('<KeyPress-b>', borrar)
ventana.bind('<KeyPress-t>', borrar_todo)


ventana.mainloop()