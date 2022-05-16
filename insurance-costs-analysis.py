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
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')

class PatientsInfo:
    # init method that takes in each list parameter
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, 
                 patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    # function that calculates the average ages of patients in insurance.csv
    def analyze_ages(self):
        total_age = 0
        for age in self.patients_ages:
            total_age += int(age)
        print ("Average Patient Age: " + str(round(total_age/len(self.patients_ages), 2)) + " years")

    # function that calculates the number of males and females in insurance.csv
    def analyze_sexes(self):
        females = 0
        males = 0
        for sex in self.patients_sexes:
            if sex == 'female':
                females += 1
            elif sex == 'male':
                males += 1
        print("Count for female: ", females)
        print("Count for male: ", males)

patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)
patient_info.analyze_ages()
patient_info.analyze_sexes()