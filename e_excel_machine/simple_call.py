import clr
import Aspose.Cells as ap

path = r'binomial_model.xlsx'
w = ap.Workbook(path)
s = w.Worksheets['crr']

interest_rate = s.Cells['B1']
strike = s.Cells['B2']
sigma = s.Cells['B3']
S_0 = s.Cells['B4']

interest_rate.PutValue(0.06)
strike.PutValue(40)
sigma.PutValue(0.25)
S_0.PutValue(36)

w.CalculateFormula()

price = s.Cells['B5'].DoubleValue

print('price', price)


