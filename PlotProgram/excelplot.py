from xlrd import open_workbook
header=[]
data=[]
wb = open_workbook('Data.xlsx')
for s in wb.sheets():
    print('工作表:',s.name)
    for row in range(s.nrows):
        print('資料列:',row)
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print(values)
        header.append(values[0])
        data.append(values[1])


