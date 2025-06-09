import tkinter as tk
import time

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronómetro")

        # Widget de texto para mostrar el tiempo
        self.tiempo_label = tk.Label(root, text="00:00:00.00")
        self.tiempo_label.pack()

        # Botones para iniciar, pausar y reiniciar
        self.start_button = tk.Button(root, text="Iniciar", command=self.start_cronometro)
        self.start_button.pack()

        self.pause_button = tk.Button(root, text="Pausar", command=self.pause_cronometro)
        self.pause_button.pack()

        self.reset_button = tk.Button(root, text="Reiniciar", command=self.reset_cronometro)
        self.reset_button.pack()

        # Variable para controlar si el cronómetro está corriendo
        self.cronometro_corriendo = False

        # Variables para almacenar el tiempo inicial y la diferencia
        self.tiempo_inicial = None
        self.tiempo_diferencia = 0

    def start_cronometro(self):
        if not self.cronometro_corriendo:
            self.cronometro_corriendo = True
            self.tiempo_inicial = time.time() - self.tiempo_diferencia
            self.actualizar_tiempo()

    def pause_cronometro(self):
        if self.cronometro_corriendo:
            self.cronometro_corriendo = False
            self.tiempo_diferencia = time.time() - self.tiempo_inicial
        self.root.after_cancel(self.actualizar_id)

    def reset_cronometro(self):
        self.cronometro_corriendo = False
        self.tiempo_diferencia = 0
        self.tiempo_inicial = None
        self.actualizar_tiempo()
        self.root.after_cancel(self.actualizar_id)
        self.tiempo_label.config(text="00:00:00.00")

    def actualizar_tiempo(self):
        if self.cronometro_corriendo:
            self.tiempo_actual = time.time() - self.tiempo_inicial
            self.actualizar_texto(self.tiempo_actual)
            self.actualizar_id = self.root.after(10, self.actualizar_tiempo)

    def actualizar_texto(self, tiempo):
        horas = int(tiempo // 3600)
        minutos = int((tiempo % 3600) // 60)
        segundos = int(tiempo % 60)
        milisegundos = int((tiempo * 100) % 100)

        texto = "{:02d}:{:02d}:{:02d}.{:02d}".format(horas, minutos, segundos, milisegundos)
        self.tiempo_label.config(text=texto)

if __name__ == "__main__":
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()
