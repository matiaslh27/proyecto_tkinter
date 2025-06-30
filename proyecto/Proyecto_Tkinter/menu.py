import tkinter as tk
from piedra_papel_tijera import iniciar_juego
from protector_de_pantalla import iniciar_protector

ventana = tk.Tk()
ventana.title('Menú Principal')
ventana.geometry('400x300')
ventana.config(background='lightblue')

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Principal', menu=menu_principal)

submenu = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label='Opciones', menu=submenu)

submenu.add_command(label='Piedra, Papel o Tijeras', command=iniciar_juego)
submenu.add_command(label='Protector de Pantalla', command=iniciar_protector)

ventana.mainloop()
