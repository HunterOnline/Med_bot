# import re
#
# from utils.db_api.quick_commands import add_question
#
# data = []
#
# def get_data():
#     with open("med.txt", "r", encoding="UTF-8") as faile:
#         question_without_number = None
#         variant = ''
#
#         # ls = []
#         for question in faile.readlines():
#
#             if question[0].isdigit():
#
#                 if question_without_number:
#
#                    data.append({'question': question_without_number.strip(), 'options': variant.split('@'), 'points': mark})
#                    # ls.clear()
#                    variant = ''
#
#
#
#                 # Регулярний вираз для знаходження цифри разом з дужкою та пробілів навколо неї
#                 pattern = r'\d+\)\s*'
#                 pattern_mark = r'\((\d+)\s*бал[а]*\)\??$'
#
#                 # Видалення номера з питання та пошук оцінки
#                 question_without_number = re.sub(pattern, '', question)
#                 match = re.search(pattern_mark, question)
#
#                 # Якщо цифра знайдена, записуємо її у змінну
#                 if match:
#                     mark = match.group(1)
#                 else:
#                     mark = None
#
#             else:
#                 pattern = r'[a-zA-Z]?\)\s*(.*?)\s*$'   #r'[a-zA-Z]?\)\s*(.*?)\s*$'
#
#                 match = re.search(pattern, question)
#
#                 if match:
#                     clean_variant = match.group(1)
#                     # ls.append(clean_variant)
#                     variant+=clean_variant+'@'
#
#
# get_data()
# for i in data:
#     i['options'].remove('')
# for i in data:
#     print(i)
import json

# # Конвертація у JSON:
# json_data = json.dumps(data)


# Вивід JSON-даних:
# print(json_data)


# with open("data.json", "w", ) as json_file:
#     json.dump(data, json_file, indent=4,)
with open("data.json", "r") as json_file:
        # Прочитати вміст файлу
        json_content = json_file.read()
        # Десеріалізувати JSON-рядок у Python-об'єкт
        for  i in json.loads(json_content):
            print(i)
