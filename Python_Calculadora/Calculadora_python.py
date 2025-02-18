import tkinter as tk
from tkinter import Button
import re

class Interfaz:
    def __init__(self, ventana):
        # Iniciamos la ventana con un título
        self.ventana = ventana
        self.ventana.title("Calculadora")

        # Agregamos una pantalla de texto para que sea la pantalla de la calculadora
        self.pantalla = tk.Text(self.ventana, state="disabled", width=40, height=3, background="oliveDrab1", foreground="white", font=("Helvetica", 16))

        # Ubicar la pantalla en la ventana
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Inicializando la operación mostrada en pantalla como string vacío
        self.operacion = ""

        # Crear los botones de la calculadora
        boton1 = self.crearBoton(7)
        boton2 = self.crearBoton(8)
        boton3 = self.crearBoton(9)
        boton4 = self.crearBoton(u"\u232B", escribir=False)
        boton5 = self.crearBoton(4)
        boton6 = self.crearBoton(5)
        boton7 = self.crearBoton(6)
        boton8 = self.crearBoton(u"\u00F7")
        boton9 = self.crearBoton(1)
        boton10 = self.crearBoton(2)
        boton11 = self.crearBoton(3)
        boton12 = self.crearBoton("*")
        boton13 = self.crearBoton(".")
        boton14 = self.crearBoton("0")
        boton15 = self.crearBoton("+")
        boton16 = self.crearBoton("-")
        boton17 = self.crearBoton("=", escribir=False, ancho=20, alto=2)

        # Ubicar los botones con el gestor grid
        botones = [boton1, boton2, boton3, boton4, boton5, boton6, boton7, boton8, boton9, boton10, boton11, boton12, boton13, boton14, boton15, boton16, boton17]
        contador = 0
        for fila in range(1, 5):
            for columna in range(4):
                botones[contador].grid(row=fila, column=columna)
                contador += 1
        
        # Ubicar el último botón al final
        botones[16].grid(row=5, column=0, columnspan=4)

    # Crear un botón mostrando el valor pasado por parámetro
    def crearBoton(self, valor, escribir=True, ancho=9, alto=1):
        return Button(self.ventana, text=valor, width=ancho, height=alto, font=("Helvetica", 15), command=lambda: self.click(valor, escribir))

    def click(self, texto, escribir):
        # Si el parámetro 'escribir' es true, el texto se debe mostrar en pantalla
        if not escribir:
            # Solo calcular si hay una operación y el usuario presiona "="
            if texto == "=" and self.operacion != "":
                # Reemplazar el valor unicode de la división por el operador division de Python "/"
                self.operacion = re.sub(u"\u00F7", "/", self.operacion)
                resultado = str(eval(self.operacion))
                self.operacion = ""
                self.limpiarPantalla()
                self.mostrarEnPantalla(resultado)
            elif texto == u"\u232B":
                # Si se presiona el botón de borrado, limpiar la pantalla
                self.operacion = ""
                self.limpiarPantalla()
        else:
            self.operacion += str(texto)
            self.mostrarEnPantalla(texto)

    # Borra el contenido de la pantalla
    def limpiarPantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0", tk.END)
        self.pantalla.configure(state="disabled")

    # Muestra en pantalla el contenido de las operaciones
    def mostrarEnPantalla(self, valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(tk.END, valor)
        self.pantalla.configure(state="disabled")


# Variables
ventana_principal = tk.Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()
