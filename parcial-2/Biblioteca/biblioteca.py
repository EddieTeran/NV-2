class Libro: #definimos la clase libro
    def __init__(self, titulo, autor, categoria, isbn):
        #trupla para titulo y autor
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
class Usuario: # definimos la clase usuario
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # lista para gestionar libros
        self.libros_prestados = []
class Biblioteca:  # definimos la clase Biblioteca
    def __init__(self):
        # diccionario para libros
        self.libros = {}
        self.usuarios = set()
        self.usuarios_registrados = {}
    def agregar_libro(self, libro): # Método para agregar un libro
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
    def quitar_libro(self, isbn): # Método para quitar un libro
        if isbn in self.libros:
            del self.libros[isbn]
        else:
            print(f"No se encontró el libro con ISBN {isbn} en la biblioteca.")
    def registrar_usuario(self, usuario): # Método para registrar usuario
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            self.usuarios_registrados[usuario.id_usuario] = usuario
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
    def dar_de_baja_usuario(self, id_usuario): # Método para dar de baja a un usuario
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            del self.usuarios_registrados[id_usuario]
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")
    def prestar_libro(self, isbn, id_usuario):   # Método prestar un libro
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios_registrados[id_usuario]
            if libro not in usuario.libros_prestados:
                usuario.libros_prestados.append(libro)
                print(f"El libro {libro.titulo_autor[0]} ha sido prestado a {usuario.nombre}.")
            else:
                print(f"El usuario {usuario.nombre} ya tiene el libro {libro.titulo_autor[0]} prestado.")
        else:
            print(f"No se encontró el libro con ISBN {isbn} o el usuario con ID {id_usuario}.")
    def devolver_libro(self, isbn, id_usuario): # Método devolver libro
        if id_usuario in self.usuarios:
            usuario = self.usuarios_registrados[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    print(f"El libro {libro.titulo_autor[0]} ha sido devuelto por {usuario.nombre}.")
                    return
            print(f"El usuario {usuario.nombre} no tiene el libro {isbn} prestado.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")
    def buscar_libro(self, titulo=None, autor=None, categoria=None): # Método para buscar libro por título, autor o categoría
        resultados = []
        for libro in self.libros.values():
            if (titulo is None or libro.titulo_autor[0] == titulo) and \
               (autor is None or libro.titulo_autor[1] == autor) and \
               (categoria is None or libro.categoria == categoria):
                resultados.append(libro)
        return resultados
    def listar_libros_prestados(self, id_usuario): #Método para listar  libro prestado
        if id_usuario in self.usuarios:
            usuario = self.usuarios_registrados[id_usuario]
            return [libro.titulo_autor[0] for libro in usuario.libros_prestados]
        else:
            return []
    def mostrar_libros_disponibles(self): #Método para ver los libros disponibles
        disponibles = [libro for libro in self.libros.values() if libro not in [l for usuario in self.usuarios_registrados.values() for l in usuario.libros_prestados]]
        return [libro.titulo_autor[0] for libro in disponibles]
    def mostrar_usuarios_registrados(self):  #Método para mostrar los usuarios registrados
        return [usuario.nombre for usuario in self.usuarios_registrados.values()]
biblioteca = Biblioteca()
# bucle para interactuar con el usuario
while True:
    print("Bienvenido a la biblioteca!")
    print("""1. Agregar libro\n2. Quitar libro\n3. Registrar usuario\n4. Dar de baja usuario\n5. Prestar libro"
6. Devolver libro\n7. Buscar libro\n8. Listar libros prestados\n9. Mostrar libros disponibles
10. Mostrar usuarios registrados\n11. Salir""")
    opcion = input("Ingrese una opción: ")
    if opcion == "1": # agregar libro
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        categoria = input("Ingrese la categoría del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")
        libro = Libro(titulo, autor, categoria, isbn)
        biblioteca.agregar_libro(libro)
    elif opcion == "2": #Quitar libro
        isbn = input("Ingrese el ISBN del libro a quitar: ")
        biblioteca.quitar_libro(isbn)
    elif opcion == "3": # registrar usuario
        nombre = input("Ingrese el nombre del usuario: ")
        id_usuario = input("Ingrese el ID del usuario: ")
        usuario = Usuario(nombre, id_usuario)
        biblioteca.registrar_usuario(usuario)
    elif opcion == "4": #dar de baja usuario
        id_usuario = input("Ingrese el ID del usuario a dar de baja: ")
        biblioteca.dar_de_baja_usuario(id_usuario)
    elif opcion == "5":  # Prestar libro
        isbn = input("Ingrese el ISBN del libro a prestar: ")
        id_usuario = input("Ingrese el ID del usuario que presta el libro: ")
        biblioteca.prestar_libro(isbn, id_usuario)
    elif opcion == "6": # Devolver libro
        isbn = input("Ingrese el ISBN del libro a devolver: ")
        id_usuario = input("Ingrese el ID del usuario que devuelve el libro: ")
        biblioteca.devolver_libro(isbn, id_usuario)
    elif opcion == "7": # buscar libro
        titulo = input("Ingrese el título del libro a buscar (opcional): ")
        autor = input("Ingrese el autor del libro a buscar (opcional): ")
        categoria = input("Ingrese la categoría del libro a buscar (opcional): ")
        resultados = biblioteca.buscar_libro(titulo, autor, categoria)
        if resultados:
            print("Resultados de la búsqueda:")
            for libro in resultados:
                print(f"{libro.titulo_autor[0]} - {libro.titulo_autor[1]} - {libro.categoria} - {libro.isbn}")
        else:
            print("No se encontraron resultados.")
    elif opcion == "8": # Lista libros prestados
        id_usuario = input("Ingrese el ID del usuario para listar libros prestados: ")
        libros_prestados = biblioteca.listar_libros_prestados(id_usuario)
        if libros_prestados:
            print("Libros prestados:")
            for libro in libros_prestados:
                print(libro)
        else:
            print("No se encontraron libros prestados.")
    elif opcion == "9": #Mostrar libros disponibles
        disponibles = biblioteca.mostrar_libros_disponibles()
        if disponibles:
            print("Libros disponibles:")
            for libro in disponibles:
                print(libro)
        else:
            print("No se encontraron libros disponibles.")
    elif opcion == "10": #Mostrar usuarios registrados
        usuarios_registrados = biblioteca.mostrar_usuarios_registrados()
        if usuarios_registrados:
            print("Usuarios registrados:")
            for usuario in usuarios_registrados:
                print(usuario)
        else:
            print("No se encontraron usuarios registrados.")
    elif opcion == "11": #Salir bucle
        print("Gracias!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")