from PyPDF2 import PdfReader
import json
def read_text(path, page_number):
    '''(str, int) -> str'''
    reader = PdfReader(path)
    page = reader.pages[page_number]
    #for page_num in range(len(reader.pages)):
        #page = reader.pages[page_num]
        #menu_str += page.extract_text()
    return page.extract_text()

#print(read_text("./menus/bmh_week1_2022.pdf", 0))
print(read_text("./menus/rvc_week4_2022.pdf", 0))
def create_database():

    pass

