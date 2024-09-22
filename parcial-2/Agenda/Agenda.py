import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox


class Agenda_personal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Agenda Personal")
        self.ventana.geometry("650x450")
        self.ventana.resizable(0, 0)
        self.ventana.config(bd="20")
        self.ventana.config(relief="sunken")
        self.ventana.config(bg="teal")

        # Frame para la lista de eventos
        frame_lista = tk.Frame(ventana)
        frame_lista.pack(pady=10)

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha",)
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para entrada de datos
        frame_entrada = tk.Frame(ventana)
        frame_entrada.pack(pady=10)
        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.hora_entry = tk.Entry(frame_entrada)
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.descripcion_entry = tk.Entry(frame_entrada)
        self.descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para botones
        frame_botones = tk.Frame(ventana)
        frame_botones.config(cursor="hand2")
        frame_botones.config(bg="Gray")
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side=tk.LEFT,
                                                                                                         padx=5)
        tk.Button(frame_botones, text="Salir", command=ventana.quit).pack(side=tk.LEFT, padx=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get_date().strftime("%Y-%m-%d")
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()
        self.tree.insert("", "end", values=(fecha, hora, descripcion))

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if seleccion:
            if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar el evento seleccionado?"):
                self.tree.delete(seleccion)
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = Agenda_personal(root)
    root.mainloop()