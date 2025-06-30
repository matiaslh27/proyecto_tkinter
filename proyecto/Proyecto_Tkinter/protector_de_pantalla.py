import tkinter as tk
import time

def iniciar_protector():
    ventana = tk.Toplevel()
    backgr = 'lightblue'
    ventana.title('Protector de Pantalla')
    ventana.geometry('600x600')
    ventana.config(background=backgr)

    reloj = tk.Label(ventana, font=('Arial', 60), bg=backgr, fg='#000')
    

    x_pos = 0
    y_pos = 0
    x_vel = 3
    y_vel = 2.5

    def hora():
        tiempo_actual = time.strftime('%H:%M')
        reloj.config(text=tiempo_actual)
        ventana.after(1000, hora)
    reloj.pack(anchor='nw')

    
    def mover_reloj():
        nonlocal x_pos, y_pos, x_vel, y_vel
        ventana.update()
        reloj_ancho = reloj.winfo_width()
        reloj_alto = reloj.winfo_height()
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()

        x_pos += x_vel
        y_pos += y_vel

        if x_pos < 0 or x_pos + reloj_ancho > ancho:
            x_vel = -x_vel
        if y_pos < 0 or y_pos + reloj_alto > alto:
            y_vel = -y_vel

        reloj.place(x=x_pos, y=y_pos)
        ventana.after(50, mover_reloj)

    hora()
    mover_reloj()
