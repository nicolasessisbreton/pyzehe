"""
2) Use xlwings to call from excel the previously created workbook.
"""
import clr
import Aspose.Cells as ap
import xlwings as xw

import pathlib
path = pathlib.Path(__file__).resolve().parents[1]
path = str(path)
path = path + r'\sol_1.xlsx'

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


