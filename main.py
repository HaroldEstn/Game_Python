# -*- coding:utf-8 -*-
'''
I'm Harold Esteban Gamboa Rodriguez  +57 320 471 3519
In this game You have to mach up the cards.
This game is not totaly mine, I have added new things and removed others for the original code. 
I have used the code form 3 people and I have comined it all in this game.
I thank the following people:
-Cronometro(stopwatch): RODY FERNANDEZ https://oimbaite.com/crear-cronometro-progresivo-de-24-horas-con-python-y-tkinter/.
-Memorama(game logic): Sprogramacion https://www.youtube.com/watch?v=BfhHWLQx5Gs&ab_channel=SProgramacion.
-Files: Teacher: JOSE MARIA STERLING COLLAZOS.
'''
try:
    from tkinter import messagebox, PhotoImage, Button
    from tkinter import Tk, Label, StringVar, Entry
    from clases import Cronometro, Puntajes, Carta
    from random import randrange
    from multiprocessing import Process
except ImportError as error:
    print(error)


class Juego:
    """
    This class has all the main functionality
    """
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Empareja')
        self.ventana.geometry('700x640')
        self.ventana.configure(bg='pale turquoise')
        self.botones = []
        self.cartas = []
        self.temporal = Carta()
        self.indice = 0
        self.par = 0
        self.movimientos = 0
        self.real_tiempo_1 = ""
        self.cronometro_inicio = False
        self.listo = True
        self.fondo = PhotoImage(file='imagenes/fondo.gif')
        self.nombre = StringVar()
        self.tiempo = StringVar()
        self.movimientos_label = StringVar()
        self.etiquetas()
        self.crear_tablero()
        self.revolver()
        self.etiquetas_mov()
        self.ahora = Cronometro(self.ventana)
        self.ventana.mainloop()

    def etiquetas(self):
        '''
        Show all labels in the window
        '''
        self.nombre.set('Kimiri <33')
        Label(self.ventana, text="WELCOME TO THE MEMORY GAME",
              bg="blue4",
              fg="red",
              font=('Times', 20)).place(x="110", y="20")
        Label(self.ventana, text="What is your name?: ",
              bg="RoyalBlue4",
              fg="red",
              font=("Times", 12)).place(x="150", y="80")
        Entry(self.ventana, width='20',
              bg="Blue4",
              fg="old lace",
              textvariable=self.nombre,
              font=('Helvetica', 12)).place(x="340", y="82")
        Label(self.ventana, text="move(s): ",
              bg="RoyalBlue4",
              fg="red",
              font=("Times", 12)).place(x="150", y="120")
        Label(self.ventana, text="Time: ",
              bg="RoyalBlue4",
              fg="red",
              font=("Times", 12)).place(x="340", y="120")

    def etiquetas_mov(self):
        '''
        Show all the moves in the game
        '''
        Label(self.ventana, text=self.movimientos,
              bg="White",
              fg="red",
              font=("Times", 12)).place(x="210", y="120")

    def crear_tablero(self):
        '''
        This create the board with all the buttons.
        '''
        i = 0
        contador = 0
        self.filas = 4 
        self.columnas = 4 # Change for 6 to have more cards
        if self.filas * self.columnas > 24:
            self.filas = 4
            self.columnas = 4
        while i < self.filas:
            j = 0
            while j < self.columnas:
                btn = Button(self.ventana, command=lambda a=contador:
                             self.revisar(a),
                             height=100, width=100, image=self.fondo)
                btn.place(x=40 + (j + 1) * 100, y=80 + (i + 1) * 100)
                self.botones.append(btn)
                j += 1
                contador += 1
            i += 1

    def revolver(self):
        '''
        This create the arrays with the values and mix it randomly
        '''
        i = 1
        parejas = int((self.filas * self.columnas)/2)
        while i <= parejas:
            carta1 = Carta()
            carta1.valor = i
            carta1.foto = PhotoImage(file='imagenes/'+str(i)+'.gif')
            carta2 = Carta()
            carta2.valor = i
            carta2.foto = PhotoImage(file='imagenes/'+str(i)+'.gif')
            self.cartas.append(carta1)
            self.cartas.append(carta2)
            i += 1
        cartas_temporal = []
        while len(self.cartas) > 0:
            posicion = randrange(0, len(self.cartas))
            cartas_temporal.append(self.cartas.pop(posicion))
        self.cartas = cartas_temporal

    def revisar(self, indice):
        '''
        change the pic of the button and 
        verify if has the same value that the other button
        '''
        self.real_tiempo_1 = self.ahora.real_tiempo
        if not self.cronometro_inicio:
            self.ahora.iniciar(0, 0, 0)
            self.cronometro_inicio = True
        if self.listo and self.cartas[indice].oculto:
            self.botones[indice].config(image=self.cartas[indice].foto)
            if self.par == 0:
                self.temporal = self.cartas[indice]
                self.cartas[indice].oculto = False
                self.temporal.posicion = indice
                self.par = 1
                self.movimientos += 1
                self.etiquetas_mov()
            elif self.par == 1:
                self.par = 0
                if self.temporal.valor == self.cartas[indice].valor:
                    self.cartas[indice].oculto = False
                    bandera = True
                    for elemento in self.cartas:
                        if elemento.oculto:
                            bandera = False
                            break
                    if bandera:
                        self.ahora.parar()
                        self.nombre = self.nombre.get()
                        self.tiempo = self.real_tiempo_1
                        self.movimientos_label = str(self.movimientos) + ' moves'
                        puntuacion = Puntajes(self.nombre, self.tiempo, self.movimientos_label)
                        puntuacion.guardar()
                        messagebox.showinfo("Yo Win!!!", "Congratulations!!")
                else:
                    self.indice = indice
                    self.listo = False
                    self.ventana.after(500, self.tapar)

    def tapar(self):
        '''
        If the pics of the two buttons is diferent set the
        defaul pic for both buttons
        '''
        self.cartas[self.temporal.posicion].oculto = True
        self.botones[self.temporal.posicion].config(image=self.fondo)
        self.botones[self.indice].config(image=self.fondo)
        self.listo = True


if __name__ == '__main__':
    p1 = Process(name='p1', target=Juego)
    p1.start()
