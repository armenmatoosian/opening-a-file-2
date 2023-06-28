# import os

import csv

#os.system("scalc C:\\Users\\armen\\Desktop\\Untitled1.xlsx")
# os.system("scalc C:\\Users\\armen\\Desktop\\Untitled1.xlsx")
# os.system("scalc C:\\Users\\armen\\Desktop\\openbb_Suppliers_for_AAPL_20230624_042437.csv")

with open("openbb_Suppliers_for_AAPL_20230624_042437.csv", 'r') as file:
  csvreader = csv.DictReader(file)
  for row in csvreader:
      print(row["Company Name"])
  file.close()