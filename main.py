import csv
import re

symb = 0
punctuation_symb = 0
spaces = 0
words = 0
sentences = 0

with open('steam_description_data.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        string = ','.join(row)
        symb += len(string)
        spaces += string.count(' ')

        punctuation_symb += string.count('.') + string.count(',') + string.count('!') + string.count('?')
        punctuation_symb += string.count('\"') + string.count('\'') + string.count(':') + string.count(';')
        punctuation_symb += string.count('>') + string.count('<')
        punctuation_symb += string.count('-') + string.count('(') + string.count(')')

        words += len(re.findall(r"(\w+'\w+)|(\w+-\w+'\w+)|(\w+-\w+'\w)|\w+", string))
        sentences += len(re.findall(r"([A-Z][^\.!?]*[\.!?])", string))

print("Общее количество символов в файле: ", symb)
print("Общее количесто символов без пробелов: ", symb - spaces)
print("Количество символов без знаков препинания: ", symb - punctuation_symb)
print("Количество слов в файле: ", words)
print("Количество предложений: ", sentences)
