from PyPDF2 import PdfReader
import os
import json
DINING_HALLS = ["royal victoria college", "bishop mountain hall", "new residence hall", "douglas hall", "carrefour sherbrooke"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
MEALS = ["breakfast", "lunch", "dinner", "soup", "brunch"]
DIETARY_SYMBOLS = ["gf", "v", "ve", "df", "msc", "h"]

def read_text(path, page_number):
    '''(str, int) -> str
    Reads pdf given by path input at a certain page and returns
    a string of what was read. This is not used lol.
    '''
    reader = PdfReader(path)
    page = reader.pages[page_number]
    return page.extract_text()


#print(read_text("./menus/bmh_week1_2022.pdf", 0))
#print(read_text("./menus/rvc_week4_2022.pdf", 0))
#print(read_text("./menus/rvc_week3_2022.pdf", 0))

def load_csv_file(filename):
    raw_data = open(filename, "r")
    return raw_data.read()


#print(load_csv_file(os.path.join(os.path.dirname(__file__), "menus", "rvc_week2_2022.xlsx")))

def refine_to_list(raw_data):
    '''
    (str) -> list<str>
    Converts raw data into a list of strings, each element being
    one line of the raw data, without any excess quotations.
    '''
    raw_list = raw_data.split("\n")
    for i in range(len(raw_list)):
        raw_list[i] = raw_list[i].strip("\"").lower()
    better_list = []
    j = -3
    for i in range(len(raw_list)):
        if raw_list[i][-1] == " ":
            new_elmt = raw_list[i].strip("\"")
        elif i == (j + 1):
            new_elmt += raw_list[i].strip("\"")
            better_list.append(new_elmt)
        else:
            better_list.append(raw_list[i])
    return better_list
def better_json_dict_creation(better_list, hall_given):
    '''
    (list<str>) -> dict
    Creates the json dictionary, hopefully in a better way.
    Maybe combines helper functions, who knows...
    '''
    json_dict = dict()
    day = "maddie day!"
    dish = ""
    symbol_list = []
    hall_name = hall_given

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
            for elmt in DIETARY_SYMBOLS:
                json_dict[day][meal][dish][elmt] = False
            for elmt in line_list:
                if elmt in DIETARY_SYMBOLS:
                    json_dict[day][meal][dish][elmt] = True
    my_tuple = json_dict, hall_name
    return my_tuple

def load_json_dict(file_shortcut, hall_given, json_name):
    '''(str) -> NoneType
    Loads the csv file corresponding to the given file shortcut and
    saves a json file. Returns nothing.
    '''
    data = load_csv_file(os.path.join(os.path.dirname(__file__), "menus", file_shortcut))
    json_list = refine_to_list(data)
    json_dict, hall_name = better_json_dict_creation(json_list, hall_given)

    filename = os.path.join(os.path.dirname(__file__), "database", "weekly", f"{json_name}.json")
    json_obj = {}
    # Check if file exists
    if os.path.isfile(filename) is True:
        # Read JSON file
        with open(filename) as fp:
            json_obj = json.load(fp)
        json_obj[hall_name] = json_dict
        final_dict = json_obj
    else:
        final_dict = dict()
        final_dict[hall_name] = json_dict

        # Verify existing list

    with open(filename, 'w') as json_file:
        json.dump(final_dict, json_file,
                  indent=4,
                  separators=(',', ': '))
    # Verify updated list

    print('Successfully appended to the JSON file')


def create_json_dict(raw_data):
    '''(str) -> NoneType
    Creates a json file in the database.
    Returns a dictionary for now...
    '''
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
            for elmt in DIETARY_SYMBOLS:
                json_dict[day][meal][dish][elmt] = False
            for elmt in line_list:
                if elmt in DIETARY_SYMBOLS:
                    json_dict[day][meal][dish][elmt] = True



    #json_dict[day] = put
    #load json string here with hall_name
    return json_dict

x = "\"\"\n\"\"\n\"\"\n\"\"\n\"\"\n\"\"\n\"\"\nWEDNESDAY\nBREAKFAST\nBlueberry Pancakes\nSOUP\nThai Chicken & Rice\nTomato & Tofu Potage VE\nLUNCH\nCod in Herbed Crust MSC\nSpaghetti\nw/ Meat Sauce\nw/Primavera Sauce VE\nGarlic Bread VE \nVegetable Fried Rice\nDINNER\nTacos VEGAN\nPulled PorkTacos GF DF\nBeef Tacos DF"
#print(load_csv_file(os.path.join(os.path.dirname(__file__), "menus", "rvc_week2_2022.xlsx")))
nrh = "nrh_jan23_2023.csv"
rvc = "rvc_week4_2022.csv"
dh = "dh_week3_2022.csv"
cs = "cs_jan23_2023.csv"
bmh = "bmh_week1_2022.csv"
#load_json_dict(nrh, "new residence hall", "mega")

data = load_csv_file(os.path.join(os.path.dirname(__file__), "menus", nrh))
#y = create_json_dict(data)
#print(y)
test = refine_to_list(data)
print(test)
#my_dict = better_json_dict_creation(test)
