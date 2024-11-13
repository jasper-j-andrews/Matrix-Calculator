import tkinter as tk
from tkinter import messagebox

from determinant_calculator import determinant  # Assuming function name is `determinant`
from matrix_multiplication import multiply  # Using the provided `calculate_product`

class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")
        
        # Mode selection: Determinant or Matrix Product
        self.mode = tk.StringVar(value="determinant")
        self.det_radio = tk.Radiobutton(root, text="Calculate Determinant", variable=self.mode, value="determinant", command=self.update_mode)
        self.det_radio.grid(row=0, column=0, padx=5, pady=5)
        self.prod_radio = tk.Radiobutton(root, text="Multiply Matrices", variable=self.mode, value="product", command=self.update_mode)
        self.prod_radio.grid(row=0, column=1, padx=5, pady=5)
        
        # Matrix size inputs
        self.size_label = tk.Label(root, text="Enter size (n for nxn):")
        self.size_label.grid(row=1, column=0, padx=5, pady=5)
        self.size_entry = tk.Entry(root, width=5)
        self.size_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.m_label = tk.Label(root, text="Enter m:")
        self.m_entry = tk.Entry(root, width=5)
        self.n_label = tk.Label(root, text="Enter n:")
        self.n_entry = tk.Entry(root, width=5)
        self.q_label = tk.Label(root, text="Enter q:")
        self.q_entry = tk.Entry(root, width=5)
        
        # Generate button
        self.generate_button = tk.Button(root, text="Generate Matrix", command=self.generate_matrix_inputs)
        self.generate_button.grid(row=1, column=2, padx=5, pady=5)
        
        # Matrix entries for input
        self.matrix_entries = []
        self.matrix_entries_2 = []
        
        # Result display
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=10, column=0, columnspan=3, pady=10)
        
    def clear_inputs(self):
        """Clear all matrix inputs, buttons, and labels."""
        for entry_row in self.matrix_entries + self.matrix_entries_2:
            for entry in entry_row:
                entry.destroy()
        
        self.matrix_entries = []
        self.matrix_entries_2 = []
        
        if hasattr(self, 'det_button'):
            self.det_button.destroy()
        if hasattr(self, 'prod_button'):
            self.prod_button.destroy()
        
        self.result_label.config(text="")

    def update_mode(self):
        self.clear_inputs()  # Clear previous inputs and buttons
        
        if self.mode.get() == "determinant":
            # Show only determinant size input
            self.size_label.grid()
            self.size_entry.grid()
            self.m_label.grid_remove()
            self.m_entry.grid_remove()
            self.n_label.grid_remove()
            self.n_entry.grid_remove()
            self.q_label.grid_remove()
            self.q_entry.grid_remove()
        elif self.mode.get() == "product":
            # Show m, n, q inputs
            self.size_label.grid_remove()
            self.size_entry.grid_remove()
            self.m_label.grid(row=1, column=0)
            self.m_entry.grid(row=1, column=1)
            self.n_label.grid(row=2, column=0)
            self.n_entry.grid(row=2, column=1)
            self.q_label.grid(row=3, column=0)
            self.q_entry.grid(row=3, column=1)
    
    def generate_matrix_inputs(self):
        self.clear_inputs()  # Clear previous inputs and buttons
        
        if self.mode.get() == "determinant":
            try:
                n = int(self.size_entry.get())
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid integer for n.")
                return
            
            # Create matrix input fields
            self.matrix_entries = []
            for i in range(n):
                row_entries = []
                for j in range(n):
                    entry = tk.Entry(self.root, width=5)
                    entry.grid(row=i+4, column=j, padx=2, pady=2)
                    row_entries.append(entry)
                self.matrix_entries.append(row_entries)
            
            # Button for determinant calculation
            self.det_button = tk.Button(self.root, text="Calculate Determinant", command=self.calculate_determinant)
            self.det_button.grid(row=n+4, column=0, columnspan=n, pady=10)
        
        elif self.mode.get() == "product":
            try:
                m = int(self.m_entry.get())
                n = int(self.n_entry.get())
                q = int(self.q_entry.get())
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter valid integers for m, n, and q.")
                return
            
            # Create first matrix (m x n)
            self.matrix_entries = []
            for i in range(m):
                row_entries = []
                for j in range(n):
                    entry = tk.Entry(self.root, width=5)
                    entry.grid(row=i+4, column=j, padx=2, pady=2)
                    row_entries.append(entry)
                self.matrix_entries.append(row_entries)
            
            # Create second matrix (n x q)
            self.matrix_entries_2 = []
            for i in range(n):
                row_entries = []
                for j in range(q):
                    entry = tk.Entry(self.root, width=5)
                    entry.grid(row=i+4, column=j+n+1, padx=2, pady=2)
                    row_entries.append(entry)
                self.matrix_entries_2.append(row_entries)
            
            # Button for matrix product calculation
            self.prod_button = tk.Button(self.root, text="Calculate Product", command=self.calculate_product)
            self.prod_button.grid(row=m+4, column=0, columnspan=q, pady=10)
    
    def get_matrix(self, entries):
        try:
            return [[int(entry.get()) for entry in row] for row in entries]
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid integers for matrix values.")
            return None
    
    def calculate_determinant(self):
        matrix = self.get_matrix(self.matrix_entries)
        if matrix:
            result = determinant(matrix)
            self.result_label.config(text=f"Determinant: {result}")
    
    def calculate_product(self):
        matrix1 = self.get_matrix(self.matrix_entries)
        matrix2 = self.get_matrix(self.matrix_entries_2)
        if matrix1 and matrix2:
            result = multiply(matrix1, matrix2)
            if result == "CAN NOT BE MULTIPLIED":
                self.result_label.config(text="Matrices cannot be multiplied (invalid dimensions).")
            else:
                result_text = "\n".join(" ".join(map(str, row)) for row in result)
                self.result_label.config(text=f"Matrix Product:\n{result_text}")

# Run the application
root = tk.Tk()
app = MatrixApp(root)
root.mainloop()
