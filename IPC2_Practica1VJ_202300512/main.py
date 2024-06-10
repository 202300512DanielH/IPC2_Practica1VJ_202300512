from listaEnlazada import ListaEnlazada

def menu():
    lista = ListaEnlazada()
    while True:
        lista.imprimir_tareas()
        print("\n===========Menú===========")
        print("1. Agregar una nueva tarea")
        print("2. Marcar tarea como 'En progreso'")
        print("3. Terminar una tarea")
        print("4. Ver lista de tareas")
        print("5. Ver información")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("\nNombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            lista.agregar_tarea(nombre, descripcion)
        elif opcion == '2':
            id = int(input("\nID de la tarea: "))
            lista.marcar_en_progreso(id)
        elif opcion == '3':
            id = int(input("\nID de la tarea: "))
            lista.terminar_tarea(id)
        elif opcion == '4':
            lista.ver_lista()
        elif opcion == '5':
            lista.ver_informacion()
        elif opcion == '6':
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    menu()