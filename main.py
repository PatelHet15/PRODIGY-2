import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'lung_cancer.csv'
data = pd.read_csv(file_path)

# Data Cleaning
# Check for missing values
missing_values = data.isnull().sum()

# Ensure correct data types
data['diagnosis_date'] = pd.to_datetime(data['diagnosis_date'])
data['end_treatment_date'] = pd.to_datetime(data['end_treatment_date'])
data['hypertension'] = data['hypertension'].astype('category')
data['asthma'] = data['asthma'].astype('category')
data['cirrhosis'] = data['cirrhosis'].astype('category')
data['other_cancer'] = data['other_cancer'].astype('category')
data['survived'] = data['survived'].astype('category')

# Summary statistics
summary_stats = data.describe()

# Distribution of numerical variables
numerical_cols = ['age', 'bmi', 'cholesterol_level']
data[numerical_cols].hist(bins=15, figsize=(15, 6), layout=(2, 2))

for ax, col in zip(plt.gcf().axes, numerical_cols):
    ax.set_xlabel(col)
    ax.set_ylabel('Frequency')
plt.tight_layout()
plt.show()

# Distribution of categorical variables
categorical_cols = ['gender', 'country', 'cancer_stage', 'family_history', 'smoking_status', 'treatment_type', 'survived']
for col in categorical_cols:
    plt.figure(figsize=(10, 4))
    sns.countplot(data[col])
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Count')
    plt.show()

# Correlation matrix for numerical variables
corr_matrix = data[numerical_cols].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.xlabel('Variables')
plt.ylabel('Variables')
plt.show()

# Explore relationships between variables
Age vs BMI
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='bmi', hue='survived', data=data)
plt.title('Age vs BMI')
plt.xlabel('Age')
plt.ylabel('BMI')
plt.show()

# Age vs Cholesterol Level
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='cholesterol_level', hue='survived', data=data)
plt.title('Age vs Cholesterol Level')
plt.xlabel('Age')
plt.ylabel('Cholesterol Level')
plt.show()

# BMI vs Cholesterol Level
plt.figure(figsize=(10, 6))
sns.scatterplot(x='bmi', y='cholesterol_level', hue='survived', data=data)
plt.title('BMI vs Cholesterol Level')
plt.xlabel('BMI')
plt.ylabel('Cholesterol Level')
plt.show()

# Cancer stage vs survival rate
plt.figure(figsize=(10, 6))
sns.countplot(x='cancer_stage', hue='survived', data=data)
plt.title('Cancer Stage vs Survival Rate')
plt.xlabel('Cancer Stage')
plt.ylabel('Count')
plt.show()

# Smoking status vs survival rate
plt.figure(figsize=(10, 6))
sns.countplot(x='smoking_status', hue='survived', data=data)
plt.title('Smoking Status vs Survival Rate')
plt.xlabel('Smoking Status')
plt.ylabel('Count')
plt.show()

# Treatment type vs survival rate
plt.figure(figsize=(10, 6))
sns.countplot(x='treatment_type', hue='survived', data=data)
plt.title('Treatment Type vs Survival Rate')
plt.xlabel('Treatment Type')
plt.ylabel('Count')
plt.show()

# Further Analysis
# Age distribution by gender
plt.figure(figsize=(10, 6))
sns.histplot(data, x='age', hue='gender', multiple='stack', bins=15)
plt.title('Age Distribution by Gender')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# BMI distribution by gender
plt.figure(figsize=(10, 6))
sns.histplot(data, x='bmi', hue='gender', multiple='stack', bins=15)
plt.title('BMI Distribution by Gender')
plt.xlabel('BMI')
plt.ylabel('Count')
plt.show()

# Cholesterol Level distribution by gender
plt.figure(figsize=(10, 6))
sns.histplot(data, x='cholesterol_level', hue='gender', multiple='stack', bins=15)
plt.title('Cholesterol Level Distribution by Gender')
plt.xlabel('Cholesterol Level')
plt.ylabel('Count')
plt.show()

# Treatment type distribution by cancer stage
plt.figure(figsize=(10, 6))
sns.countplot(x='treatment_type', hue='cancer_stage', data=data)
plt.title('Treatment Type Distribution by Cancer Stage')
plt.xlabel('Treatment Type')
plt.ylabel('Count')
plt.show()

# Hypertension vs survival rate
plt.figure(figsize=(10, 6))
sns.countplot(x='hypertension', hue='survived', data=data)
plt.title('Hypertension vs Survival Rate')
plt.xlabel('Hypertension')
plt.ylabel('Count')
plt.show()

# Asthma vs survival rate
plt.figure(figsize=(10, 6))
sns.countplot(x='asthma', hue='survived', data=data)
plt.title('Asthma vs Survival Rate')
plt.xlabel('Asthma')
plt.ylabel('Count')
plt.show()

# Cirrhosis vs survival rate
plt.figure(figsize=(10, 6))
sns.countplot(x='cirrhosis', hue='survived', data=data)
plt.title('Cirrhosis vs Survival Rate')
plt.xlabel('Cirrhosis')
plt.ylabel('Count')
plt.show()

# Other cancer vs survival rate
plt.figure(figsize=(10, 6))
sns.countplot(x='other_cancer', hue='survived', data=data)
plt.title('Other Cancer vs Survival Rate')
plt.xlabel('Other Cancer')
plt.ylabel('Count')
plt.show()

# Insights on specific countries
country_summary = data.groupby('country').agg({
    'age': ['mean', 'std'],
    'bmi': ['mean', 'std'],
    'cholesterol_level': ['mean', 'std'],
    'survived': ['mean']
}).reset_index()

# Display results
print("Missing Values:\n", missing_values)
print("\nSummary Statistics:\n", summary_stats)
print("\nCountry Summary:\n", country_summary)
