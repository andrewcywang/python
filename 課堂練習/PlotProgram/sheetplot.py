from xlrd import open_workbook
import matplotlib.pyplot as plt
import matplotlib.font_manager as pf

data=[]
wb = open_workbook('Data.xlsx')
s = wb.sheet_by_name('總和')
print('工作表:',s.name)
for row in range(s.nrows):
    print('資料列:',row)
    values = []
    for col in range(s.ncols):
        values.append(s.cell(row,col).value)
    print(values)
    data.append(list(values))

print(data)

zhfont1 = pf.FontProperties(fname='C:\Windows\Fonts\kaiu.ttf')
plt.bar(x=data[0],height=data[1])
plt.xticks(fontproperties=zhfont1)
plt.xlabel("季度",fontproperties=zhfont1)  
plt.ylabel("金額",fontproperties=zhfont1)  
plt.title("業績",fontproperties=zhfont1) 
plt.show()


