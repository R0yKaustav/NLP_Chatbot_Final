import json
import csv

def csvConv(csv_path, json_path):
    jsonData = {}

    with open(csv_path, encoding = 'utf-8') as csvfile:
        csvData = csv.DictReader(csvfile)
        for rows in csvData:
            key = rows['ArticleTitle']
            jsonData[key] = rows

    with open(json_path, 'w', encoding= 'utf-8') as jsonfile:
        jsonfile.write(json.dumps(jsonData, indent=5))
    print("Data Convert")

csv_path = r'xcldata.csv'
json_path = r'projectdata.json'

csvConv(csv_path,json_path)
print("Data Convert")
   