import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append(['Nombre', 'Edad', 'Email', 'Teléfono', 'Dirección'])
wb.save('datos.xlsx')