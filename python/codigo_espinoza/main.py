import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append(['Nombre', 'Edad', 'Email', 'Teléfono', 'Dirección'])

root = tk.Tk()
root.title("Formulario de Entrada de Datos")
root.configure(bg='#4b6587')
label_style = {'bg': '#4b6587', 'fg': 'white'}
entry_style = {'bg': '#D3D3D3', 'fg': 'black'}

label_nombre = tk.Label(root, text='Nombre', **label_style)
label_nombre.grid(row=0, column=0, padx=10, pady=5)

root.mainloop()