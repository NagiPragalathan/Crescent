# Python program to read an excel file

# import openpyxl module
import openpyxl

path = "gfg.xlsx"

wb_obj = openpyxl.load_workbook(path)

sheet_obj = wb_obj.active

cell_obj = sheet_obj.cell(row = 1, column = 1)

print(cell_obj.value)
