#import python libraries
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns

#Importing file
file = r'C:\Users\amuthumanikandan\OneDrive - athenahealth\Audit\SQL Doc\Grow data skills\Class 15 Python\Class_Project\CLASS6\Diwali Sales Data.csv'
df = pd.read_csv(file,encoding='unicode_escape')

df.drop(['Status','Unnamed'],axis=1,inplace=True)

#filtering rows with null atleast one null value
rowwithnulls = df[df.isnull().any(axis = 1)]
print("Rows with null")
print(rowwithnulls)

df['Amount'] = df.groupby('Product_Category')['Amount'].transform(lambda x:x.fillna(x.mean()))

df.rename(columns = {'Maritial_Status': 'Married'})

def categorize_age(age):
    if age <= 17:
        return '0-17'
    elif age <= 25:
        return '18-25'
    elif age <= 35:
        return '26-35'
    elif age <= 45:
        return '36-45'
    elif age <= 50:
        return '46-50'
    elif age <= 55:
        return '51-55'
    else:
        return '55+'#creating age category

df['Age_Group'] = df['Age'].apply(categorize_age)
print(df)

ax = sns.countplot(x='Gender',data = df)

ax = sns.countplot(x='Gender',data = df)
for bars in ax.containers:
    ax.bar_label(bars)

df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)

# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)

# Grouping, summing, and sorting the data by 'Amount'
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

# Creating the bar plot
sns.barplot(x='Gender', y='Amount', data=sales_gen)

# Adding data labels on each bar
for index, row in sales_gen.iterrows():
    plt.text(row.name, row['Amount'], round(row['Amount'], 2), color='black', ha="center", va="bottom")

# Displaying the plot
plt.show()

age_group_counts = df['Age_Group'].value_counts()
age_group_counts.plot(kind='pie',autopct='%1.1f%%',title='Agecategorywise_contribution')
plt.ylabel('')
plt.show()

ax = sns.countplot(data = df, x = 'Age_Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# Grouping and sorting the data by 'Orders', then selecting the top 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

# Setting the figure size
sns.set(rc={'figure.figsize': (16, 5)})

# Creating the bar plot
ax = sns.barplot(data=sales_state, x='State', y='Orders')

# Adding data labels on each bar
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center', va = 'center',
                xytext = (0, 9),
                textcoords = 'offset points')

# Displaying the plot
plt.show()


# Step 1: Group by 'State' and sum the 'Amount'
state_amount = df.groupby('State')['Amount'].sum().sort_values(ascending=False).head(10)

# Step 2: Filter original DataFrame for only the top 10 states
top_10_states_data = df[df['State'].isin(state_amount.index)]

# Step 3: Create the scatter plot
plt.figure(figsize=(15, 6))
plt.scatter(top_10_states_data['State'], top_10_states_data['Amount'], alpha=0.7)
plt.title('Scatter Plot of Amount vs State for Top 10 States')
plt.xlabel('State')
plt.ylabel('Amount')
plt.grid(True)
plt.show()

# Step 1: Group by 'State' and sum the 'Amount', then get the top 5 states
state_amount = df.groupby('State')['Amount'].sum().sort_values(ascending=False).head(5)

# Step 2: Filter the original DataFrame for the top 5 states
top_5_states_data = df[df['State'].isin(state_amount.index)]

# Step 3: Create the subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Histogram (unchanged)
axs[0].hist(df['State'], bins=range(1, 6), edgecolor='black')
axs[0].set_title('Histogram of States')
axs[0].set_xlabel('State')
axs[0].set_ylabel('Frequency')
axs[0].set_xticks(range(1, 6))
axs[0].grid(True)

# Scatter plot (filtered for top 5 states)
scatter = axs[1].scatter(top_5_states_data['State'], top_5_states_data['Amount'], alpha=0.7)
axs[1].set_title('Scatter Plot of Top 5 States vs Amount')
axs[1].set_xlabel('State')
axs[1].set_ylabel('Amount')
axs[1].grid(True)

plt.tight_layout()
plt.show()



