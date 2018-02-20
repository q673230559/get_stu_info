__author__ = 'Administrator'
import xlwt

"""
插入数据到excel中
"""
def insert_xls(dic_list, xls_name):
    wb = xlwt.Workbook()
    ws = wb.add_sheet(xls_name)

    q = 0
    for h in dic_list[0]:
        q += 1
        ws.write(0, q, h)

    m = 0
    for d in dic_list:
        m += 1
        n = 0
        for i in d:
            n += 1
            ws.write(m, n, d[i])

    wb.save("myfile.xls")