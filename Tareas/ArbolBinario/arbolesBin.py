from collections import deque

class Nodo:
    """
    Representa la unidad básica de información en un árbol binario.

    Esta clase implementa el TDA Nodo utilizando encapsulamiento para
    proteger las referencias a sus descendientes.
    """

    def __init__(self, dato):
        """
        Inicializa un nuevo nodo con un valor específico.

        Args:
            dato: El valor que almacenará el nodo.
        """
        self._dato = dato
        self._izquierdo = None
        self._derecho = None

    @property
    def dato(self):
        """Obtiene el valor almacenado en el nodo."""
        return self._dato

    @dato.setter
    def dato(self, valor):
        """Establece un nuevo valor para el nodo."""
        self._dato = valor

    @property
    def izquierdo(self):
        """Obtiene la referencia al hijo izquierdo."""
        return self._izquierdo

    @izquierdo.setter
    def izquierdo(self, nodo):
        """
        Establece la referencia al hijo izquierdo validando el tipo.

        Args:
            nodo (Nodo): Instancia de tipo Nodo o None.
        """
        if nodo is None or isinstance(nodo, Nodo):
            self._izquierdo = nodo
        else:
            raise TypeError("El hijo izquierdo debe ser de tipo Nodo")

    @property
    def derecho(self):
        """Obtiene la referencia al hijo derecho."""
        return self._derecho

    @derecho.setter
    def derecho(self, nodo):
        """
        Establece la referencia al hijo derecho validando el tipo.

        Args:
            nodo (Nodo): Instancia de tipo Nodo o None.
        """
        if nodo is None or isinstance(nodo, Nodo):
            self._derecho = nodo
        else:
            raise TypeError("El hijo derecho debe ser de tipo Nodo")

class ArbolBinario:
    """
    Clase que gestiona la estructura y operaciones de un Árbol Binario de Búsqueda.

    Proporciona métodos tanto recursivos como iterativos para manipulación
    y análisis de la jerarquía de datos.
    """

    def __init__(self):
        """Inicializa un árbol binario vacío."""
        self.raiz = None

    def es_vacio(self):
        """Verifica si el árbol no contiene nodos."""
        return self.raiz is None

    # --- MÉTODOS DE INSERCIÓN ---

    def insertar_recursivo(self, dato):
        """Inserta un valor usando la pila de llamadas del sistema."""
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar_recursiva_logica(self.raiz, dato)

    def _insertar_recursiva_logica(self, actual, dato):
        """Lógica privada de soporte para la inserción recursiva."""
        if dato < actual.dato:
            if actual.izquierdo is None:
                actual.izquierdo = Nodo(dato)
            else:
                self._insertar_recursiva_logica(actual.izquierdo, dato)
        else:
            if actual.derecho is None:
                actual.derecho = Nodo(dato)
            else:
                self._insertar_recursiva_logica(actual.derecho, dato)

    def insertar_iterativo(self, dato):
        """Inserta un valor navegando el árbol mediante un bucle while."""
        nuevo_nodo = Nodo(dato)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return

        actual = self.raiz
        while True:
            padre = actual
            if dato < actual.dato:
                actual = actual.izquierdo
                if actual is None:
                    padre.izquierdo = nuevo_nodo
                    return
            else:
                actual = actual.derecho
                if actual is None:
                    padre.derecho = nuevo_nodo
                    return

    # --- MÉTODOS DE BÚSQUEDA ---

    def buscar_recursivo(self, dato):
        """Busca un valor de forma recursiva (Divide y Vencerás)."""
        return self._buscar_recursiva_logica(self.raiz, dato)

    def _buscar_recursiva_logica(self, actual, dato):
        if actual is None or actual.dato == dato:
            return actual
        if dato < actual.dato:
            return self._buscar_recursiva_logica(actual.izquierdo, dato)
        return self._buscar_recursiva_logica(actual.derecho, dato)

    def buscar_iterativo(self, dato):
        """Busca un valor recorriendo el árbol con un puntero móvil."""
        actual = self.raiz
        while actual is not None and actual.dato != dato:
            if dato < actual.dato:
                actual = actual.izquierdo
            else:
                actual = actual.derecho
        return actual

    # --- MÉTRICAS ---

    def cantidad_recursivo(self):
        """Calcula el total de nodos sumando subárboles recursivamente."""
        return self._contar_recursivo(self.raiz)

    def _contar_recursivo(self, actual):
        if actual is None:
            return 0
        return 1 + self._contar_recursivo(actual.izquierdo) + self._contar_recursivo(actual.derecho)

    def cantidad_iterativo(self):
        """Calcula el total de nodos usando una pila (Stack) manual."""
        if self.raiz is None:
            return 0
        contador = 0
        pila = [self.raiz]
        while pila:
            nodo = pila.pop()
            contador += 1
            if nodo.derecho: pila.append(nodo.derecho)
            if nodo.izquierdo: pila.append(nodo.izquierdo)
        return contador

    def altura_recursivo(self):
        """Retorna la altura máxima basada en la profundidad de las ramas."""
        return self._altura_logica(self.raiz)

    def _altura_logica(self, actual):
        if actual is None:
            return 0
        return 1 + max(self._altura_logica(actual.izquierdo),
                       self._altura_logica(actual.derecho))

    def altura_iterativo(self):
        """Calcula la altura recorriendo nivel por nivel (BFS)."""
        if self.raiz is None:
            return 0
        altura = 0
        cola = deque([self.raiz])
        while cola:
            altura += 1
            for _ in range(len(cola)):
                nodo = cola.popleft()
                if nodo.izquierdo: cola.append(nodo.izquierdo)
                if nodo.derecho: cola.append(nodo.derecho)
        return altura

    def es_hoja(self, nodo):
        """Verifica si el nodo proporcionado no tiene descendientes."""
        return nodo is not None and nodo.izquierdo is None and nodo.derecho is None

    def amplitud(self):
        """Retorna una lista con los valores del árbol por niveles."""
        if self.raiz is None:
            return []
        resultado = []
        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.dato)
            if nodo.izquierdo: cola.append(nodo.izquierdo)
            if nodo.derecho: cola.append(nodo.derecho)
        return resultado

    def mostrar_arbol(self):
        """
        Muestra la estructura del árbol de forma gráfica en la consola.
        Gira el árbol 90 grados a la izquierda para una mejor visualización.
        """
        print("\n--- Estructura Gráfica del Árbol ---")
        self._mostrar_recursivo(self.raiz, 0)
        print("------------------------------------\n")

    def _mostrar_recursivo(self, actual, nivel):
        """Lógica auxiliar para imprimir el árbol con sangrías."""
        if actual is not None:
            # Primero recorremos el lado derecho (se verá arriba)
            self._mostrar_recursivo(actual.derecho, nivel + 1)

            # Imprimimos el nodo actual con espacios según su nivel
            print("       " * nivel + f"|--[{actual.dato}]")

            # Luego recorremos el lado izquierdo (se verá abajo)
            self._mostrar_recursivo(actual.izquierdo, nivel + 1)
    
    # --- RECORRIDOS EN PROFUNDIDAD (DFS) ---

    def pre_orden(self, actual, resultado=None):
        """
        Recorre el árbol en orden: Raíz -> Izquierda -> Derecha.
        Ideal para crear una copia del árbol.
        """
        if resultado is None:
            resultado = []
        if actual:
            resultado.append(actual.dato)        # 1. Raíz
            self.pre_orden(actual.izquierdo, resultado)  # 2. Izquierda
            self.pre_orden(actual.derecho, resultado)    # 3. Derecha
        return resultado

    def in_orden(self, actual, resultado=None):
        """
        Recorre el árbol en orden: Izquierda -> Raíz -> Derecha.
        En un BST, los elementos se obtienen en orden ascendente.
        """
        if resultado is None:
            resultado = []
        if actual:
            self.in_orden(actual.izquierdo, resultado)   # 1. Izquierda
            resultado.append(actual.dato)        # 2. Raíz
            self.in_orden(actual.derecho, resultado)     # 3. Derecha
        return resultado

    def post_orden(self, actual, resultado=None):
        """
        Recorre el árbol en orden: Izquierda -> Derecha -> Raíz.
        Útil para eliminar nodos o calcular el tamaño de subárboles.
        """
        if resultado is None:
            resultado = []
        if actual:
            self.post_orden(actual.izquierdo, resultado) # 1. Izquierda
            self.post_orden(actual.derecho, resultado)   # 2. Derecha
            resultado.append(actual.dato)        # 3. Raíz
        return resultado

# --- EVALUACIÓN DE MÉTODOS RECURSIVOS E ITERATIVOS ---

def ejecutar_pruebas():
    # 1. Instanciación
    arbol = ArbolBinario()
    datos = [100, 50, 150, 25, 75, 125, 175]

    # 2. Inserción (Probamos el iterativo)
    for valor in datos:
        arbol.insertar_iterativo(valor)

    # --- AQUÍ COLOCAMOS EL MÉTODO GRÁFICO ---
    print("\nVisualización del Árbol:")
    arbol.mostrar_arbol()
    # ----------------------------------------

    print("--- RESULTADOS DEL ÁRBOL ---")
    print(f"Amplitud (Niveles): {arbol.amplitud()}")

    # Comparación de Cantidad
    cant_rec = arbol.cantidad_recursivo()
    cant_ite = arbol.cantidad_iterativo()
    print(f"Cantidad -> Rec: {cant_rec} | Ite: {cant_ite}")

    # Comparación de Altura
    alt_rec = arbol.altura_recursivo()
    alt_ite = arbol.altura_iterativo()
    print(f"Altura   -> Rec: {alt_rec} | Ite: {alt_ite}")

    # Prueba de Búsqueda Iterativa
    nodo_buscado = arbol.buscar_iterativo(75)
    if nodo_buscado:
        print(f"\nNodo 75 encontrado. ¿Es hoja?: {arbol.es_hoja(nodo_buscado)}")
    
    # --- EJECUCIÓN DE RECORRIDOS DFS (Profundidad) ---
    print("\n--- RECORRIDOS EN PROFUNDIDAD ---")
    
    # 1. Pre-Orden (Raíz - Izq - Der)
    pre = arbol.pre_orden(arbol.raiz)
    print(f"Pre-Orden  : {pre}")
    
    # 2. In-Orden (Izq - Raíz - Der) -> Debería salir ordenado de menor a mayor
    ino = arbol.in_orden(arbol.raiz)
    print(f"In-Orden   : {ino}")
    
    # 3. Post-Orden (Izq - Der - Raíz)
    pos = arbol.post_orden(arbol.raiz)
    print(f"Post-Orden : {pos}")

if __name__ == "__main__":
    ejecutar_pruebas()