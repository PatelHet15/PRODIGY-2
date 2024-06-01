# PRODIGY-2
# **Lung Cancer Data Analysis**

This repository contains a comprehensive analysis of a lung cancer dataset. The analysis includes data cleaning, summary statistics, and various visualizations to explore the relationships between different variables. The goal is to identify patterns and trends in the data related to lung cancer.

## **Dataset**
The dataset is stored in a CSV file named **lung_cancer.csv**. The dataset includes the following columns:

- **id**: Patient ID
- **age**: Age of the patient
- **gender**: Gender of the patient
- **country**: Country of residence
- **diagnosis_date**: Date of cancer diagnosis
- **cancer_stage**: Stage of cancer
- **family_history**: Family history of cancer
- **smoking_status**: Smoking status of the patient
- **bmi**: Body Mass Index of the patient
- **cholesterol_level**: Cholesterol level of the patient
- **hypertension**: Hypertension status
- **asthma**: Asthma status
- **cirrhosis**: Cirrhosis status
- **other_cancer**: Other cancer history
- **treatment_type**: Type of treatment received
- **end_treatment_date**: End date of treatment
- **survived**: Survival status

## **Analysis Steps:**

### **1. Data Cleaning:**
Checked for missing values.
Ensured correct data types for all columns.

### **2. Summary Statistics:**
- Provided an overview of numerical columns using descriptive statistics.

### **3. Distribution of Numerical Variables**
- Created histograms for age, bmi, and cholesterol_level.

### **4. Distribution of Categorical Variables**
- Created count plots for gender, country, cancer_stage, family_history, smoking_status, treatment_type, and survived.

### **5. Correlation Matrix**
- Displayed a heatmap of correlations between numerical variables.

### **6. Exploring Relationships Between Variables**
- Scatter plots for Age vs BMI, Age vs Cholesterol Level, and BMI vs Cholesterol Level.
- Count plots for Cancer Stage vs Survival Rate, Smoking Status vs Survival Rate, and Treatment Type vs Survival Rate.

### **7. Further Analysis**
- Histograms of age, bmi, and cholesterol_level distributions by gender.
- Count plots of Treatment Type by Cancer Stage, Hypertension vs Survival Rate, Asthma vs Survival Rate, Cirrhosis vs Survival Rate, and Other Cancer vs Survival Rate.

### **8. Country-Specific Insights**
- Aggregated data for key statistics by country.

## **How to run the analysis**

### **1. Prerequisites**
- Python 3.x
- Required Python libraries: pandas, matplotlib, seaborn

### **2. Installation**
- **Install the required libraries using pip :** pip install pandas matplotlib seaborn

### **3. Run the Script**
- Ensure the dataset file lung_cancer.csv is in the same directory as the script.
- **Then Run by :** python main.py
