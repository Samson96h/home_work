import argparse
from itertools import count

parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",default="history.txt", help="The file name")
parser.add_argument("-c","--count",default=10,help="top frequently used words")
count = int(parser.parse_args().count)
fname = parser.parse_args().file


def get_data(fname):
    try:
        with (open(fname) as f):
            content = f.read().lower()
    except FileNotFoundError:
        content = None
    mstr = ''
    for el in content:
        if el == " ":
            mstr += el
        if el.isalpha():
            mstr += el
    ml = mstr.split()
    return ml

def dict_sort(ml):
    md = {}
    for el in ml:
        if el not in md:
            md[el] = 1
        else:
            md[el] += 1
    content = list(md.items())
    content.sort(key=lambda x: x[1], reverse=True)
    return content


def main():
    word_list = get_data(fname)
    result = dict_sort(word_list)
    for k, v in result[0:count + 1]:
        print(k," : ", v)

if __name__ == '__main__':
    main()