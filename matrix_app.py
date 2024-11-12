import tkinter as tk
from tkinter import messagebox

# Import files
from determinant_calculator import determinant
from matrix_multiplication import calculate_product

class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Matrix Calculator")

        # Matrix size input
        self.size_label = tk.Label(root, text="Enter Matrix Size (n x n):")
        self.size_label.grid(row=0, column=0, padx=5, pady=5)
        self.size_entry = tk.Entry(root, width=5)
        self.size_entry.grid(row=0, column=1, padx=5, pady=5)

        # Buttons
        self.generate_button = tk.Button(root, text="Generate Matrix", command=self.generate_matrix_inputs)
        self.generate_button.grid(row=0, column=2, padx=5, pady=5)

        self.matrix_entries = []
    
    def generate_matrix_inputs(self):
        # Clear previous entries
        for entry_row in self.matrix_entries:
            for entry in entry_row:
                entry.destroy()
        try:
            self.n = int(self.size_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer for matrix size")
        
        # Input fields
        self.matrix_entries = []
        for i in range(self.n):
            row_entries = []
            for j in range(self.n):
                entry = tk.Entry(self.root, width=5)
                entry.grid(row=i+1, column=j, padx=2, pady=2)
                row_entries.append(entry)
            self.matrix_entries.append(row_entries)
        
        self.determinant_button = tk.Button(self.root, text="Calculate determinant", command=self.calculate_determinant)
        self.determinant_button.grid(row=self.n+1, column=0, columnspan=2, pady=10)

        self.multiply_button = tk.Button(self.root, text="Calculate product", command = self.multiply_matrices)
        self.multiply_button.grid(row=self.n+1, column=2, columnspan=2, pady=10)

        # Result display placeholder
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=self.n+2, column=0, columnspan=self.n, pady=10)

    def get_matrix(self):
        matrix = []
        try:
            for row_entries in self.matrix_entries:
                row = [int(entry.get()) for entry in row_entries]
                matrix.append(row)
            return matrix
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid integers for matrix values.")
            return None

    def calculate_determinant(self):
        matrix = self.get_matrix()
        if matrix:
            try:
                result = determinant(matrix)
                self.result_label.config(text=f"Determinant: {result}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
    def multiply_matrices(self):
        pass

root = tk.Tk()
app = MatrixApp(root)
root.mainloop()


