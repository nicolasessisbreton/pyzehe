"""
1) Write an excel workbook to add two numbers.
	 Use this workbook in python.
	 """
import clr
import sys

aspose_root = r'C:\Users\nessisbr\Desktop\mat\exp\aspose.cells.18.5.0\lib\net40'
sys.path.insert(0, aspose_root)

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


