# import csv and statistics libraries
import csv
import statistics

# Initialize lists for diffrent attributes in insurance.csv
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
        # open csv file
        csv_dict = csv.DictReader(csv_info)
        # loop through the data in each row of the csv  
        for row in csv_dict:
            # add the data from each row to a list
            lst.append(row[column_name])

# Load data from the csv file into respective lists
load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')

# Convert list elements into appropriate types to aid analysis
insurance_charges = [float(charge) for charge in insurance_charges ]
num_children = [int(child) for child in num_children] 
ages = [int(age) for age in ages] 
bmis = [float(bmi) for bmi in bmis]

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

    # function that calculates the average charges for patients in different age groups
    def analyze_ages(self):
        #intitializing total_age and counters for all age classes and their respective charges
        total_age = 0
        age_20 = 0
        age_30 = 0
        age_40 = 0
        age_50 = 0
        age_g50 = 0
        chg_20 = 0
        chg_30 = 0
        chg_40 = 0
        chg_50 = 0
        chg_g50 = 0
        
        for age in self.patients_ages:
            total_age += age

        # Looping through the dataset to find out how many people are in each age group and their total charges for each
        for age, charge in zip(self.patients_ages, self.patients_charges):
            if age < 20:
                age_20 += 1
                chg_20 += charge
            if 20 <= age < 30:
                age_30 += 1
                chg_30 += charge
            if 30 <= age < 40:
                age_40 += 1
                chg_40 += charge
            if 40 <= age < 50:
                age_50 += 1
                chg_50 += charge 
            if age >= 50:
                age_g50 += 1
                chg_g50 += charge
        
        print("----------------------------------------------------------------------")
        print("ANALYSIS BASED ON AGE ATRRIBUTE\n")
        print ("Average Patient Age: " + str(round(total_age/len(self.patients_ages), 2)) + " years")
        print ("Average charges for patients below the age of 20: $", round(chg_20/age_20, 3))
        print ("Average charges for patients between the age of 20 and 30: $", round(chg_30/age_30, 3))
        print ("Average charges for patients between the age of 30 and 40: $", round(chg_40/age_40, 3))
        print ("Average charges for patients between the age of 40 and 50: $", round(chg_50/age_50, 3))
        print ("Average charges for patients above the age of 50         : $", round(chg_g50/age_g50, 3), "\n")
    

    # function that calculates the number of males and females and the average charges for each group in insurance.csv
    def analyze_sexes(self):
        # Intialize counters for number of males and females and their respective cumulative charges
        females = 0
        males = 0
        female_charges = 0
        male_charges = 0
        avg_female = 0
        avg_male = 0

        # loop through sex and charge columns to count number of males and females and their respective charges
        for sex, charge in zip(self.patients_sexes, self.patients_charges):
            if sex == 'female':
                females += 1
                female_charges += charge
            elif sex == 'male':
                males += 1
                male_charges += charge
        avg_female = round(female_charges/females, 3)
        avg_male = round(male_charges/males, 3)
        print("----------------------------------------------------------------------")
        print("ANALYSIS BASED ON GENDER ATRRIBUTE\n")
        print("Count of females: ", females)
        print("    Average charge for a female: $", avg_female)
        print("Count of males: ", males)
        print("    Average charge for a male: $", avg_male, "\n")
    
    def analyze_bmi(self):
        # Intialize counters for each BMI class and their respective charge counters
        undr_wt = 0
        norm_wt = 0
        ovr_wt = 0
        obese = 0
        undr_ch = 0
        norm_ch = 0
        ovr_ch = 0
        obese_ch = 0

        # loop through bmi and charge columns to count number of people in different BMI classes and their respective charges
        for bmi, charge in zip(self.patients_bmis, self.patients_charges):
            if bmi < 18.5:
                undr_wt += 1
                undr_ch += charge
            if 15.5 <= bmi <= 24.9:
                norm_wt += 1
                norm_ch += charge
            if 15.5 <= bmi <= 24.9:
                ovr_wt += 1
                ovr_ch += charge
            if bmi >= 30.0:
                obese += 1
                obese_ch += charge
        
        print("----------------------------------------------------------------------")
        print("ANALYSIS BASED ON BMI ATRRIBUTE\n")
        print("Patients underweight: ", undr_wt)
        print("    Average charges: $", round(undr_ch/undr_wt, 3))
        print("Patients healthy weight: ", norm_wt)
        print("    Average charges: $", round(norm_ch/norm_wt, 3))
        print("Patients overweight: ", ovr_wt)
        print("    Average charges: $", round(ovr_ch/ovr_wt, 3))
        print("Patients obese: ", obese)
        print("    Average charges: $", round(obese_ch/obese, 3), "\n")

    def analyze_smokers(self):
        smkrs = 0
        non_smkrs = 0
        smkr_ch = 0
        nonsmk_ch = 0

        for smkr, charge in zip(self.patients_smoker_statuses, self.patients_charges):
            if smkr == 'yes':
                smkrs += 1
                smkr_ch += charge
            else:
                non_smkrs += 1
                nonsmk_ch += charge
        
        print("----------------------------------------------------------------------")
        print("ANALYSIS BASED ON SMOKER ATRRIBUTE\n")
        print("Percentage of smokers in dataset: ", round(((smkrs/(smkrs+non_smkrs))*100), 3), "%")
        print("    Average charge for a smoker: $", round(smkr_ch/smkrs, 3))
        print("Percentage of non-smokers in dataset: ", round(((non_smkrs/(smkrs+non_smkrs))*100), 3), "%")
        print("    Average charge for a non-smoker: $", round(nonsmk_ch/non_smkrs, 3), "\n")
        

    # function to find each unique region patients are from
    def unique_regions(self):
        unique_regions = []
        for region in self.patients_regions:
            if region not in unique_regions: 
                unique_regions.append(region)
        
        print("----------------------------------------------------------------------")
        print("UNIQUE REGIONS IN THE DATASET\n")
        print (unique_regions)

    # method to find average yearly medical charges for patients in insurance.csv
    def charges_stats(self):
        #Calculating mean, variance and standard deviation of total charges of all people in the dataset
        mean = round(statistics.mean(insurance_charges), 2)
        variance = round(statistics.pvariance(insurance_charges), 2)
        st_dev = round(statistics.pstdev(insurance_charges), 2)

        print("----------------------------------------------------------------------")
        print("ANNUAL CHARGES STATS\n")
        print("Annual charges':")
        print("    Mean: ", mean)
        print("    Variance: ", variance)
        print("    Standard Deviation: ", st_dev)
        print("----------------------------------------------------------------------")


    # method to create dictionary with all patients information
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary["sex"] = self.patients_sexes
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_num_children
        self.patients_dictionary["smoker"] = self.patients_smoker_statuses
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = self.patients_charges
        return self.patients_dictionary

# creating an instance of PatientsInfo class to call different function on the dataset
patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

# calling all functions to analyze the dataset with respect to different attributes
patient_info.analyze_ages()
patient_info.analyze_sexes()
patient_info.analyze_bmi()
patient_info.analyze_smokers()
patient_info.unique_regions()
patient_info.charges_stats()
PatDict=patient_info.create_dictionary()