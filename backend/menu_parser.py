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

def rid_not_apostrophes(weird_string):
    good_string = ""
    for i in len(range(weird_string)):
        pass
    return good_string


#print(load_csv_file(os.path.join(os.path.dirname(__file__), "menus", "rvc_week2_2022.xlsx")))

DINING_HALLS = ["royal victoria college", "bishop mountain hall", "new residence hall", "douglas hall", "carrefour sherbrooke"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
MEALS = ["breakfast", "lunch", "dinner", "soup", "brunch"]
DIETARY_SYMBOLS = ["gf", "v", "ve", "df", "mse", "h"]
def create_json_dict(raw_data):
    '''(str) -> NoneType
    Creates a json file in the database.
    Returns a dictionary for now...'''
    raw_list = raw_data.split("\n")
    better_list = []
    j = -3
    new_elmt = ""
    for i in range(len(raw_list)):
        if i == (len(raw_list)-1):
            break
        elif raw_list[i][-2] == " ":
            new_elmt = raw_list[i].strip("\"")
            j = i
        elif i == (j+1):
            new_elmt += raw_list[i].strip("\"")
            better_list.append(new_elmt)
        else:
            better_list.append(raw_list[i])

    json_dict = dict()
    day = "maddie day!"
    dish = ""
    symbol_list = []

    for i in range(len(better_list)):
        new_line = better_list[i].lower().strip("\"")
        if new_line in DINING_HALLS:
            hall_name = new_line
        elif new_line in DAYS:
            day = new_line
            json_dict[day] = {}
        elif new_line in MEALS:
            meal = new_line
            json_dict[day][meal] = {}
        elif new_line in ["dining hall"] or "*" in new_line:
            continue
        elif new_line[0:2] == "w/" or new_line[0:6] == "option":
            new_list = new_line.split()
            for j in range(len(new_list)):
                if new_list[j] in DIETARY_SYMBOLS:
                    new_key = dish + " " + " ".join(new_list[:j])
                    symbol_list.append(new_list[j:])
                    break
                new_key = dish + " " + new_line
            for elmt in symbol_list:
                if elmt in DIETARY_SYMBOLS:
                    json_dict[day][meal][dish][elmt] = True

            json_dict[day][meal][new_key] = json_dict[day][meal][dish]
        elif new_line.split()[0] not in DIETARY_SYMBOLS:
            dish_list = new_line.split()

            dish = ""
            symbol_list = []
            for j in range(len(dish_list)):
                if dish_list[j] in DIETARY_SYMBOLS:
                    dish = " ".join(dish_list[:j])
                    symbol_list = dish_list[j:]
                    break
                else:
                    dish = new_line

            json_dict[day][meal][dish] = {}
            for elmt in DIETARY_SYMBOLS:
                if elmt in symbol_list:
                    json_dict[day][meal][dish][elmt] = True
                    symbol_list.remove(elmt)
                else:
                    json_dict[day][meal][dish][elmt] = False

        elif new_line.split()[0] in DIETARY_SYMBOLS:
            line_list = new_line.split()
            for elmt in line_list:
                symbol_list.append(elmt)
            for elmt in DIETARY_SYMBOLS:
                json_dict[day][meal][dish][elmt] = True


    #json_dict[day] = put
    #load json string here with hall_name
    return json_dict

x = "\"\"\n\"\"\n\"\"\n\"\"\n\"\"\n\"\"\n\"\"\nWEDNESDAY\nBREAKFAST\nBlueberry Pancakes\nSOUP\nThai Chicken & Rice\nTomato & Tofu Potage VE\nLUNCH\nCod in Herbed Crust MSC\nSpaghetti\nw/ Meat Sauce\nw/Primavera Sauce VE\nGarlic Bread VE \nVegetable Fried Rice\nDINNER\nTacos VEGAN\nPulled PorkTacos GF DF\nBeef Tacos DF"

nrh = "nrh_jan23_2023.csv"
rvc = "rvc_week4_2022.csv"
dh = "dh_week3_2022.csv"
cs = "cs_jan23_2023.csv"
bmh = "bmh_week1_2022.csv"
data = load_csv_file(os.path.join(os.path.dirname(__file__), "menus", dh))
y = create_json_dict(data)
print(y)
