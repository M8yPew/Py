import os
import re
import datetime
import json

#path = "C:\\Users\\Admin\\Desktop\\archive TLOCKs_rphost" + "\\"
path = "C:\\Users\\Admin\\Desktop\\Logs\\rphost" + "\\"
filename = str(path + "23022015.log")
result = ''
rownumber = 0
text = ''
result_dict = {}


print('Я дурак я начал парсит в ' + str(datetime.datetime.now()))

new_file = open(path+"result_file.txt", "w", encoding="utf-8-sig")
with open(filename, "r", encoding="utf-8-sig") as file:
    for str_line in file:
        str_line = str_line.strip()
        #if str_line.find('t:connectID=683') > -1 or str_line.find('t:connectID=264') > -1:
        if re.match(r'(\d{2}:\d{2}\.\d{6}-\d)', str_line):
            if len(result)!=0:
                text = text + '\n'
            text = str_line
        else:
            text = str(text) + str(str_line)

        new_file.write("".join([result, text]) + '\n')
        rownumber = rownumber + 1
new_file.close()

print('Я дурак я окончил парсит в ' + str(datetime.datetime.now()))
print('Всего строк ' + str(rownumber))

print('Я дурак я начал разбор в ' + str(datetime.datetime.now()))
new_file2 = open(path+"Tlock_DeadLock.txt", "w", encoding="utf-8")
with open(path+"result_file.txt", "r", encoding="utf-8-sig") as restruct_file:
    for str_line in restruct_file:
        if str_line.find('LOCK') > -1 and str_line.find('AccumRg88340') > -1 \
                or str_line.find('LOCK') > -1 and str_line.find('AccumRg88353') > -1:
            #new_file2.writelines('\n')
            new_file2.writelines(str_line)
        #[ ^],
        #new_file.write(str_line)
new_file2.close()

print('Я дурак я окончил разбор в ' + str(datetime.datetime.now()))




