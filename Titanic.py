#Titanic Dataset Analisys

import pandas as pd
import matplotlib.pyplot as plt # Necessary libraries

pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns

# Load and read dataset
df = pd.read_csv("C:\\Users\\pc\\Desktop\\PYTHON PROJECT\\DATA_SCIENTIST\\train.csv")
#print(df.head())
#print(df.shape)
#print(df.columns)
#print(df.info())
#print(df.describe())
#print(df.isnull().sum()) # Check for missing values in each column
df.drop(columns=["Cabin"], inplace=True) # Drop the "Cabin" column,which is not useful for the analisys 
df["Age"].fillna(df["Age"].mean(), inplace=True) # Clean the "Age" column by filling missing values
df= df[df["Embarked"].notnull()] # Remove rows with missing values in "Embarked" column
#correlation = df.corr(numeric_only=True) Check the correlations 
#print(correlation["Survived"].sort_values(ascending=False)) print the correlation values between "Survived" and the other columns

# "Pclass" is a non-human attribute with strong correlation to survival

#print(df["Pclass"].value_counts()) check the number of passengers in each class 
#print(df.groupby("Pclass")["Age"].mean()) View the mean age for each class
#print(df.groupby("Survived")["Sex"].count()) View the amount of survivors by gender
# The 'Survived' column indicates survival status: 1 means the passenger survived, 0 means they did not survive.
#print(df.groupby("Sex")["Survived"].mean()) View the survival rate by gender
#print(df.groupby(["Pclass", "Sex", "Survived"]).size()) Check the number of survivors by class and gender
#print(df.groupby(["Pclass", "Sex"])["Survived"].mean() * 100) Calculate the survival percentage by class and gender

# Divide the "Age" column into three age groups: under 25, under 50, over 50
age_bins = [0, 25, 50, float('inf')]
age_labels = ['<25', '<50', '>50']
df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

# Group by "Pclass","Sex", and "AgeGroup" for survived passengers
survived_group = (df[df["Survived"] == 1].groupby(["Pclass", "Sex", "AgeGroup"]).size()) # Apply the "AgeGroup" segmentation to the survivors
survived_table = survived_group.unstack(level=["AgeGroup"])
#print(survived_table) Display the number of survivors by class, gender and age group
totali = df.groupby(["Pclass","Sex","AgeGroup"]).size().unstack(level=["AgeGroup"])
percentuali_survived = (survived_table/totali)*100
percentuali_survived = percentuali_survived.round(2)
print(percentuali_survived)


# Plot the percentage of survived passengers per class, per gender, and per age group
ax = percentuali_survived.plot(kind="bar", figsize=(15, 6), color=["skyblue", "lightgreen", "salmon"], edgecolor="black")
# Add percentage labels on each bar
for container in ax.containers:
	ax.bar_label(container, fmt='%.1f%%', label_type='edge', fontsize=7, padding=3)
plt.title("Survival Rate by Class, Gender and Age Group")
plt.xlabel("Class and Gender")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Age Group")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()



