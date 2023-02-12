import csv
import pandas as pd

target_list = []

with open('UserList@_sou_ura.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@539__zu.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@abcdefgjtjt.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@armada_armd.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@dos__sama.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@hamesama_numa.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@ikisama_land.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@jojou7777.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@numaoji_.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@numashin_.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@takkysa.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@toy_hop_582.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@tubasa_dao_.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@tukibito_s.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@xenphoad.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@xOZdFBPlGyTOcoR.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@yoshiyos9.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@yukkii_69.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

with open('UserList@yuudai0941.csv', encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        editRow = [row[1], row[2], row[3]]
        target_list.append(editRow)

result_list =[]
for i in target_list:
    if i not in result_list:
        result_list.append(i)

user_list = pd.DataFrame(result_list, columns=["user", "friends", "followers"])
user_list.to_csv("TargetUserList.csv")
print("TargetUserList.csvファイルを作成しました")