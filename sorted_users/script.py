import argparse
import os
try:
    import xlsxwriter
except ImportError:
    os.system("pip install xlsxwriter")


def parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default="users.txt", help="Input file name")
    parser.add_argument("-x", "--excel", default="sorted_users.xlsx", help="Excel output file name")
    parser.add_argument("-a", action="store_true", help="Sort alphabetically by name")
    parser.add_argument("-p", "--prog", help="Filter by profession (e.g., Programmer)")
    return parser.parse_args()

def get_data(fname):
    ml = []
    try:
        with open(fname) as f:
            content = (el.strip() for el in f.readlines())
    except FileNotFoundError:
        print("File not found:", fname)
        exit(1)

    for el in content:
        name, lastname, age, profession = el.split(" ")
        md = {
            "name": name,
            "lastname": lastname,
            "age": age,
            "profession": profession
        }
        ml.append(md)
    return ml

def write_people_rows(worksheet, start_row, people, green_fill):
    for idx, person in enumerate(people):
        age = int(person['age'])
        row_format = green_fill if age > 25 else None
        worksheet.write(start_row + idx, 0, person['name'], row_format)
        worksheet.write(start_row + idx, 1, person['lastname'], row_format)
        worksheet.write(start_row + idx, 2, age, row_format)
        worksheet.write(start_row + idx, 3, person['profession'], row_format)
    return start_row + len(people)

def write_data_excel(workbook, sheet_name, data, filtered=None, filter_sheet_name=None):
    headers = ['Name', 'Last Name', 'Age', 'Profession']
    green_fill = workbook.add_format({'bg_color': '#C6EFCE', 'pattern': 1})
    bold_header = workbook.add_format({'bold': True})

    worksheet_all = workbook.add_worksheet(sheet_name)
    for col, title in enumerate(headers):
        worksheet_all.write(0, col, title, bold_header)
    write_people_rows(worksheet_all, 1, data, green_fill)

    if filtered and filter_sheet_name:
        worksheet_filtered = workbook.add_worksheet(filter_sheet_name)
        for col, title in enumerate(headers):
            worksheet_filtered.write(0, col, title, bold_header)
        write_people_rows(worksheet_filtered, 1, filtered, green_fill)

def main():
    args = parser_arguments()
    data = get_data(args.file)

    if args.a:
        data.sort(key=lambda person: person['name'].lower())

    filtered = []
    if args.prog:
        filtered = [p for p in data if p['profession'].lower() == args.prog.lower()]
        if args.a:
            filtered.sort(key=lambda p: p['name'].lower())

    workbook = xlsxwriter.Workbook(args.excel)
    write_data_excel(workbook, "People", data, filtered, args.prog if args.prog else None)
    workbook.close()

if __name__ == "__main__":
    main()