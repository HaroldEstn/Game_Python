# -*- coding: utf-8 -*-
'''
Carta(card)
Cronometro(Stopwatch)
Puntajes(Score)
Modulo clases.py
'''
try:
    from tkinter import messagebox, Label, PhotoImage
    from archivos import buscar_registro
except ImportError as error:
    print(error)
PROCESO = 0


class Carta:
    '''
    has all attributes for the cards
    '''
    def __init__(self):
        self.valor = 0
        self.posicion = 0
        self.oculto = True
        self.foto = PhotoImage(file='imagenes/fondo.gif')


class Cronometro:
    '''
    Stopwatch Start in the fist click and end 
    when the game is finished
    '''
    def __init__(self, ventana):
        self.ventana = ventana
        self.real_tiempo = ""
        self.time = Label()

    def iniciar(self, horas, minutos, segundos):
        '''
        Stopwatch start
        '''
        global PROCESO
        if segundos >= 60:
            segundos = 0
            minutos = minutos + 1
            if minutos >= 60:
                minutos = 0
                horas = horas + 1
                if horas >= 24:
                    horas = 0
        self.real_tiempo = (str(horas).zfill(2) + ":" +
                            str(minutos).zfill(2) + ":" +
                            str(segundos).zfill(2))
        self.repeticion()
        self.time['text'] = (str(horas) + ":" +
                             str(minutos) + ":" +
                             str(segundos))
        PROCESO = self.time.after(1000, self.iniciar, (horas),
                                  (minutos), (segundos + 1))

    def parar(self):
        '''Stopwatch stop
        '''
        global PROCESO
        self.time.after_cancel(PROCESO)

    def repeticion(self):
        '''Label for stopwatch
        '''
        Label(self.ventana, text=self.real_tiempo,
              bg="White",
              fg="red",
              font=("Times", 12)).place(x="380", y="120")


class Puntajes:
    '''save the data
    '''
    def __init__(self, nombre, tiempo, movimientos):
        self.nombre = "--" + nombre + "--"
        self.tiempo = "--" + tiempo + "--"
        self.movimientos = "--" + movimientos + "--"
        super().__init__()

    def guardar(self):
        '''name, time, moves will be save
        '''
        confirmacion = messagebox.askyesno(
            message=('Do you want to save your score?',
                     self.nombre, self.tiempo), title='Confirmación')
        if confirmacion:
            buscar_registro(self.nombre, self.tiempo, self.movimientos)
        else:
            print('Don´t worry you score is not save')

