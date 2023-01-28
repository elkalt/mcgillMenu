from PyPDF2 import PdfReader
import json
import pandas as pd
import warnings


def read_text(path, page_number):
    '''(str, int) -> str'''
    reader = PdfReader(path)
    page = reader.pages[page_number]
    #for page_num in range(len(reader.pages)):
        #page = reader.pages[page_num]
        #menu_str += page.extract_text()
    return page.extract_text()


#print(read_text("./menus/bmh_week1_2022.pdf", 0))
#print(read_text("./menus/rvc_week4_2022.pdf", 0))
#print(read_text("./menus/rvc_week3_2022.pdf", 0))


def load_csv_file(filename):
    #read and store content of the excel file
    read_file = pd.read_excel(filename)
    #write the df obj into a csv file
    read_file.to_csv(filename, index=None, header=True)
    #read a csv file and convert into a dataframe obj
    df = pd.DataFrame(pd.read_csv(filename))
    return df


print(load_csv_file("./menus/rvc_week2_2022.xlsx"))
def create_database():
    pass

