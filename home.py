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