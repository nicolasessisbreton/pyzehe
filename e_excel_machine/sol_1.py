"""
1) Write an excel workbook to add two numbers.
	 Use this workbook in python.
 """
import clr
import Aspose.Cells as ap

path = r'sol_1.xlsx'
w = ap.Workbook(path)
s = w.Worksheets[0]

x = s.Cells['B1']
y = s.Cells['B2']

x.PutValue(1)
y.PutValue(1)

w.CalculateFormula()

result = s.Cells['B3'].DoubleValue

print('result', result)


