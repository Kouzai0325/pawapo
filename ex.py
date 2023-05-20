from openpyxl import Workbook
wb = Workbook()

ws = wb.active
ws['A1'] = 42
ws.append([1,2,3])

import datetime
ws['A2'] = datetime.datetime.now()

# Save the file
wb.save("sample.xlsx")

ab = Workbook()
colC = ws['A']
col_range = ws['A:J']
row10 = ws[10]
row_range = ws[5:10]
wb.save("s4mple.xlsx")