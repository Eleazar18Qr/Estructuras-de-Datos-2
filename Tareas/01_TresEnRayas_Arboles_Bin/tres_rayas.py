"""
Módulo para la representación del juego Tres en Raya usando estructuras de Árbol.
Desarrollado para la materia Estructuras de Datos 2.
Cumple con el estándar PEP 8 y programación orientada a objetos.
"""


class Nodo:
    """
    Representa un estado específico (un movimiento) en el tablero.
    
    Atributos:
        _tablero (list): Matriz de 3x3 que representa el estado del juego.
        _hijos (list): Lista de nodos que representan los siguientes movimientos.
    """

    def __init__(self, tablero=None):
        """Inicializa el nodo con un tablero dado o uno vacío."""
        if tablero is None:
            self._tablero = [[" " for _ in range(3)] for _ in range(3)]
        else:
            # Copia profunda para mantener la integridad de cada estado
            self._tablero = [fila[:] for fila in tablero]
        self._hijos = []

    @property
    def tablero(self):
        """Getter: Retorna la matriz 3x3 del estado actual."""
        return self._tablero

    @tablero.setter
    def tablero(self, nuevo_tablero):
        """Setter: Permite actualizar la matriz completa del nodo."""
        if len(nuevo_tablero) == 3 and len(nuevo_tablero[0]) == 3:
            self._tablero = [fila[:] for fila in nuevo_tablero]

    def establecer_jugada(self, fila, col, jugador):
        """
        Modifica una celda específica de la matriz.
        
        Returns:
            bool: True si la jugada fue exitosa, False si no.
        """
        if 0 <= fila <= 2 and 0 <= col <= 2:
            if self._tablero[fila][col] == " ":
                self._tablero[fila][col] = jugador
                return True
        return False

    def verificar_ganador(self):
        """
        Analiza el tablero en busca de una victoria o empate.
        
        Returns:
            str: 'X', 'O', 'Empate' o None si el juego continúa.
        """
        tab = self._tablero

        # Revisar Filas y Columnas
        for i in range(3):
            if tab[i][0] == tab[i][1] == tab[i][2] != " ":
                return tab[i][0]
            if tab[0][i] == tab[1][i] == tab[2][i] != " ":
                return tab[0][i]

        # Revisar Diagonales
        if tab[0][0] == tab[1][1] == tab[2][2] != " ":
            return tab[0][0]
        if tab[0][2] == tab[1][1] == tab[2][0] != " ":
            return tab[0][2]

        # Revisar si hay espacios vacíos
        for fila in tab:
            if " " in fila:
                return None
        return "Empate"

    def agregar_hijo(self, nodo_hijo):
        """Añade un estado sucesor a la lista de hijos."""
        self._hijos.append(nodo_hijo)


class ArbolJuego:
    """
    Gestiona la estructura jerárquica de los estados del juego.
    """

    def __init__(self):
        """Inicializa el árbol con un tablero vacío como raíz."""
        self._raiz = Nodo()
        self._nodo_actual = self._raiz

    @property
    def nodo_actual(self):
        """Getter: Retorna el estado actual del juego."""
        return self._nodo_actual

    @nodo_actual.setter
    def nodo_actual(self, nuevo_nodo):
        """Setter: Actualiza el puntero al estado actual del juego."""
        if isinstance(nuevo_nodo, Nodo):
            self._nodo_actual = nuevo_nodo

    def registrar_movimiento(self, nueva_matriz):
        """Crea un nuevo nodo, lo vincula y avanza el juego."""
        nuevo_nodo = Nodo(nueva_matriz)
        self._nodo_actual.agregar_hijo(nuevo_nodo)
        self._nodo_actual = nuevo_nodo


def mostrar_interfaz(tablero):
    """Dibuja el tablero en la consola de forma estética."""
    print("\n" + "  0   1   2")
    for i, fila in enumerate(tablero):
        print(f"{i} {' | '.join(fila)}")
        if i < 2:
            print("  ---------")


def jugar():
    """Bucle principal de ejecución del juego."""
    juego = ArbolJuego()
    jugador_actual = "X"

    print("=== TRES EN RAYA: ESTRUCTURAS DE DATOS ===")

    while True:
        mostrar_interfaz(juego.nodo_actual.tablero)
        
        # Verificar estado del juego
        resultado = juego.nodo_actual.verificar_ganador()
        if resultado:
            if resultado == "Empate":
                print("\n¡Es un EMPATE!")
            else:
                print(f"\n¡Felicidades! El jugador '{resultado}' ha GANADO.")
            break

        print(f"\nTurno de: {jugador_actual}")
        try:
            f = int(input("Ingrese fila (0-2): "))
            c = int(input("Ingrese columna (0-2): "))

            if juego.nodo_actual.establecer_jugada(f, c, jugador_actual):
                # Guardamos el estado en el árbol y avanzamos
                juego.registrar_movimiento(juego.nodo_actual.tablero)
                jugador_actual = "O" if jugador_actual == "X" else "X"
            else:
                print(">> Error: Casilla ocupada o fuera de rango.")
        except ValueError:
            print(">> Error: Por favor, ingrese números válidos.")


if __name__ == "__main__":
    jugar()