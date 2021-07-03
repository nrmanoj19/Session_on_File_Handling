import csv
import json

with open("my_csv3.csv") as inp_csv:
    csv_reader = csv.DictReader(inp_csv)
    my_lst = []
    my_dict = {}
    for each_row in csv_reader:
        my_lst.append(each_row)
        key = each_row['Name']
        temp_dict = {"Age": each_row["Age"], "Gender": each_row["Gender"]}
        my_dict[key] = temp_dict
    print(my_dict)
    with open("my_json2.json", "w") as out_csv:
        json.dump(my_lst, out_csv, indent=4)
        out_csv.close()
    with open("my_json3.json", "w") as out_csv2:
        json.dump(my_dict, out_csv2, indent=4)
        out_csv2.close()
    inp_csv.close()
