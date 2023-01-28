from PyPDF2 import PdfReader
import json
import os


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
    raw_data = open(filename, "r")
    return raw_data.read()



print(load_csv_file(os.path.join(os.path.dirname(__file__), "menus", "rvc_week2_2022.xlsx")))

def create_database():
    pass

