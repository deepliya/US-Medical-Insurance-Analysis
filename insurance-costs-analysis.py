# importing csv library
import csv

# Initializing lists for diffrent attributes in insurance.csv
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

# helper function to load csv data
def load_list_data(lst, csv_file, column_name):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info) 
        for row in csv_dict:
            lst.append(row[column_name])

load_list_data(ages, 'insurance.csv', 'age')
print(ages)