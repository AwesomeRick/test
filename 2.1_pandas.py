import pandas as pd
import sys
input_file = 'C:/Users/AwesomeRick/Desktop/Study/机器学习/csv文件/supplier_data.csv'
output_file = 'C:/Users/AwesomeRick/Desktop/new 1.csv'
data = pd.read_csv(input_file)
print(data)
data.to_csv(output_file, index=False)