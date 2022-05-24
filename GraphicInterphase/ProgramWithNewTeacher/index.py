from tkinter import *
from PIL import ImageTk, Image

raiz = Tk()
raiz.title("Juegos gratis divertidos.com")
raiz.resizable(0,0)
raiz.iconbitmap(ImageTk.PhotoImage(Image.open('/home/baruch/Documentos/GitHub/POOE/GraphicInterphase/ProgramWithNewTeacher/icon.ico')))
raiz.geometry('650x350')
raiz.config(bg='gray')
raiz.mainloop()