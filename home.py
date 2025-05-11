################################  1

def sum_nums (*args):
    sum = 0
    for el in args:
        if type(el) == int:
            sum += el
    return sum

print(sum_nums(9,8,[45,8],'hello',18))

################################  2

def count_mstr (*args):
    return len([el for el in args if type(el) == str])

print(count_mstr('hello',4,8,7,[4,5],'world'))

################################  3

def sum_mid (*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

print(sum_mid(3,6,9,8,12))

################################  4

def results (a,b):
    return [a + b, a - b, b - a, a * b, a / b, b / a]

print(results(5,9))

################################  5

def upper (str):
    upp = ""
    for i in str:
        if i == " ":
            upp += i
        elif 97 <= ord(i) <= 122:
            upp += chr(ord(i) - 32)
        else:
            upp += i
    return upp

print(upper('hello good world'))

################################  6

def lower (str):
    low = ""
    for i in str:
        if i == " ":
            low += i
        elif 65 <= ord(i) <= 90:
            low += chr(ord(i) + 32)
        elif 97 <= ord(i) <= 122:
            low += i
        else:
            low += i
    return low

print(lower('HELLO GOOD WORLD'))

################################  7

def title(text):
    words = text.split()
    md = []
    for word in words:
        if len(word) > 0:
            new_word = word[0].upper() + word[1:].lower()
            md.append(new_word)
        else:
            md.append(word)
    return ' '.join(md)

print(title('hello good world'))

################################  8

def reversed (str):
    return str[::-1]

print(reversed('hello world'))

################################  9

def subString (str,a,b):
    return str[a+1:b]

print(subString('substring',2,6))

################################  10

def longest (mstr):
    long = ''
    for el in mstr.split():
        if len(long) < len(el):
            long = el
    return long

print(longest('hello good world!'))

################################  11

def max_let (mstr):
    nc = 0
    el = ''
    for i in mstr.lower():
        coun = mstr.count(i)
        if coun > nc:
            nc = coun
            el = i
    return el

print(max_let("hello good world"))

################################  12

def longest_word_let (mstr):
    ml = mstr.split()
    ml.sort(key = len)
    el = ""
    nc = 0
    word = ml[-1]
    for i in word.lower():
        coun = word.count(i)
        if coun > nc:
            nc = coun
            el = i
    return el

print(longest_word_let("hello good world!"))

################################  13

def duble_index (mstr,num):
    ml = []
    ml.append(mstr[num])
    if mstr[-1] not in ml:
        ml.append(mstr[-num])
    return set(ml)

print(duble_index('names!',3))

################################  15

def is_polindrom (num):
    mstr = str(num)
    return mstr == mstr[::-1]

print(is_polindrom(5653))

################################  16

def nearby_polindrom (num):
    num1 = num
    num2 = num
    if len(str(num)) == 1:
        return num
    else:
        while str(num1) != str(num1)[::-1]:
            num1 += 1
        while str(num2) != str(num2)[::-1]:
            num2 -= 1
        if num - num2 > num1 - num:
            return num1
        else:
            return num2

print(nearby_polindrom(32))

################################  17

def product_of_nums (num):
    ns = str(num)
    return int(ns[0]) * int(ns[-1])

print(product_of_nums(2365))

################################  18

def count_str(list):
    count = 0
    for el in list:
        if isinstance(el, str):
            count += 1
    return count

print(count_str([15, 'hello', [4, 6, 9, 7], {"a": 12}, 'my day']))

################################  19

def max_num (list):
    ml = []
    for el in list:
        if isinstance(el, int):
            ml.append(el)
    return max(ml)

print(max_num([15, 'hello', 4, 56, [4, 6, 9, 7], {"a": 12}, 'my day']))

################################  20

def even_nums (list):
    ml = []
    for el in list:
        if isinstance(el, int) and 10 <= el <= 99 and el % 2 == 0:
            ml.append(el)
    return ml

print(even_nums([15, 'hello', 4, 56, [4, 6, 9, 7], {"a": 12}, 98, 'my day']))

################################  21

def numerical_average (list):
    ml = []
    for el in list:
        if isinstance(el, int):
            ml.append(el)
    return sum(ml) / len(ml)

print(numerical_average([15, 'hello', 4, 56, [4, 6, 9, 7], {"a": 12}, 98, 'my day']))

################################  22

def len_str (list):
    ml = []
    for el in list:
        ml.append(len(el))
    return ml

print(len_str(['hello', 'my', 'good', 'world']))

################################  23

def nums_reverse (list):
    ml = []
    for el in list:
        if isinstance(el, int):
            ml.append(el)
    ml.sort(reverse=True)
    return ml

print(nums_reverse([15, 'hello', 4, 56, [4, 6, 9, 7], {"a": 12}, 98, 'my day']))

################################  24

def mstr_reverse (list):
    ml = []
    for el in list:
        if isinstance(el, str):
            ml.append(el)
    ml.sort(reverse = True,key = len)
    return ml

print(mstr_reverse([15, 'hello', 4, 56, [4, 6, 9, 7], 'professional', {"a": 12}, 98, 'my day']))

################################  25

def many_vowels (list):
    count = 0
    ms = ''
    for el in list:
        a = 0
        for i in el:
            if i in 'oauei':
                a += 1
        if a > count:
            count = a
            ms = el
    return ms

print(many_vowels(['hello', 'mooon', 'good', 'world']))

################################  26

def longest_mstr (list):
    count = 0
    ms = ''
    for el in list:
        ml = el.split()
        if len(ml) > count:
            count = len(ml)
            ms = el
    return ms

print(longest_mstr(['hello world', 'the moon is so big', 'good by my friend']))

################################  27

def big_num(mstr):
    words = mstr.split()
    max = 0

    for word in words:
        digits = ''
        for i in word:
            if i.isdigit():
                digits += i
        if digits:
            number = int(digits)
            if number > max:
                max = number

    return max

print(big_num('ok156 my45 is a 1968!'))

################################  28

def oldest_person(list):
    oldest = list[0]
    for el in list[1:]:
        if el['age'] > oldest['age']:
            oldest = el
    return oldest


print(oldest_person([{'name': 'Ann','age': 36,'phon': '54864'},{'name':'Georgy','age': 45},{'name': 'Matin', 'age': 46 , 'phon' : '033215487'}]))

################################  29

def sort_score(list):
    return sorted(list, key=lambda dct: dct['score'])

print(sort_score([{'name':'Anna', 'score': 88},{'name': 'Ben','score':74},{'name':'Diana', 'score':95}
]))

################################  30

def longest_name(list):
    ml = sorted(list, key=lambda dct: len(dct['name']))
    return ml[-1]

print(longest_name([
    {'name': 'MIT', 'rank': 5},
    {'name': 'Harvard University', 'rank': 2},
    {'name': 'California Institute of Technology', 'rank': 2}
]))