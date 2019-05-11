import sys
with open('C:/Users/AwesomeRick/Desktop/Study/机器学习/csv文件/supplier_data.csv','r',newline='') as filereader:
    with open('C:/Users/AwesomeRick/Desktop/new 1.csv', 'w', newline='') as filewriter:
        header = filereader.readline()
        print(header)
        header = header.strip()
        header_list = header.split(',')
        print(header_list)
        filewriter.write(','.join(map(str, header_list))+'\n')
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')
