# US Medical Insurance Analysis
In this project, a **CSV** file with medical insurance costs is investigated using Python fundamentals. The goal with this project will be to analyze various attributes within **insurance.csv** to learn more about the patient information in the file and gain insight into potential use cases for the dataset.

First we look through **insurance.csv** in order to get aquanted with the data. The following aspects of the data file will be checked in order to plan out how to import the data into a Python file:

-   The names of columns and rows
-   Any noticeable missing data
-   Types of values (numerical vs. categorical)

**insurance.csv** contains the following columns:

-   Patient Age
-   Patient Sex
-   Patient BMI
-   Patient Number of Children
-   Patient Smoking Status
-   Patient U.S Geopraphical Region
-   Patient Yearly Medical Insurance Cost

There are no signs of missing data. To store this information, seven empty lists are created to hold each individual column of data from **insurance.csv**.

A helper function called `load_list_data()` is created to make loading data into the lists as efficient as possible.

Once all the data from **insurance.csv** is neatly organized into labeled lists, the analysis can be started. There are many aspects of the data that could be looked into. The following operations will be implemented:
-   find average age of the patients and find out if varying age classes have an impact on charges
-   return the number of males vs. females counted in the dataset and to find out if gender has an impact on charges
-  return the number of people in different BMI classes and find out if BMI has an impact on charges
- return the percentage of smokers in the dataset and find out if smoking has an impact on charges
-   find geographical location of the patients
-   return the average yearly medical charges of the patients and their variance and standard deviation
-   creating a dictionary that contains all patient information

To perform these inspections, a class called `PatientsInfo` has been built out which contains fives methods:

-   `analyze_ages()`
-   `analyze_sexes()`
-  `analyze_bmi()`
- `analyze_smokers()`
-   `unique_regions()`
-   `charges_stats()`
-   `create_dictionary()`

After this an instance named `patient_info` of the class `PatientsInfo` is created so that we can use the functions in that class and get some useful insights.

## Analysis

### Analyzing the age attribute
To inspect if age has an impact on charges, the age analysis function is executed like so - `patient_info.analyze_ages()`. The following output is obtained:

`Average Patient Age: 39.21 years`<br />
`Average charges for patients below the age of 20: $ 8407.349`<br />
`Average charges for patients between the age of 20 and 30: $ 9561.751`<br />
`Average charges for patients between the age of 30 and 40: $ 11738.784`<br />
`Average charges for patients between the age of 40 and 50: $ 14399.204`<br />
`Average charges for patients above the age of 50         : $ 17902.552`<br />

As seen from the output above it's clear that there is a pattern in the result, we can see how the annual charges increase with age, hence charges are directly proportional to age. 

### Analyzing the gender attribute
To inspect if gender has an impact on charges, the age analysis function is executed like so - `patient_info.analyze_sexes()`. The following output is obtained:

`Count of females:  662`<br />
&emsp;`Average charge for a female: $ 12569.579`<br />
`Count of males:  676`<br />
&emsp;`Average charge for a male: $ 13956.751`<br />

Here we can see that the number of females and males is almost the same and the average charges for the groups have a small difference. No useful insight can be made from this information.

### Analyzing the BMI attribute
To inspect if BMI has an impact on charges, the age analysis function is executed like so - `patient_info.analyze_bmi()`. The following output is obtained:

`Patients underweight:  20`<br />
&emsp;`Average charges: $ 8852.201`<br />
`Patients healthy weight:  242`<br />
&emsp;`Average charges: $ 10253.277`<br />
`Patients overweight:  242`<br />
&emsp;`Average charges: $ 10253.277`<br />
`Patients obese:  707`<br />
&emsp;`Average charges: $ 15552.335`<br />

As seen from the output above it's clear that there is a pattern in the result, we can see how the annual charges increase with increase in BMI, hence charges are directly proportional to age.  We also observe that the number of obese people in the dataset is more than any other category.

### Analyzing the smoker attribute
To inspect if smoker has an impact on charges, the age analysis function is executed like so - `patient_info.analyze_smokers()`. The following output is obtained:

`Percentage of smokers in dataset:  20.478 %`<br />
&emsp;`Average charge for a smoker: $ 32050.232`<br />
`Percentage of non-smokers in dataset:  79.522 %`<br />
&emsp;`Average charge for a non-smoker: $ 8434.268`<br />

From the output we see that almost 80% of people from the data set smoke. We also observe that there is a big difference of `$ 23615.964` between average charges of a smoker and a non smoker. This tells us that the smoking status of a person drastically impacts charges. 