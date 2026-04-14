from typing import Optional, List

class Node:
    """Clase que representa un nodo individual en el árbol binario."""
    def __init__(self, value: str):
        self.value: str = value
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

class BinaryTree:
    """Clase que gestiona la lógica de la estructura de datos del árbol."""
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, value: str, parent_value: Optional[str] = None, side: Optional[str] = None) -> bool:
        """
        Inserta un nodo. Si no hay raíz, el primer nodo se convierte en ella.
        Si hay padre, lo busca y asigna el hijo según el lado ('L' o 'R').
        """
        new_node = Node(value)
        
        # Caso 1: El árbol está vacío, el primer nodo es la raíz
        if not self.root:
            self.root = new_node
            return True
        
        # Caso 2: Buscar el nodo padre para insertar el hijo
        parent_node = self.find_node(self.root, parent_value)
        if parent_node:
            if side == 'L' and not parent_node.left:
                parent_node.left = new_node
                return True
            elif side == 'R' and not parent_node.right:
                parent_node.right = new_node
                return True
        return False

    def find_node(self, current: Optional[Node], value: str) -> Optional[Node]:
        """Busca un nodo por su valor de forma recursiva."""
        if not current:
            return None
        if current.value == value:
            return current
        
        left_search = self.find_node(current.left, value)
        if left_search:
            return left_search
            
        return self.find_node(current.right, value)

    def get_preorder(self, node: Optional[Node], res: List[str]) -> List[str]:
        if node:
            res.append(node.value)
            self.get_preorder(node.left, res)
            self.get_preorder(node.right, res)
        return res

    def get_inorder(self, node: Optional[Node], res: List[str]) -> List[str]:
        if node:
            self.get_inorder(node.left, res)
            res.append(node.value)
            self.get_inorder(node.right, res)
        return res

    def get_postorder(self, node: Optional[Node], res: List[str]) -> List[str]:
        if node:
            self.get_postorder(node.left, res)
            self.get_postorder(node.right, res)
            res.append(node.value)
        return res

    def clear(self) -> None:
        """Reinicia el árbol."""
        self.root = None