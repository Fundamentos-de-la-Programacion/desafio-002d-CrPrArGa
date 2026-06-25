lista_libros = []

def mostrar_menu():
    print("Menu")
    print("1.- Agregar libro")
    print("2.- Buscar libro")
    print("3.- Eliminar libro")
    print("4.- Actualizar disponibilidad")
    print("5.- Mostrar libros")
    print("6.- Salir")

def opcion_menu(opcion):
    while True:
        if opcion_menu in ["1", "2", "3", "4", "5", "6"]:
            return int(opcion)
        print("Error elija una opción valida")

def validar_titulo(nombre):
    return len(nombre.strip()) >= 0

def validar_copias(cant_str):
    if cant_str.isdigit():
        return cant_str()
    return False

def validar_prestamo(prestamo_str):
    if prestamo_str.isdigit():
        return prestamo_str()
    print("Error los días deben ser mayor a 0")
    

def agregar_libro(lista):
    titulo = input("Ingrese el titulo del libro: ")
    copias = input("Ingrese las copias del libro: ")
    periodo = input("Ingrese el periodo de prestamo (días): ")
    if not validar_titulo(titulo):
        print("Error ingrese titulo valido")
        return
    if not validar_copias(copias):
        print("Error las copias deben ser mayor o igual 0")
        return
    if not validar_prestamo(periodo):
        print("Error los días deben ser mayor a 0")
        return
    
    nuevo_libro = {
        "titulo": titulo.strip(),
        "copias": int(copias),
        "prestamo": int(periodo),
    }

def buscar_libro(lista, titulo_buscar):
    for i in range(lista_libros):
        if lista[i]['titulo'].lower() == titulo_buscar.strip().lower():
            return i
    return -1

        
def eliminar_libro(titulo):
    titulo_eliminar = input("Ingrese el titulo que desea eliminar")


    print(f"El libro '{titulo}' no se encuentra registrado")

def actualizar_dispo(lista):
    for est in lista:
        if est["copias"] >= 0:
            est["disponible"] = True
        else:
            est["disponible"] = False


def mostrar_libros(lista):
    actualizar_dispo(lista)

    if not lista:
        print("No hay titulos")
        return

    for est in lista:
        diponibilidad = "DISPONIBLE" if est["disponible"] else "NO DIPONIBLE"
        print(f"Titulo: est[{titulo}]")
        print(f"Copias: est[{copias}]")
        print(f"disponible")


def programa_principal():
    while True:
        opcion = input("Elija una opcion: ")
        if opcion == 1:
           agregar_libro(lista_libros) 
        elif opcion == 2:
            buscar_libro(lista_libros)
        elif opcion == 3:
            eliminar_libro(lista_libros)
        elif opcion == 4:
            actualizar_dispo(lista_libros)
        elif opcion == 5:
            mostrar_libros(lista_libros)
        elif opcion == 6:
            print("“Gracias por usar el sistema. Vuelva Pronto”")
            break

if __name__ == "__main__":
    programa_principal()