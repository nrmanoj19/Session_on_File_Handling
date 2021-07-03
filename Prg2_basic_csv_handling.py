import csv

my_lst1 = ["Name", "Age"]
my_lst2 = ["Manoj", "27"]
my_lst3 = ["Kumar", "27"]
my_lst4 = [my_lst1, my_lst2, my_lst3]

with open("my_csv1.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(my_lst1)
    csv_writer.writerow(my_lst2)
    csv_writer.writerow(my_lst3)
    csv_file.close()

with open("my_csv2.csv", "w", newline="") as csv_file2:
    csv_writer2 = csv.writer(csv_file2)
    for each_item in my_lst4:
        csv_writer2.writerow(each_item)
    csv_file2.close()

with open("my_csv1.csv") as csv_inp:
    csv_reader = csv.reader(csv_inp)
    for each_line in csv_reader:
        print(each_line)

with open("my_csv1.csv") as csv_inp1:
    csv_reader = csv.DictReader(csv_inp1)
    count = 0
    with open("my_csv3.csv", "w", newline="") as csv_out1:
        my_header = ["Name", "Age", "Gender"]
        csv_out_writer = csv.DictWriter(csv_out1, fieldnames=my_header)
        # csv_out_writer = csv.writer(csv_out1)
        for each_line in csv_reader:
            each_line['Gender'] = "Male"
            if count == 0:
                csv_out_writer.writeheader()
                # csv_out_writer.writerow(each_line.keys())
                count = count + 1
            csv_out_writer.writerow(each_line)
            # csv_out_writer.writerow(each_line.values())
