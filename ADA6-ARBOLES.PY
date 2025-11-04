import tkinter as tk
from tkinter import messagebox, simpledialog
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# --- CLASE ÁRBOL BINARIO DE BÚSQUEDA ---
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar(nodo.derecha, valor)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        return self._buscar(nodo.izquierda, valor) if valor < nodo.valor else self._buscar(nodo.derecha, valor)

    def inorden(self):
        return self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo is None:
            return []
        return self._inorden(nodo.izquierda) + [nodo.valor] + self._inorden(nodo.derecha)

# --- INTERFAZ GRÁFICA ---
class InterfazArbol(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Árbol Binario de Búsqueda")
        self.geometry("800x600")
        self.arbol = ArbolBinario()

        # Entrada y botones
        frame = tk.Frame(self)
        frame.pack(pady=10)
        tk.Label(frame, text="Valor:").pack(side="left")
        self.valor_entry = tk.Entry(frame, width=10)
        self.valor_entry.pack(side="left", padx=5)
        tk.Button(frame, text="Insertar", command=self.insertar).pack(side="left", padx=5)
        tk.Button(frame, text="Buscar", command=self.buscar).pack(side="left", padx=5)
        tk.Button(frame, text="InOrden", command=self.mostrar_inorden).pack(side="left", padx=5)
        tk.Button(frame, text="Limpiar Árbol", command=self.limpiar).pack(side="left", padx=5)

        # Canvas para dibujar el árbol
        self.canvas = tk.Canvas(self, bg="white", width=780, height=400)
        self.canvas.pack(pady=10)

        # Área de resultados
        self.texto = tk.Text(self, height=5, width=90)
        self.texto.pack(pady=5)

    def insertar(self):
        try:
            valor = int(self.valor_entry.get())
            if self.arbol.buscar(valor):
                messagebox.showinfo("Duplicado", f"El valor {valor} ya existe.")
            else:
                self.arbol.insertar(valor)
                self.mostrar_mensaje(f"Insertado: {valor}")
                self.dibujar()
            self.valor_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número entero.")

    def buscar(self):
        try:
            valor = int(simpledialog.askstring("Buscar", "Valor a buscar:"))
            existe = self.arbol.buscar(valor)
            msg = f"El valor {valor} {'SÍ está' if existe else 'NO está'} en el árbol."
            self.mostrar_mensaje(msg)
        except:
            pass

    def mostrar_inorden(self):
        lista = self.arbol.inorden()
        self.mostrar_mensaje("Recorrido InOrden:\n" + " -> ".join(map(str, lista)))

    def limpiar(self):
        self.arbol = ArbolBinario()
        self.canvas.delete("all")
        self.mostrar_mensaje("Árbol eliminado.")

    def mostrar_mensaje(self, texto):
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, texto)

    # --- Dibujo del árbol ---
    def dibujar(self):
        self.canvas.delete("all")
        if self.arbol.raiz:
            self._dibujar_nodo(self.arbol.raiz, 400, 50, 150)

    def _dibujar_nodo(self, nodo, x, y, sep):
        r = 20
        if nodo.izquierda:
            x_izq = x - sep
            y_izq = y + 70
            self.canvas.create_line(x, y, x_izq, y_izq)
            self._dibujar_nodo(nodo.izquierda, x_izq, y_izq, sep / 2)
        if nodo.derecha:
            x_der = x + sep
            y_der = y + 70
            self.canvas.create_line(x, y, x_der, y_der)
            self._dibujar_nodo(nodo.derecha, x_der, y_der, sep / 2)
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="#4DD0E1")
        self.canvas.create_text(x, y, text=str(nodo.valor), font=("Arial", 10, "bold"))

if __name__ == "__main__":
    app = InterfazArbol()
    app.mainloop()
