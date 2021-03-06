from xlwt import *

font0 = Font()
font0.name = 'Times New Roman'
font0.struck_out = True
font0.bold = True

style0 = XFStyle()
style0.font = font0


wb = Workbook()
ws0 = wb.add_sheet('0')

ws0.write(1, 1, 'Krishna kumar', style0)

for i in range(0, 0x53):
    fnt = Font()
    fnt.name = 'Arial'
    fnt.colour_index = i
    fnt.outline = True

    borders = Borders()
    borders.left = i

    style = XFStyle()
    style.font = fnt
    style.borders = borders

    ws0.write(i, 2, 'Krishna', style)
    ws0.write(i, 3, hex(i), style0)


wb.save('styles.xls')