import tkinter
from PIL import Image, ImageTk
from tkinter import filedialog, PhotoImage

def buscar_nueva():
    global imagen
    global img
    archivo = filedialog.askopenfilename(filetypes=[("Image", ("*.jpg", "*.png"))])
    img = Image.open(archivo)
    img = img.resize((500,300))
    img = ImageTk.PhotoImage(img)
    imagen = tkinter.Label(ventana, image=img)
    imagen.image = img
    imagen.pack()
    
ventana = tkinter.Tk()
ventana.title("Editor de Imagenes")
ventana.geometry("800x600+50+50")
ventana.resizable(0,0)
ventana.configure(bg="#ebe7a7")

titulo = tkinter.Label(ventana, text="Proyecto Python")
titulo.pack()

btn = tkinter.Button(ventana, text="Buscar", height=3, width=10, command= buscar_nueva)
btn.configure(bg="grey")
btn.pack()




ventana.mainloop()