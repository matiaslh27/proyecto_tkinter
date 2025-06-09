import tkinter as tk
import time
ventana = tk.Tk()
backgr = 'lightblue'
ventana.title('Reloj simple')
ventana.geometry('600x600')
ventana.config(background=backgr)
reloj = tk.Label(ventana, font =
('Arial', 60), bg = backgr , fg = '#000')
def hora():
 tiempo_actual = time.strftime('%H:%M')
 reloj.config(text = tiempo_actual)
 ventana.after(1000, hora)
reloj.pack(anchor = 'nw')

#configuro el movimiento del widget
x_pos = 0
y_pos = 0
#x_vel = 3
#y_vel = 2 
ancho = reloj.winfo_width()
alto = ventana.winfo_height() 

def mover_reloj():
 global x_pos, y_pos
 x_pos += 3
 y_pos += 2.5 
 reloj.place(x=x_pos,y=y_pos)
 if x_pos == 600 or y_pos == 600:
  x_pos = 0
  y_pos = 0
 ventana.after(50,mover_reloj)

mover_reloj()

hora()
ventana.mainloop()
