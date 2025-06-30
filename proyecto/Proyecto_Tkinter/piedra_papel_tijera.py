import tkinter as tk
import random

def iniciar_juego():
    opciones = ["piedra", "papel", "tijera"]

    ventana = tk.Toplevel()
    ventana.title("Piedra, Papel o Tijera")
    ventana.geometry("300x300")

    def jugar(usuario):
        maquina = random.choice(opciones)
        if maquina == usuario:
            resultado = "Empate"
        elif (usuario == "piedra" and maquina == "tijera") or \
             (usuario == "papel" and maquina == "piedra") or \
             (usuario == "tijera" and maquina == "papel"):
            resultado = "Ganaste"
        else:
            resultado = "Perdiste"
        etiqueta_resultado.config(text=f"Máquina eligió: {maquina}\n{resultado}")

    def resetear():
        etiqueta_resultado.config(text="")

    etiqueta = tk.Label(ventana, text="Elegí una opción:", font=("Arial", 14))
    etiqueta.pack(pady=10)

    tk.Button(ventana, text="Piedra", width=15, command=lambda: jugar("piedra")).pack(pady=5)
    tk.Button(ventana, text="Papel", width=15, command=lambda: jugar("papel")).pack(pady=5)
    tk.Button(ventana, text="Tijera", width=15, command=lambda: jugar("tijera")).pack(pady=5)

    etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12))
    etiqueta_resultado.pack(pady=15)

    tk.Button(ventana, text="Reset", width=15, command=resetear, bg="lightgray").pack()
