import unittest

class Contacto:
    """Representa la información personal de un cliente."""
    def __init__(self, nombre, telefono, email, direccion):
        """Inicializa los atributos del contacto."""
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    def __str__(self):
        """Representación amigable del objeto para la interfaz."""
        return (f"Nombre: {self.nombre} | Tel: {self.telefono} | "
                f"Email: {self.email} | Dir: {self.direccion}")

class Agenda:
    """Gestiona la colección de contactos mediante diccionarios y listas."""
    def __init__(self):
        self.contactos = {}

    def registrar_contacto(self, nombre, telefono, email, direccion):
        """Agrega un nuevo contacto al sistema."""
        if nombre in self.contactos:
            return False, "Error: El nombre ya está registrado."
        nuevo = Contacto(nombre, telefono, email, direccion)
        self.contactos[nombre] = nuevo
        return True, f"Contacto '{nombre}' registrado con éxito."

    def buscar_contacto(self, criterio):
        """Busca por nombre o número de teléfono."""
        encontrados = []
        for c in self.contactos.values():
            if criterio.lower() in c.nombre.lower() or criterio in c.telefono:
                encontrados.append(c)
        return encontrados

    def editar_contacto(self, nombre, nuevo_tel=None, nuevo_mail=None, nueva_dir=None):
        """Modifica la información de un contacto existente."""
        if nombre in self.contactos:
            if nuevo_tel: self.contactos[nombre].telefono = nuevo_tel
            if nuevo_mail: self.contactos[nombre].email = nuevo_mail
            if nueva_dir: self.contactos[nombre].direccion = nueva_dir
            return True
        return False

    def eliminar_contacto(self, nombre):
        """Elimina un registro de la base de datos."""
        if nombre in self.contactos:
            del self.contactos[nombre]
            return True
        return False

def mostrar_menu():
    mi_agenda = Agenda()
    while True:
        print("\n--- GESTIÓN DE CONTACTOS V2.0 ---")
        print("1. Registrar  2. Buscar  3. Editar  4. Eliminar  5. Listar  6. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\nPrecione 0 para regresar al menú")
            n = input("Nombre: ")
            if n == "0": continue
            t = input("Teléfono: ")
            e = input("Email: ")
            d = input("Dirección: ")
            exito, msg = mi_agenda.registrar_contacto(n, t, e, d)
            print(msg)

        elif opcion == "2":
            print("\nPrecione 0 para regresar al menú")
            criterio = input("Ingrese nombre o teléfono a buscar: ")
            resultados = mi_agenda.buscar_contacto(criterio)
            if resultados:
                for r in resultados: print(r)
            else: print("Sin coincidencias.")

        elif opcion == "3":
            print("\nPrecione 0 para regresar al menú")
            n = input("Nombre del contacto a editar: ")
            if n == "0": continue
            print("Deje en blanco para no modificar.")
            t = input("Nuevo Teléfono: ")
            e = input("Nuevo Email: ")
            d = input("Nueva Dirección: ")
            if mi_agenda.editar_contacto(n, t or None, e or None, d or None):
                print("Actualizado correctamente.")
            else: print("Contacto no encontrado.")

        elif opcion == "4":
            print("\nPrecione 0 para regresar al menú")
            n = input("Nombre del contacto a eliminar: ")
            if mi_agenda.eliminar_contacto(n): print("Eliminado.")
            else: print("No existe.")

        elif opcion == "5":
            if not mi_agenda.contactos: print("Agenda vacía.")
            else:
                for c in mi_agenda.contactos.values(): print(c)

        elif opcion == "6":
            print("Cerrando sistema...")
            break

class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()
    
    def test_registro(self):
        exito, msg = self.agenda.registrar_contacto("Test", "123", "a@a.com", "Calle 1")
        self.assertTrue(exito)
        self.assertIn("Test", self.agenda.contactos)

    def test_busqueda(self):
        self.agenda.registrar_contacto("Juan", "999", "j@mail.com", "Dir")
        res = self.agenda.buscar_contacto("999")
        self.assertEqual(len(res), 1)

if __name__ == "__main__":
    mostrar_menu()