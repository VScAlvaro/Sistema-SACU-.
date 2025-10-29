# ==============================
# Sistema de Asignación de Cupos Universitarios
# Programación Orientada a Objetos (POO)
# ==============================

class Ciudadano:
    def __init__(self, cedula, nombre, edad):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        # Campos booleanos de las categorías
        self.cupo_aceptado_historico_pc = False
        self.cupo_historico_activo = False
        self.vulnerabilidad_socioeconomica = False
        self.merito_academico = False
        self.bachiller_pueblos_nacionalidad = False
        self.bachiller_periodo_academico = False
        self.poblacion_general = False

    def __str__(self):
        return f"{self.nombre} ({self.cedula}) - Edad: {self.edad}"


# === CLASES DE CATEGORÍAS ===

class CupoAceptadoHistoricoPC:
    def evaluar(self, ciudadano):
        ciudadano.cupo_aceptado_historico_pc = True


class CupoHistoricoActivo:
    def evaluar(self, ciudadano):
        ciudadano.cupo_historico_activo = True


class VulnerabilidadSocioeconomica:
    def evaluar(self, ciudadano):
        ciudadano.vulnerabilidad_socioeconomica = True


class MeritoAcademico:
    def evaluar(self, ciudadano):
        ciudadano.merito_academico = True


class BachillerPueblosNacionalidad:
    def evaluar(self, ciudadano):
        ciudadano.bachiller_pueblos_nacionalidad = True


class BachillerPeriodoAcademico:
    def evaluar(self, ciudadano):
        ciudadano.bachiller_periodo_academico = True


class PoblacionGeneral:
    def evaluar(self, ciudadano):
        ciudadano.poblacion_general = True


# === CONTROLADOR GENERAL ===

class SistemaAsignacionCupo:
    def __init__(self):
        self.ciudadanos = []

    def registrar_ciudadano(self):
        print("\n--- Registrar nuevo ciudadano ---")
        cedula = input("Cédula: ")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        nuevo = Ciudadano(cedula, nombre, edad)
        self.ciudadanos.append(nuevo)
        print(f"[OK] Ciudadano {nombre} registrado con éxito.\n")

    def asignar_cupo(self):
        if not self.ciudadanos:
            print("No hay ciudadanos registrados.\n")
            return

        print("\n--- Asignar categoría ---")
        for i, c in enumerate(self.ciudadanos):
            print(f"{i + 1}. {c}")

        indice = int(input("Seleccione el número del ciudadano: ")) - 1
        if indice < 0 or indice >= len(self.ciudadanos):
            print("Selección inválida.\n")
            return

        ciudadano = self.ciudadanos[indice]

        print("\nSeleccione la categoría:")
        categorias = [
            ("Cupo Aceptado Histórico PC", CupoAceptadoHistoricoPC),
            ("Cupo Histórico Activo", CupoHistoricoActivo),
            ("Vulnerabilidad Socioeconómica", VulnerabilidadSocioeconomica),
            ("Mérito Académico", MeritoAcademico),
            ("Bachiller Pueblos/Nacionalidad", BachillerPueblosNacionalidad),
            ("Bachiller Período Académico", BachillerPeriodoAcademico),
            ("Población General", PoblacionGeneral)
        ]

        for i, (nombre, _) in enumerate(categorias, start=1):
            print(f"{i}. {nombre}")

        opcion = int(input("Opción: ")) - 1

        if 0 <= opcion < len(categorias):
            clase_categoria = categorias[opcion][1]()
            clase_categoria.evaluar(ciudadano)
            print(f"[OK] {ciudadano.nombre} asignado a {categorias[opcion][0]}.\n")
        else:
            print("Opción inválida.\n")

    def mostrar_registro(self):
        print("\n--- Lista de Ciudadanos Registrados ---")
        if not self.ciudadanos:
            print("No hay registros aún.\n")
            return

        for c in self.ciudadanos:
            print(f"\n{c}")
            print(f"  Cupo aceptado histórico PC: {c.cupo_aceptado_historico_pc}")
            print(f"  Cupo histórico activo: {c.cupo_historico_activo}")
            print(f"  Vulnerabilidad socioeconómica: {c.vulnerabilidad_socioeconomica}")
            print(f"  Mérito académico: {c.merito_academico}")
            print(f"  Bachiller pueblos/nacionalidad: {c.bachiller_pueblos_nacionalidad}")
            print(f"  Bachiller período académico: {c.bachiller_periodo_academico}")
            print(f"  Población general: {c.poblacion_general}")
        print()  # línea vacía final

    def menu(self):
        while True:
            print("=== SISTEMA DE ASIGNACIÓN DE CUPOS UNIVERSITARIOS ===")
            print("1. Registrar ciudadano")
            print("2. Asignar categoría")
            print("3. Mostrar registros")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_ciudadano()
            elif opcion == "2":
                self.asignar_cupo()
            elif opcion == "3":
                self.mostrar_registro()
            elif opcion == "4":
                print("Saliendo del sistema... 👋")
                break
            else:
                print("Opción inválida.\n")


# === PROGRAMA PRINCIPAL ===

if __name__ == "__main__":
    sistema = SistemaAsignacionCupo()
    sistema.menu()
1 print jsjsjsjssjs