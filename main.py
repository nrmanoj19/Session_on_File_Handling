import csv


with open("my_csv1.csv") as csv_inp1:
    csv_reader = csv.DictReader(csv_inp1)
    for each_line in csv_reader:
        print(each_line)
        print(type(each_line))


with open("my_csv1.csv") as csv_inp:
    csv_reader = csv.reader(csv_inp)
    for each_line in csv_reader:
        print(each_line)
        print(type(each_line))


import pandas as pd


my_df = pd.read_csv('my_csv1.csv')
print(my_df.head(3))
my_df.to_csv("df_to_csv.csv", index=False)