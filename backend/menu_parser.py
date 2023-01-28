from PyPDF2 import PdfReader

reader = PdfReader("./menus/bmh_week1_2022.pdf")

for page_num in range(len(reader.pages)):
    page = reader.pages[page_num]
    print(page.extract_text())
