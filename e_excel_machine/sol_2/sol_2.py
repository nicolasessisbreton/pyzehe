"""
2) Use xlwings to call from excel the previously created workbook.
"""
import clr
import sys
import xlwings as xw

aspose_root = r'C:\Users\nessisbr\Desktop\mat\exp\aspose.cells.18.5.0\lib\net40'
sys.path.insert(0, aspose_root)

import Aspose.Cells as ap

path = r'C:\Users\nessisbr\Desktop\mat\mat\e_excel_machine\sol_1.xlsx'
w = ap.Workbook(path)
s = w.Worksheets[0]
x = s.Cells['B1']
y = s.Cells['B2']
r = s.Cells['B3']

@xw.func
def add(a, b):
	x.PutValue.Overloads[float](a)
	y.PutValue.Overloads[float](b)

	w.CalculateFormula()

	result = r.DoubleValue

	return result


