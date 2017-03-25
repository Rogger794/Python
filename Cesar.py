import sys
from tkinter import *

alfabeto=" a b c d e f g h i j k l m n ñ o p q r s t u v w x y z á é í ó ú"
numeros=" 0 1 2 3 4 5 6 7 8 9"
alfabeto=alfabeto+alfabeto.upper()+numeros
alfabeto=alfabeto.split()
tam=len(alfabeto)
encrip=""
dic={}
y=0
resultado=""
for x in alfabeto:
    dic[y]=x
    dic[x]=y
    y=y+1
d=0

def Desencriptar():
    T2.delete(1.0, END)   
    try:
       d = int(desplazamiento.get())
       y = T1.get(1.0, END)
       resultado=""
       for x in y:
           if x in dic:
               resultado=resultado+dic[(dic[x]-d)%tam]
           else:
               resultado=resultado+x
       etiqueta2.config(text="Texto desencriptado")
       T2.insert(END, resultado)
    except ValueError:
       resultado=""
       T2.delete(1.0, END)

def Encriptar():
    T2.delete(1.0, END)
    try:
       d = int(desplazamiento.get())
       y = T1.get(1.0, END)
       resultado=""
       for x in y:
           if x in dic:
               resultado=resultado+dic[(dic[x]+d)%tam]
           else:
               resultado=resultado+x
       etiqueta2.config(text="Texto encriptado")
       T2.insert(END, resultado)
    except ValueError:
       resultado=""
       T2.delete(1.0, END)

app = Tk()
app.title("Cifrado César")

vp = Frame(app, relief="raised")
vp.grid(column=0, row=0, padx=(25,25), pady=(10,10), sticky=(N, S, E, W))
vp.columnconfigure(0, weight=3)
vp.rowconfigure(0, weight=1)
        
scrollbar = Scrollbar(vp) 

etiqueta1 = Label(vp, text="Ingresar texto")
etiqueta1.grid(column=1, row=1, columnspan=3, sticky=(N,S,E,W))        

T1 = Text(vp, height=10, width=30)
T1.config(bd=5, yscrollcommand=scrollbar)
T1.grid(column=1, row=2, columnspan=3, sticky=(E, W))
T1.columnconfigure(0, weight=3)
T1.rowconfigure(0, weight=1)

etiqueta2 = Label(vp, text="Resultado")
etiqueta2.grid(column=1, row=3, columnspan=3, sticky=(N,S,E,W))

T2 = Text(vp, height=10, width=30)
T2.config(bd=5, yscrollcommand=scrollbar)
T2.grid(column=1, row=4, columnspan=3, sticky=(E, W))
T2.columnconfigure(0, weight=3)
T2.rowconfigure(0, weight=1)

boton1 = Button(vp, text="Encriptar", command=Encriptar)
boton1.grid(column=1, row=5)
 
boton2 = Button(vp, text="Desencriptar", command=Desencriptar)
boton2.grid(column=2, row=5)

desplazamiento = Entry(vp,width=10, textvariable=d)
desplazamiento.grid(column=3, row=5)
desplazamiento.columnconfigure(0, weight=1)
desplazamiento.rowconfigure(0, weight=1)

app.mainloop()
