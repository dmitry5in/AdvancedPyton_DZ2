from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding="UTF-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ


def change_phone(contacts_list):
    pattern_for_phone = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)' \
                        r'(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    new_pattern_for_phone = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    new_list_contacts = []
    for item in contacts_list:
        line = ','.join(item)
        changed_line = re.sub(pattern_for_phone, new_pattern_for_phone, line)
        new_line = changed_line.split(',')
        new_list_contacts.append(new_line)
    return new_list_contacts


def change_name():
    contacts_list_2 = change_phone(contacts_list)
    pattern_for_name = r'^([А-Я][a-я]+)(\s*)(\,?)([А-Я][a-я]+)(\s*)(\,?)([А-Я][a-я]+)?(\,?)(\,?)(\,?)'
    new_pattern_for_name = r'\1\3\10\4\6\9\7\8'
    new_list_contacts = []
    for item in contacts_list_2:
        line = ','.join(item)
        changed_line = re.sub(pattern_for_name, new_pattern_for_name, line)
        new_line = changed_line.split(',')
        new_list_contacts.append(new_line)
    return new_list_contacts


def final_list():
    contacts_list_2 = change_name()
    temp_dict = {}
    for contact in contacts_list_2:
        if contact[0] not in temp_dict.keys():
            temp_dict[contact[0]] = contact[1:]
        else:
            for i, item in enumerate(contact[1:]):
                if temp_dict[contact[0]][i - 6] == '':
                    temp_dict[contact[0]][i - 6] = item
    final_list = []
    for key, value in temp_dict.items():
        temp_contact_list = []
        temp_contact_list.append(key)
        for i in value:
            temp_contact_list.append(i)
        final_list.append(temp_contact_list)
    return final_list

# TODO 2: сохраните получившиеся данные в другой файл


list_to_write = final_list()


with open("phonebook.csv", "w", encoding="UTF-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(list_to_write)


