
import openpyxl

def get_login_data():
    workbook = openpyxl.load_workbook('C://Users//Subham//PycharmProjects//M25_Selenium//Part_C//DemoTricentis_BasePage//test_data//Login_Data.xlsx')
    sheet=workbook["Login_Data"]

    data = []

    for row in sheet.iter_rows(min_row=2,values_only=True):
        data.append(row)

    return data