import csv

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



