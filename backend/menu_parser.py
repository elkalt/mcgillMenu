from PyPDF2 import PdfReader

reader = PdfReader("./menus/bmh_week1_2022.pdf")
page = reader.pages[0]
foo = page.extract_text()
print(foo)
