from openpyxl import load_workbook


# Get ParamValue by ParamName
def get_param_value(param_name):
    # Load in the workbook
    wb = load_workbook('./Param.xlsx')

    # Get a sheet by name
    sheet = wb['Python']

    for row in range(sheet.min_row, sheet.max_row + 1):
        if sheet.cell(row, 1).value == param_name:
            cell_value = sheet.cell(row, 2).value
            return cell_value
            break
