
def recordsetting(time):
    import openpyxl as xl
    wb = xl.load_workbook("racerecords3.xlsx")
    sheet = wb["Tabelle1"]
    time /= 1000
    first_cell = sheet["A1"]
    second_cell = sheet["A2"]
    third_cell = sheet["A3"]
    third = float(third_cell.value)
    second = float(second_cell.value)
    first = float(first_cell.value)
    firster = first
    seconder = second
    thirder = third
    if time < first:
        underline = 1
        firster = time

        seconder = first
        thirder = second
    elif time < second:
        underline = 2
        thirder = second
        seconder = time

    elif time < third:
        thirder = time
        underline = 3
    else:
        underline = 0
    first_cell.value = firster
    second_cell.value = seconder
    third_cell.value = thirder
    wb.save("racerecords3.xlsx")
    return firster, seconder, thirder, underline









