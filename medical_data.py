import PyPDF2
import xlsxwriter
from excelwrter import excel_writer
import re
from Data_Extractor import data_extractor

workbook = xlsxwriter.Workbook('Counselling_data.xlsx')
worksheet = workbook.add_worksheet("YEAR_2021")
input_File = open("All Admitted Candidates List MBBS_BDS & BSC NURSIN.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(input_File)
row_num = 0
data_extractor = data_extractor()
excel_writer = excel_writer()
pattern = re.compile(r'\d{10}')
total_pages = pdf_reader.numPages
# college_pattern = re.compile(r'\d+\S[a-zA-Z]+.+\s+(MBBS|BDS)')
for page in range(1293,1297):
    pageObj = pdf_reader.getPage(page)
    page_data = pageObj.extractText()
    indexes = []
    matches = pattern.finditer(page_data)
    for match in matches:
        start, end = match.span()
        # print(start,end)
        indexes.append(start)
    j = 0
    for i in indexes:
        j += 1
        if (j == len(indexes)):
            row_info = (page_data[i + 10:])
            # print("last", end="")
            # print(row_info.replace("\n", " "))
        else:
            row_info = (page_data[i + 10:indexes[j]])
            # print("first", end="")
            # print(row_info.replace("\n", " "))
        row_num += 1
        try:
            college_name, option_No = data_extractor.get_collage_name(row_info)
            print(college_name,option_No)
            # Subject      = data_extractor.get_branch(row_info)
            subject, alloted_category, alloted_ph, admitted_round = data_extractor.get_alloted_cat_ph_roundnum(row_info)
            all_india_rank, category = data_extractor.get_air_category(row_info)
            quota_name = data_extractor.get_quota_name(row_info)
            data_to_insert = [quota_name, all_india_rank, category, option_No, (college_name), subject,
                              alloted_category,
                              alloted_ph, admitted_round]
        except:
            print()

        try:
            excel_writer.insert_into_rows(data_to_insert, row_num,worksheet)
        except:
            print()
workbook.close()

#
# (MBBS|BDS)\s\w+\s\w+\s+\d+\s\d+           branch alloted category ph rpund
# \d+\s\w+\s\d+\w+                        ********** quota