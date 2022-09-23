

# import xlsxwriter module
import xlsxwriter




# def create_header():
#     column = 0
#
#     content = ["Serial_NO", "Form_No", "Batch_Code", "Name",
#                "PHY_MARKS", "CHE_MARKS", "BOT_MARKS", "ZOO_MARKS", "Total_MARKS", "PERCENT", "RANK", "CAMPUS_RANK"]
#
#     for item in content:
#         # write operation perform
#         worksheet.write(0, column, item)
#
#         column += 1
#     workbook.close()
#
#
#
# def insert_rows_into_excel(row_List,cellrow,worksheet):
#
#     colnum = 0
#     for item in row_List:
#         print(item)
#         worksheet.write(cellrow, colnum, item)
#         colnum += 1


class excel_writer():
    def __init__(self):
        pass
        # self.workbook = xlsxwriter.Workbook('Counselling_data.xlsx')
        # self.worksheet = self.workbook.add_worksheet("YEAR_2021")
        # print(self.worksheet)

    def insert_into_rows(self, data_to_insert, row_num,worksheet):
        # print(data_to_insert)


        colnum = 0

        for item in data_to_insert:

            worksheet.write(row_num,colnum,item)
            colnum = colnum+1
