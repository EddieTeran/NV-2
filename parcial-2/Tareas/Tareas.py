import tkinter as tk
from tkinter import ttk


class ListaTareas:  # Nombre de la clase  ListaTareas
    def __init__(self, master):
        # Inicialización de la ventana principal
        self.master = master
        self.master.title("LISTA DE TAREAS")
        self.master.geometry("400x400")
        self.master.resizable(0, 0)
        self.master.config(bg="lightgray")
        self.master.config(bd=10)
        self.master.config(relief="solid")

        # Crear y configurar widgets
        # Entry para ingresar nuevas tareas
        self.task_entry = ttk.Entry(master, width=40)
        # Botón para añadir tareas
        self.add_button = ttk.Button(master, text="Añadir Tarea", command=self.add_task)
        # Botón para marcar tareas como completadas
        self.complete_button = ttk.Button(master, text="Marcar como Completada", command=self.mark_completed)
        # Botón para eliminar tareas
        self.delete_button = ttk.Button(master, text="Eliminar Tarea", command=self.delete_task)
        # Treeview para mostrar la lista de tareas
        self.task_list = ttk.Treeview(master, columns=("Task", "Status"), show="headings")

        # Configurar la lista de tareas
        self.task_list.heading("Task", text="Tarea")
        self.task_list.heading("Status", text="Estado")
        self.task_list.column("Task", width=150)
        self.task_list.column("Status", width=100)

        # Posicionar widgets en la ventana usando grid
        self.task_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.add_button.grid(row=0, column=1, padx=5, pady=5)
        self.complete_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.delete_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.task_list.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Configurar el peso de las filas y columnas para que se expandan correctamente
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        # Vincular eventos
        # Añadir tarea al presionar Enter
        self.task_entry.bind("<Return>", self.on_enter_pressed)
        # Marcar tarea como completada al hacer doble clic
        self.task_list.bind("<Double-1>", self.on_item_double_clicked)

    def add_task(self):
        # Obtener la tarea del entry y eliminar espacios en blanco
        task = self.task_entry.get().strip()
        if task:
            # Insertar la tarea en la lista con estado "Pendiente"
            self.task_list.insert("", "end", values=(task, "Pendiente"))
            # Limpiar el entry después de añadir la tarea
            self.task_entry.delete(0, "end")

    def mark_completed(self):
        # Obtener el item seleccionado
        selected_item = self.task_list.selection()
        if selected_item:
            # Obtener la tarea y su estado actual
            task = self.task_list.item(selected_item)["values"][0]
            current_status = self.task_list.item(selected_item)["values"][1]
            # Cambiar el estado: si está pendiente, marcar como completada y viceversa
            new_status = "Completada" if current_status == "Pendiente" else "Pendiente"
            # Actualizar el item en la lista
            self.task_list.item(selected_item, values=(task, new_status))

    def delete_task(self):
        # Obtener el item seleccionado
        selected_item = self.task_list.selection()
        if selected_item:
            # Eliminar el item de la lista
            self.task_list.delete(selected_item)

    def on_enter_pressed(self, event):
        # Llamar a add_task cuando se presiona Enter
        self.add_task()

    def on_item_double_clicked(self, event):
        # Llamar a mark_completed cuando se hace doble clic en un item
        self.mark_completed()


if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    # Inicializar la aplicación
    app = ListaTareas(root)
    # Iniciar el loop principal de la aplicación
    root.mainloop()