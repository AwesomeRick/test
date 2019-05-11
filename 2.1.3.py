import csv
input_file = 'C:/Users/AwesomeRick/Desktop/Study/机器学习/csv文件/supplier_data.csv'
output_file = 'C:/Users/AwesomeRick/Desktop/new 1.csv'
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file, 'r', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file,delimiter='')
        filewriter = csv.reader(csv_out_file, delimiter='')
        for row_list in filereader:
            print(row_list)
            filewriter.writerrow(row_list)