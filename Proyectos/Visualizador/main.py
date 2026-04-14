from model import BinaryTree
from view import TreeView
from controller import TreeController

def main():
    # Inicialización de componentes MVC
    model = BinaryTree()
    view = TreeView()
    app = TreeController(model, view)
    
    # Ejecución del loop principal
    view.mainloop()

if __name__ == "__main__":
    main()