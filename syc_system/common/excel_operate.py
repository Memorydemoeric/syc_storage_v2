import xlrd
import openpyxl


def translate_excel_data(file_path, sheet_num=0, start_row=0, end_row=-1):
    data = xlrd.open_workbook(file_path)
    table = data.sheets()[sheet_num]
    data_lt = [table.row_values(i) for i in range(start_row, table.nrows + 1 + end_row)]
    check_word = table.cell_value(0, 0)
    return data_lt, check_word

