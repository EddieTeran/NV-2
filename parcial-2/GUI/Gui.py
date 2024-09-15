import tkinter as tk

# Define la clase Application GUI
class ApplicationGUI:
    def __init__(self, root):
        # Inicializa la interfaz gráfica de la aplicación
        self.root = root
        root.title("Aplicacion GUI")  # Establece el título de la ventana
        self.root.resizable(0,0)  # Deshabilita el redimensionamiento de la ventana
        self.root.geometry("350x450")  # Establece el tamaño de la ventana
        self.root.config(bd="20")  # Establece el ancho del borde de la ventana
        self.root.config(relief="sunken")  # Establece el estilo del borde de la ventana
        self.root.config(bg="teal")  # Establece el color de fondo de la ventana

        # Crea componentes de la interfaz gráfica
        self.label_datos = tk.Label(root, text="Datos:")  # Crea una etiqueta
        self.label_datos.config(bg="Gray")  # Establece el color de fondo de la etiqueta
        self.label_datos.pack()  # Agrega la etiqueta a la ventana

        self.entry_datos = tk.Entry(root, width=20)  # Crea un campo de texto
        self.entry_datos.config(bg="cyan")  # Establece el color de fondo del campo de texto
        self.entry_datos.pack()  # Agrega el campo de texto a la ventana

        self.button_agregar = tk.Button(root, text="Agregar", command=self.agregar_datos)  # Crea un botón "Agregar"
        self.button_agregar.config(cursor="hand2")  # Establece la forma del cursor del botón
        self.button_agregar.config(bg="Gray")  # Establece el color de fondo del botón
        self.button_agregar.pack()  # Agrega el botón a la ventana

        self.button_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar_datos)  # Crea un botón "Limpiar"
        self.button_limpiar.config(cursor="hand2")  # Establece la forma del cursor del botón
        self.button_limpiar.config(bg="Gray")  # Establece el color de fondo del botón
        self.button_limpiar.pack()  # Agrega el botón a la ventana

        self.listbox_datos = tk.Listbox(root, width=60, height=20)  # Crea una lista
        self.listbox_datos.config(bg="Cyan")  # Establece el color de fondo de la lista
        self.listbox_datos.pack()  # Agrega la lista a la ventana

    def agregar_datos(self):
        # Obtiene el texto del campo de texto
        datos = self.entry_datos.get()
        if datos:
            # Agrega el texto a la lista
            self.listbox_datos.insert(tk.END, datos)
            # Limpia el campo de texto
            self.entry_datos.delete(0, tk.END)

    def limpiar_datos(self):
        # Limpia la lista
        self.listbox_datos.delete(0, tk.END)
        # Limpia el campo de texto
        self.entry_datos.delete(0, tk.END)

# Crea la instancia de la aplicación
root = tk.Tk()
app = ApplicationGUI(root)
root.mainloop()  # Inicia el bucle principal de la ap