import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

for n, contact in enumerate(contacts_list):
    contact_name = contact[0].split(' ') + contact[1].split(' ') + contact[2].split(' ')
    contact_name = [string for string in contact_name if string]
    if len(contact_name) > 2:
        contacts_list[n][2] = contact_name[2]
    contacts_list[n][1] = contact_name[1]
    contacts_list[n][0] = contact_name[0]

for n, first_contact in enumerate(contacts_list):
    first_name = first_contact[0] + first_contact[1]
    for m, second_contact in enumerate(contacts_list):
        second_name = second_contact[0] + second_contact[1]
        if first_name == second_name and m != n:
            if not first_contact[3] or not second_contact[3]:
                contacts_list[n][3] = first_contact[3] + second_contact[3]
            contacts_list[n][4] = first_contact[4] + second_contact[4]
            contacts_list[n][5] = first_contact[5] + second_contact[5]
            contacts_list[n][6] = first_contact[6] + second_contact[6]
            del contacts_list[m]

pattern = r"\+?[7|8]?\s?[\s|\(]?(\d{3})(\)\s|-|\))?(\d{3})-?(\d{2})-?(\d+)"

for n, contact in enumerate(contacts_list):
    phone_number = contact[5]
    phone_number = re.sub(pattern, r"+7(\1)\3-\4-\5", phone_number)
    phone_number = re.sub(r"\(?доб\.\s?(\d+)\)?", r"доб.\1", phone_number)
    contacts_list[n][5] = phone_number

with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)