# import openpyxl

# wb = openpyxl.Workbook()
# sheet = wb["Sheet"]
# sheet.title = "Hoobbies"

# for row in range(1, 10):
#     values = ["we are 3", "Om Nama Shibay"]
#     for ind, value in enumerate(values, start=1):
#         sheet.cell(row=row, column=ind, value=value)

# for row in sheet.values:
#     print(row)

# for row_id in range(1, sheet.max_row + 1):
#     for col_id in range(1, sheet.max_column +1):
#         # Update the value attribute of cell object
#         # sheet.cell(row_id, col_id).value = "Om Namah shibay"
#         # This will print the cell object
#         # print(sheet.cell(row_id, col_id))
#         # we want to print the value of the cell
#         print(sheet.cell(row_id, col_id).value, end="\t")
#     print()

# cells = sheet['a1:b3']

# print(cells)


# print (wb.worksheets)

# wb.save("output.xlsx")

# =============
a = [1,2,3,4,5]
b=set([10,20,30,40,50])
dict_1 = dict(zip(a,b))
print(dict_1)
mandatory_kpi = set([1542455307,1542460296,1542460297,1542455297,1542455298,1542455299,1542455300])
meas_types = [50332573,50332574,50342574,50342575,50342635,50342636,50332582,50332583,50332584,50332586,50342584,50342585,50342586,50342587,50342606,50342607,50342608,50342609,50342632,50342633,50332582,50332583,50332584,50332586,50342584,50342585,50342586,50342587,50342606,50342607,50342608,50342609,50342632,50342633,50332582,50332583,50332584,50332586,50342584,50342585,50342586,50342587,50342606,50342607,50342608,50342609,50342632,50342633,50332627,50332627,50332627,1526727075,1526727076,1526727077,1526727078,1526727079,1526727080,1542455297,1542455298,1542455299,1542455300,1542455301,1542455302,1542455303,1542455304,1542455305,1542455306,1542455307,1542460296,1542460297,1542455297,1542455298,1542455299,1542455300]

for meas in meas_types:
    if meas in mandatory_kpi:
        print(meas)

        