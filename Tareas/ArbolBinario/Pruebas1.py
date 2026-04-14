from collections import deque

class Nodo:
    """Representa la unidad básica de información en un árbol binario."""

    def __init__(self, dato):
        self._dato = dato
        self._izquierdo = None
        self._derecho = None

    @property
    def dato(self): return self._dato
    @dato.setter
    def dato(self, valor): self._dato = valor

    @property
    def izquierdo(self): return self._izquierdo
    @izquierdo.setter
    def izquierdo(self, nodo):
        if nodo is None or isinstance(nodo, Nodo):
            self._izquierdo = nodo
        else:
            raise TypeError("El hijo izquierdo debe ser de tipo Nodo")

    @property
    def derecho(self): return self._derecho
    @derecho.setter
    def derecho(self, nodo):
        if nodo is None or isinstance(nodo, Nodo):
            self._derecho = nodo
        else:
            raise TypeError("El hijo derecho debe ser de tipo Nodo")

class ArbolBinario:
    """Clase que gestiona la estructura y operaciones de un ABB."""

    def __init__(self):
        self.raiz = None

    def es_vacio(self):
        return self.raiz is None

    # --- INSERCIÓN ---
    def insertar_iterativo(self, dato):
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

    # --- BÚSQUEDA Y MÉTRICAS ---
    def buscar_iterativo(self, dato):
        actual = self.raiz
        while actual is not None and actual.dato != dato:
            actual = actual.izquierdo if dato < actual.dato else actual.derecho
        return actual

    def es_hoja(self, nodo):
        return nodo is not None and nodo.izquierdo is None and nodo.derecho is None

    def es_completo(self, nodo):
        """Verifica si un nodo tiene ambos hijos."""
        return nodo is not None and nodo.izquierdo is not None and nodo.derecho is not None

    def es_incompleto(self, nodo):
        """Verifica si un nodo tiene exactamente un hijo."""
        if nodo is None: return False
        tiene_uno = (nodo.izquierdo is not None) or (nodo.derecho is not None)
        return tiene_uno and not self.es_completo(nodo)

    def mostrar_arbol(self):
        print("\n--- Estructura Gráfica del Árbol ---")
        self._mostrar_recursivo(self.raiz, 0)
        print("------------------------------------")

    def _mostrar_recursivo(self, actual, nivel):
        if actual is not None:
            self._mostrar_recursivo(actual.derecho, nivel + 1)
            print("       " * nivel + f"|--[{actual.dato}]")
            self._mostrar_recursivo(actual.izquierdo, nivel + 1)

    # --- MÉTODOS DE ELIMINACIÓN  ---

    def _buscar_con_padre(self, dato):
        padre = None
        actual = self.raiz
        while actual is not None and actual.dato != dato:
            padre = actual
            actual = actual.izquierdo if dato < actual.dato else actual.derecho
        return padre, actual

    def encontrar_sucesor(self, nodo):
        actual = nodo.derecho
        while actual is not None and actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    def ejecutar_caso_1(self, dato):
        """Caso 1: Nodo Hoja."""
        padre, actual = self._buscar_con_padre(dato)
        if actual and self.es_hoja(actual):
            if padre is None: self.raiz = None
            elif padre.izquierdo == actual: padre.izquierdo = None
            else: padre.derecho = None
            return True
        return False

    def ejecutar_caso_2(self, dato):
        """Caso 2: Nodo Incompleto."""
        padre, actual = self._buscar_con_padre(dato)
        if actual and self.es_incompleto(actual):
            heredero = actual.izquierdo if actual.izquierdo else actual.derecho
            if padre is None: self.raiz = heredero
            elif padre.izquierdo == actual: padre.izquierdo = heredero
            else: padre.derecho = heredero
            return True
        return False

    def ejecutar_caso_3(self, dato):
        """Caso 3: Nodo Completo."""
        padre, actual = self._buscar_con_padre(dato)
        if actual and self.es_completo(actual):
            sucesor = self.encontrar_sucesor(actual)
            valor_sucesor = sucesor.dato
            # Eliminamos el sucesor de su posición original (será caso 1 o 2)
            self.ejecutar_caso_1(valor_sucesor) or self.ejecutar_caso_2(valor_sucesor)
            actual.dato = valor_sucesor
            return True
        return False

    # --- RECORRIDOS ---
    def in_orden(self, actual, resultado=None):
        if resultado is None: resultado = []
        if actual:
            self.in_orden(actual.izquierdo, resultado)
            resultado.append(actual.dato)
            self.in_orden(actual.derecho, resultado)
        return resultado

# --- PRUEBAS DE ELIMINACIÓN ---

def probar_eliminacion(arbol, valor):
    """Muestra didácticamente el proceso de eliminación."""
    print(f"\n>>> INTENTANDO ELIMINAR: {valor}")
    padre, nodo = arbol._buscar_con_padre(valor)
    
    if nodo is None: return

    if arbol.es_hoja(nodo):
        print(f"INFO: Aplicando CASO 1 (Hoja)")
        arbol.ejecutar_caso_1(valor)
    elif arbol.es_completo(nodo):
        print(f"INFO: Aplicando CASO 3 (Completo)")
        arbol.ejecutar_caso_3(valor)
    else:
        print(f"INFO: Aplicando CASO 2 (Incompleto)")
        arbol.ejecutar_caso_2(valor)
    
    arbol.mostrar_arbol()

def ejecutar_pruebas():
    arbol = ArbolBinario()
    datos = [100, 50, 150, 25, 75, 125, 175]
    for valor in datos: arbol.insertar_iterativo(valor)

    print("Visualización Inicial del Árbol:")
    arbol.mostrar_arbol()
    
    # Pruebas de los 3 casos
    probar_eliminacion(arbol, 25)   # Caso 1
    
    # Preparamos un caso 2: eliminamos el 175 para que el 150 sea incompleto
    arbol.ejecutar_caso_1(175)
    arbol.mostrar_arbol()
    print("\n(Se eliminó 175 para dejar al 150 con un solo hijo)")
    probar_eliminacion(arbol, 150)  # Caso 2
    
    probar_eliminacion(arbol, 100)  # Caso 3 (Raíz)

    print("\nIn-Orden Final:", arbol.in_orden(arbol.raiz))

if __name__ == "__main__":
    ejecutar_pruebas()