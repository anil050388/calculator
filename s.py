# import json

# # read file
# with open('Deposits.json', 'r') as myfile:
#     data = myfile.read()

# # parse file
# obj = json.loads(data)

# # print object
# print(len(obj))

# import csv
# import json

# # open the CSV file and create a dictionary reader
# with open("Deposits.csv", "r") as csvfile:
#     reader = csv.DictReader(csvfile)

#     # open the JSON file and write the data
#     with open("file.json", "w") as jsonfile:
#         # loop through each row in the CSV file
#         for row in reader:
#             # dump the row as a JSON object
#             json.dump(row, jsonfile)
#             # add a new line after each row
#             # jsonfile.write("\n")

import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 

        for row in csvReader: 
            jsonArray.append(row)
  
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'Deposits.csv'
jsonFilePath = r'Products.json'
csv_to_json(csvFilePath, jsonFilePath)