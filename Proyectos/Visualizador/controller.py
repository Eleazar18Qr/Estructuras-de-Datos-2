import json
from typing import Optional
from model import BinaryTree, Node
from view import TreeView

class TreeController:
    """Clase que coordina la interacción entre el Modelo y la Vista."""
    def __init__(self, model: BinaryTree, view: TreeView):
        self.model = model
        self.view = view
        
        # Vincular eventos
        self.view.btn_insert.config(command=self.handle_insert)
        self.view.btn_clear.config(command=self.handle_clear)
        self.view.btn_load.config(command=self.handle_load_json)

    def handle_insert(self):
        val = self.view.val_entry.get()
        parent = self.view.parent_entry.get() or None
        side = self.view.side_var.get()

        if val:
            success = self.model.insert(val, parent, side)
            if success:
                self.update_display()
            else:
                import tkinter.messagebox as mb
                mb.showerror("Error", "No se pudo insertar. Verifique el padre o si el lugar está ocupado.")

    def handle_clear(self):
        self.model.clear()
        self.update_display()

    def handle_load_json(self):
        # Ejemplo de formato esperado: [{"val": "10", "p": null, "s": null}, {"val": "5", "p": "10", "s": "L"}]
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                self.model.clear()
                for item in data:
                    self.model.insert(item['val'], item.get('p'), item.get('s'))
            self.update_display()
        except Exception as e:
            import tkinter.messagebox as mb
            mb.showerror("Error de Archivo", f"No se pudo cargar: {e}")

    def update_display(self):
        self.view.clear_canvas()
        if self.model.root:
            self._render_tree(self.model.root, 500, 50, 200)
            
            # Actualizar recorridos
            pre = self.model.get_preorder(self.model.root, [])
            ino = self.model.get_inorder(self.model.root, [])
            post = self.model.get_postorder(self.model.root, [])
            
            self.view.txt_traversal.insert('end', f"PRE: {' '.join(pre)}\n\n")
            self.view.txt_traversal.insert('end', f"IN:  {' '.join(ino)}\n\n")
            self.view.txt_traversal.insert('end', f"POST: {' '.join(post)}")

    def _render_tree(self, node: Node, x: float, y: float, offset: float):
        """Algoritmo recursivo para posicionar nodos en el Canvas."""
        if node.left:
            self.view.draw_line(x, y, x - offset, y + 60)
            self._render_tree(node.left, x - offset, y + 60, offset / 1.7)
            
        if node.right:
            self.view.draw_line(x, y, x + offset, y + 60)
            self._render_tree(node.right, x + offset, y + 60, offset / 1.7)
            
        self.view.draw_node(x, y, node.value)