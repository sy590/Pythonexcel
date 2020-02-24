import openpyxl
from openpyxl import load_workbook
wb = load_workbook(filename ='Rev1.xlsx')
sheet_ranges = wb['Rev Client']
print(sheet_ranges['G2'].value)