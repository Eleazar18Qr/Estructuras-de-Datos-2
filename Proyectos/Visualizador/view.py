import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional, Callable

class TreeView(tk.Tk):
    """Clase encargada de la representación visual (GUI)."""
    def __init__(self):
        super().__init__()
        self.title("Software Engineer - Binary Tree Visualizer")
        self.geometry("1000x700")
        self.configure(bg="#f0f0f0")

        self._setup_ui()

    def _setup_ui(self):
        # Panel Lateral de Control
        self.sidebar = tk.Frame(self, width=250, bg="#2c3e50", padx=10, pady=10)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(self.sidebar, text="Configuración Nodo", fg="white", bg="#2c3e50", font=('Arial', 12, 'bold')).pack(pady=10)

        # Entradas
        self.val_entry = self._create_input("Valor del Nodo:")
        self.parent_entry = self._create_input("Valor del Padre (vacío si es raíz):")
        
        tk.Label(self.sidebar, text="Lado (L/R):", fg="white", bg="#2c3e50").pack()
        self.side_var = tk.StringVar(value="L")
        ttk.Combobox(self.sidebar, textvariable=self.side_var, values=["L", "R"], state="readonly").pack(pady=5)

        # Botones
        self.btn_insert = tk.Button(self.sidebar, text="Insertar Nodo", bg="#27ae60", fg="white")
        self.btn_insert.pack(fill=tk.X, pady=10)

        self.btn_load = tk.Button(self.sidebar, text="Cargar JSON", bg="#2980b9", fg="white")
        self.btn_load.pack(fill=tk.X, pady=5)

        self.btn_clear = tk.Button(self.sidebar, text="Limpiar Árbol", bg="#e74c3c", fg="white")
        self.btn_clear.pack(fill=tk.X, pady=5)

        # Área de Recorridos
        self.txt_traversal = tk.Text(self.sidebar, height=10, width=25, font=('Consolas', 9))
        self.txt_traversal.pack(pady=20)

        # Canvas de Visualización
        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def _create_input(self, label_text: str) -> tk.Entry:
        tk.Label(self.sidebar, text=label_text, fg="white", bg="#2c3e50").pack()
        entry = tk.Entry(self.sidebar)
        entry.pack(fill=tk.X, pady=5)
        return entry

    def draw_node(self, x: float, y: float, value: str):
        radius = 20
        self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="#ecf0f1", outline="#34495e", width=2)
        self.canvas.create_text(x, y, text=value, font=('Arial', 10, 'bold'))

    def draw_line(self, x1: float, y1: float, x2: float, y2: float):
        self.canvas.create_line(x1, y1, x2, y2, fill="#7f8c8d", width=2)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.txt_traversal.delete('1.0', tk.END)