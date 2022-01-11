import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"\nOk {usuario[1]}! vamos a hacer una nueva nota... ")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\n Has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota ")

    def mostrar(self, usuario):
        print(f"\nOk,estas son tus notas {usuario[1]}\n")
        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.listar()
        for nota in notas:
            print("****************")
            print(nota[2])
            print(nota[3])
            print("****************")

    def borrar(self, usuario):
        print(f"\nOk {usuario[1]}!, vamos a borrar una nota\n")
        titulo = input("Introduce el titulo de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo, "")
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"\nHemos borrado la nota {titulo}")
        else:
            print("\nNo se ha borrado la nota, intentalo de nuevo...")
