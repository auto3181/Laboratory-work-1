import string
import re


def show_ans():
    print("Общее количество символов в файле: ", all_letters_count)
    print("Общее количесто символов без пробелов: ", letters_count_without_spaces)
    print("Количество символов без знаков препинания: ", letter_count_without_punctuation)
    print("Количество слов в файле: ", words_count)
    print("Количество предложений: ", sentences_count)


punctuation_list = list(string.punctuation)  # список знаков препинания
punctuation_count = 0 
spaces_count = 0
all_letters_count = 0
letters_count_without_spaces = 0
words_count = 0
sentences_count = 0

with open('steam_description_data.csv', encoding='utf-8') as f:
    for line in f:
        all_letters_count += len(line)  # считаю длинну считанной строчки
        spaces_count += line.count(' ')  # считаю количество пробелов в строчке
        words_count += len(line.split())  # считаю количество слов в строчке, учитывая, что разделитель - пробел 
        for i in punctuation_list:  # считаю количество знаков препинания
            punctuation_count += line.count(i)
        sentences_count += len(re.findall(r"([A-Z][^\.!?]*[\.!?])", line))  # считаю количество предложений

letters_count_without_spaces = all_letters_count - spaces_count  # количество слов без пробелов
letter_count_without_punctuation = letters_count_without_spaces - punctuation_count  # количество букв без знаков преп
show_ans()
