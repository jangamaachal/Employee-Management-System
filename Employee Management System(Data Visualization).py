#!/usr/bin/env python
# coding: utf-8

# In[17]:


# import all relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt       #visualizing the data
import seaborn as sns


# In[18]:


# import csv file

data = pd.read_csv("C:/Users/janga/OneDrive/Desktop/Anudip-C8906/Python/Labs/employee_data.csv", encoding = "unicode_escape")


# In[19]:


# Shape of Data file

data.shape


# In[20]:


# First five data (rows)

data.head(5)


# In[21]:


# count of columns and Datatype
data.info()


# In[22]:


# Show the columns in employee data file

data.columns


# In[23]:


# Duplicate Values

import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/janga/OneDrive/Desktop/Anudip-C8906/Python/Labs/employee_data.csv")

# Check the columns to find the correct one
print(df.columns)

# Find duplicate rows based on all columns
duplicates = df[df.duplicated()]

# If you want to find duplicates in a specific column (replace 'Employee_ID' with your actual column name)
duplicates_column = df[df['EmpID'].duplicated()]  # Replace 'Employee_ID' with your column name

# Count the number of duplicates in the entire DataFrame
duplicates_count = df.duplicated().sum()

# Print results
print("\nDuplicates in the entire DataFrame:")
print(duplicates)

print("\nDuplicates in a specific column:")
print(duplicates_column)

print(f"\nTotal number of duplicate rows: {duplicates_count}")



# In[24]:


# rename the Column in the given data
data.rename(columns={"ADEmail":"Emp_Email"})


# In[25]:


import pandas as pd

# Load your dataset
df = pd.read_csv("C:/Users/janga/OneDrive/Desktop/Anudip-C8906/Python/Labs/employee_data.csv")

# Check the first few rows to understand the data structure
print(df.head())

# Convert 'employee_status' (categorical) to numeric. 
# You may need to replace 'Active' and 'Inactive' with your actual column values.
df['employee_status_numeric'] = df['EmployeeStatus'].map({'Active': 1, 'Inactive': 0})

# Check if the conversion was successful
print(df[['EmployeeStatus', 'employee_status_numeric']].head())

# Calculate the correlation between employee status and performance
# Replace 'performance' with the actual column name for performance in your dataset
correlation = df['employee_status_numeric'].corr(df['Performance Score'])

# Print the correlation value
print(f"Correlation between EmployeeStatus and Performance Score: {correlation}")


# In[26]:


data.describe


# In[27]:


# describe the value for specific columns
data[['EmployeeClassificationType', 'EmployeeStatus', 'Title']].describe()


# # Exploratory Data Analysis

# In[28]:


# 1.What is the distribution of Performance Scores (e.g., "Fully Meets," "Exceeds," etc.) among employees?

import matplotlib.pyplot as plt
import seaborn as sns

# Set the visual style
sns.set(style="whitegrid")

# Plot the distribution of Performance Scores
plt.figure(figsize=(10, 6))
ax = sns.countplot(data=data, x='Performance Score', palette='viridis', order=data['Performance Score'].value_counts().index)

# Add labels and title
plt.title('Distribution of Performance Scores', fontsize=16)
plt.xlabel('Performance Score', fontsize=12)
plt.ylabel('Count of Employees', fontsize=12)

# Annotate the bars with counts
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=11, color='black', xytext=(0, 5),
                textcoords='offset points')

# Display the plot
plt.show()


# In[29]:


# 2. How do Performance Scores vary across different JobFunctionDescriptions?
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Performance Scores across JobFunctionDescriptions
plt.figure(figsize=(14, 8))
ax2 = sns.countplot(data=data, x='JobFunctionDescription', hue='Performance Score', palette='viridis')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add labels and title
plt.title('Performance Scores by Job Function Descriptions', fontsize=16)
plt.xlabel('Job Function Description', fontsize=12)
plt.ylabel('Count of Employees', fontsize=12)

# Add legend
plt.legend(title='Performance Score', loc='upper right')

# Display the plot
plt.show()


# In[30]:


# 3. Divisions with the highest proportion of "Exceeds" or "Fully Meets" Performance Scores
plt.figure(figsize=(12, 6))
filtered_data = data[data['Performance Score'].isin(['Exceeds', 'Fully Meets'])]
proportion_data = filtered_data['Division'].value_counts(normalize=True) * 100

# Plot proportions
ax3 = sns.barplot(x=proportion_data.index, y=proportion_data.values, palette='viridis')

# Add labels and title
plt.title('Proportion of Employees with "Exceeds" or "Fully Meets" Performance Scores by Division', fontsize=16)
plt.xlabel('Division', fontsize=12)
plt.ylabel('Percentage of Employees (%)', fontsize=12)

# Annotate the bars with percentages
for p in ax3.patches:
    ax3.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='center', fontsize=11, color='black', xytext=(0, 5),
                 textcoords='offset points')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the plot
plt.show()


# In[31]:


# 4. Distribution of employees by GenderCode


plt.figure(figsize=(8, 8))
gender_counts = data['GenderCode'].value_counts()

def plot_gender_distribution():
    # Pie chart
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Distribution of Employees by GenderCode', fontsize=16)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

plot_gender_distribution()


# In[32]:


#5. How many employees are located in each State?
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data: Number of employees in each state
data = {
    'State': ['California', 'Texas', 'New York', 'Florida', 'Illinois'],
    'Employees': [120, 95, 110, 80, 70]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(df['Employees'], labels=df['State'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', len(df)))
plt.title('Employee Distribution by State', fontsize=14)
plt.show()


# In[33]:


#6. Distribution od employees acoording to state and department.
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data: Number of employees in each state
data = {
    'State': ['California', 'Texas', 'New York', 'Florida', 'Illinois'],
    'Employees': [120, 95, 110, 80, 70]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Example: Employees split into categories (e.g., Departments)
df['IT'] = [40, 30, 50, 20, 15]
df['HR'] = [30, 20, 30, 25, 20]
df['Finance'] = [50, 45, 30, 35, 35]

# Plot stacked bar chart
df.plot(x='State', kind='bar', stacked=True, figsize=(8, 5), color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title('Number of Employees by State and Department', fontsize=14)
plt.xlabel('State', fontsize=12)
plt.ylabel('Number of Employees in Percentage', fontsize=12)
plt.legend(title='Department')
plt.show()


# In[34]:


# Dot Plot
plt.figure(figsize=(8, 5))
sns.stripplot(x='Employees', y='State', data=df, color='purple', size=10)
plt.title('Employee Distribution (Dot Plot)', fontsize=14)
plt.xlabel('Number of Employees in Perccentage{}', fontsize=12)
plt.ylabel('State', fontsize=12)
plt.show()


# In[35]:


# 7.What is the distribution of employees across different PayZones?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example data: Replace this with your actual dataset
data = {
    'EmployeeID': [1, 2, 3, 4, 5, 6, 7, 8],
    'PayZone': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Count the number of employees in each PayZone
payzone_counts = df['PayZone'].value_counts()

# Plot the distribution of employees across PayZones
plt.figure(figsize=(8, 5))
sns.barplot(x=payzone_counts.index, y=payzone_counts.values, palette='viridis')
plt.title('Distribution of Employees Across PayZones', fontsize=16)
plt.xlabel('PayZone', fontsize=14)
plt.ylabel('Number of Employees in Percentage', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()


# In[36]:


# 8.How do EmployeeType (Full-Time vs. Contract) employees compare across PayZones or Divisions?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example data: Replace this with your actual dataset
data = {
    'EmployeeID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'PayZone': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Division': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'HR', 'Finance', 'IT', 'HR'],
    'EmployeeType': ['Full-Time', 'Contract', 'Full-Time', 'Contract', 'Contract', 'Full-Time', 'Contract', 'Full-Time', 'Contract', 'Full-Time']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group data by PayZone and EmployeeType
payzone_comparison = df.groupby(['PayZone', 'EmployeeType'])['EmployeeID'].count().unstack().fillna(0)

# Visualization: Grouped bar chart for PayZones
payzone_comparison.plot(kind='bar', figsize=(10, 6), color=['#1f77b4', '#ff7f0e'])
plt.title('Comparison of EmployeeType Across PayZones', fontsize=16)
plt.xlabel('PayZone', fontsize=14)
plt.ylabel('Number of Employees', fontsize=14)
plt.xticks(rotation=0, fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='EmployeeType', fontsize=12)
plt.show()

# Group data by Division and EmployeeType
division_comparison = df.groupby(['Division', 'EmployeeType'])['EmployeeID'].count().unstack().fillna(0)

# Visualization: Grouped bar chart for Divisions
division_comparison.plot(kind='bar', figsize=(10, 6), color=['#2ca02c', '#d62728'])
plt.title('Comparison of EmployeeType Across Divisions', fontsize=16)
plt.xlabel('Division', fontsize=14)
plt.ylabel('Number of Employees in percentage', fontsize=14)
plt.xticks(rotation=0, fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='EmployeeType', fontsize=12)
plt.show()


# In[37]:


# 9.How do Performance Scores vary across different PayZones?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example data: Replace this with your actual dataset
data = {
    'EmployeeID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'PayZone': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'PerformanceScore': [85, 78, 92, 88, 76, 95, 80, 89, 77, 93]
}

# Create a DataFrame
df = pd.DataFrame(data)

### Grouped Bar Chart: Average Performance Score per PayZone
# Calculate mean performance score for each PayZone
avg_scores = df.groupby('PayZone')['PerformanceScore'].mean()

# Plot grouped bar chart
plt.figure(figsize=(8, 5))
sns.barplot(x=avg_scores.index, y=avg_scores.values, palette='Blues_d')
plt.title('Average Performance Scores Across PayZones', fontsize=16)
plt.xlabel('PayZone', fontsize=14)
plt.ylabel('Average Performance Score', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

### Box Plot: Distribution of Performance Scores Across PayZones
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='PayZone', y='PerformanceScore', palette='Set3')
plt.title('Performance Score Distribution Across PayZones', fontsize=16)
plt.xlabel('PayZone', fontsize=14)
plt.ylabel('Performance Score', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()


# In[38]:


# 10.How does employee count differ across Divisions and JobFunctionDescription?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example data: Replace this with your actual dataset
data = {
    'EmployeeID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Division': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'HR', 'Finance', 'IT', 'HR'],
    'JobFunctionDescription': ['Recruiting', 'Support', 'Accounting', 'Development', 'Recruiting',
                                'Accounting', 'Training', 'Accounting', 'Development', 'Training']
}

# Create a DataFrame
df = pd.DataFrame(data)

### Count employees by Division and JobFunctionDescription
employee_counts = df.groupby(['Division', 'JobFunctionDescription'])['EmployeeID'].count().unstack().fillna(0)

### Heatmap: Visualizing employee count
plt.figure(figsize=(10, 6))
sns.heatmap(employee_counts, annot=True, fmt='.0f', cmap='Blues', cbar=True)
plt.title('Employee Count Across Divisions and Job Functions', fontsize=16)
plt.xlabel('Job Function Description', fontsize=14)
plt.ylabel('Division', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.show()

### Grouped Bar Chart: Employee Count by Division and JobFunctionDescription
employee_counts = df.groupby(['Division', 'JobFunctionDescription'])['EmployeeID'].count().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(data=employee_counts, x='Division', y='EmployeeID', hue='JobFunctionDescription', palette='muted')
plt.title('Employee Count by Division and Job Function', fontsize=16)
plt.xlabel('Division', fontsize=14)
plt.ylabel('Employee Count in Percent', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Job Function', fontsize=12)
plt.show()


# In[44]:


# 11.What is the distribution of EmployeeStatus (e.g., Active, Inactive)?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example data: Replace this with your actual dataset
data = {
    'EmployeeID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'EmployeeStatus': ['Active', 'Active', 'Inactive', 'Active', 'Active', 'Inactive', 'Active', 'Inactive', 'Active', 'Inactive']
}

# Create a DataFrame
df = pd.DataFrame(data)

### Calculate the distribution of EmployeeStatus
status_counts = df['EmployeeStatus'].value_counts()

### Bar Chart: Distribution of EmployeeStatus
plt.figure(figsize=(8, 5))
sns.barplot(x=status_counts.index, y=status_counts.values, palette='viridis')
plt.title('Distribution of EmployeeStatus', fontsize=16)
plt.xlabel('Employee Status', fontsize=14)
plt.ylabel('Number of Employees in Percentage', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

### Pie Chart: Distribution of EmployeeStatus
plt.figure(figsize=(6, 6))
plt.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%', startangle=140, colors=("pink","yellow"))
plt.title('EmployeeStatus Distribution', fontsize=16)
plt.show()


# In[40]:


# 12.What are the most common JobFunctionDescriptions within each Division?
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example data: Replace this with your actual dataset
data = {
    'EmployeeID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Division': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'HR', 'Finance', 'IT', 'HR'],
    'JobFunctionDescription': ['Recruiting', 'Support', 'Accounting', 'Development', 'Recruiting',
                                'Accounting', 'Training', 'Accounting', 'Development', 'Training']
}

# Create a DataFrame
df = pd.DataFrame(data)

### Identify the most common JobFunctionDescription within each Division
most_common_jobfunc = (
    df.groupby(['Division', 'JobFunctionDescription'])
    .size()
    .reset_index(name='Count')
    .sort_values(['Division', 'Count'], ascending=[True, False])
    .groupby('Division')
    .head(1)  # Keep only the top JobFunctionDescription for each Division
)

print("Most Common JobFunctionDescription Within Each Division:")
print(most_common_jobfunc)

### Visualization: Bar Chart of Most Common Job Functions per Division
plt.figure(figsize=(10, 6))
sns.barplot(data=most_common_jobfunc, x='Division', y='Count', hue='JobFunctionDescription', palette='muted')
plt.title('Most Common JobFunctionDescriptions in Each Division', fontsize=16)
plt.xlabel('Division', fontsize=14)
plt.ylabel('Employee Count in Percent', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Job Function', fontsize=12)
plt.show()


# In[45]:


# 13.Which States have the highest count of Performance Score = Exceeds employees?

import pandas as pd
import matplotlib.pyplot as plt

# Example data: Replace this with your actual dataset
data = {
    'EmployeeID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'State': ['CA', 'NY', 'TX', 'CA', 'NY', 'TX', 'CA', 'NY', 'TX', 'CA'],
    'PerformanceScore': ['Exceeds', 'Meets', 'Exceeds', 'Exceeds', 'Meets', 'Exceeds', 'Meets', 'Exceeds', 'Meets', 'Exceeds']
}

# Create a DataFrame
df = pd.DataFrame(data)

### Filter data for Performance Score = "Exceeds"
exceeds_df = df[df['PerformanceScore'] == 'Exceeds']

### Count employees with Performance Score = "Exceeds" by State
state_counts = exceeds_df['State'].value_counts().sort_index()

### Line Chart: States with Highest Count of Exceeds Employees
plt.figure(figsize=(8, 5))
plt.plot(state_counts.index, state_counts.values, marker='o', linestyle='-', color='b')
plt.title('States with the Highest Count of Employees with Performance Score = Exceeds', fontsize=16)
plt.xlabel('State', fontsize=14)
plt.ylabel('Number of Employees in Percentage', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


# In[ ]:




