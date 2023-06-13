from tkinter import *
import random


def maluj(event):
    kolory = podaj_kolor.get()
    kolory = kolory.split(', ')
    # print(kolory)
    kolor = random.choice(kolory)
    # print(kolor)
    obraz.create_oval(event.x, event.y, event.x, event.y, fill=kolor, outline=kolor, width=5)


def usun(event):
    obraz.create_rectangle(event.x, event.y, event.x, event.y, fill='white', outline='white', width=20)


okno = Tk()
okno.geometry('600x600')

obraz = Canvas(okno, width=500, height=500, bg='white')
obraz.pack()

podaj_kolor = Entry(okno)
podaj_kolor.pack()

obraz.bind('<B1-Motion>', maluj)
obraz.bind('<B3-Motion>', usun)

okno.mainloop()
