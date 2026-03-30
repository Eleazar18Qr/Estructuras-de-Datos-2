"""
Módulo para la representación del juego Tres en Raya usando estructuras de Árbol.
Cumple con los requerimientos de la materia Estructuras de Datos 2.
"""


class Nodo:
    """
    Representa un estado específico del tablero de Tres en Raya.
    
    Atributos:
        _tablero (list): Matriz de 3x3 que contiene el estado del juego.
        _hijos (list): Lista de nodos que representan jugadas futuras.
    """

    def __init__(self, tablero=None):
        """
        Inicializa un nuevo nodo con un tablero dado o uno vacío.
        """
        if tablero is None:
            self._tablero = [[" " for _ in range(3)] for _ in range(3)]
        else:
            # Copia profunda manual para cumplir con PEP 8 y evitar efectos secundarios
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
        
        Args:
            fila (int): Índice de la fila (0-2).
            col (int): Índice de la columna (0-2).
            jugador (str): Carácter 'X' o 'O'.
            
        Returns:
            bool: True si la jugada fue exitosa, False si no.
        """
        if 0 <= fila <= 2 and 0 <= col <= 2:
            if self._tablero[fila][col] == " ":
                self._tablero[fila][col] = jugador
                return True
        return False

    def agregar_hijo(self, nodo_hijo):
        """Añade un nodo a la lista de estados sucesores."""
        self._hijos.append(nodo_hijo)


class ArbolJuego:
    """
    Clase que gestiona la raíz y el flujo de estados del juego.
    """

    def __init__(self):
        """Inicializa el árbol con un nodo raíz vacío."""
        self._raiz = Nodo()
        self._nodo_actual = self._raiz

    @property
    def nodo_actual(self):
        """Getter: Retorna el nodo donde se encuentra el juego actualmente."""
        return self._nodo_actual

    @nodo_actual.setter
    def nodo_actual(self, nuevo_nodo):
        """Setter: Permite mover el puntero del juego a un nuevo estado."""
        if isinstance(nuevo_nodo, Nodo):
            self._nodo_actual = nuevo_nodo

    def registrar_movimiento(self, nueva_matriz):
        """
        Crea un nuevo estado, lo vincula como hijo y avanza el juego.
        """
        nuevo_nodo = Nodo(nueva_matriz)
        self._nodo_actual.agregar_hijo(nuevo_nodo)
        self._nodo_actual = nuevo_nodo