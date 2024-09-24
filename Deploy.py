import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configure the page layout
st.set_page_config(layout="wide")

# Load data
file = r'C:\Users\amuthumanikandan\OneDrive - athenahealth\Audit\SQL Doc\Grow data skills\Class 15 Python\Class_Project\CLASS6\Diwali Sales Data.csv'
df = pd.read_csv(file, encoding='unicode_escape')

# Drop unwanted columns
df.drop(['Status', 'Unnamed'], axis=1, inplace=True)

# Filter rows with at least one null value
rowwithnulls = df[df.isnull().any(axis=1)]
st.write("Rows with null values")
st.write(rowwithnulls)

# Fill missing 'Amount' values with the mean of the respective 'Product_Category'
df['Amount'] = df.groupby('Product_Category')['Amount'].transform(lambda x: x.fillna(x.mean()))

# Rename 'Maritial_Status' column to 'Married'
df.rename(columns={'Maritial_Status': 'Married'}, inplace=True)

# Create age categories
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
        return '55+'

df['Age_Group'] = df['Age'].apply(categorize_age)

st.write("Data Overview")
st.write(df)

# Gender count plot
st.subheader("Gender Count Plot")
fig, ax = plt.subplots()
sns.countplot(x='Gender', data=df, ax=ax)
for bars in ax.containers:
    ax.bar_label(bars)
st.pyplot(fig)

# Gender vs. Total Amount bar chart
st.subheader("Gender vs. Total Amount")
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
fig, ax = plt.subplots()
sns.barplot(x='Gender', y='Amount', data=sales_gen, ax=ax)
for index, row in sales_gen.iterrows():
    ax.text(row.name, row['Amount'], round(row['Amount'], 2), color='black', ha="center", va="bottom")
st.pyplot(fig)

# Age Group distribution pie chart
st.subheader("Age Group Distribution")
age_group_counts = df['Age_Group'].value_counts()
fig, ax = plt.subplots()
age_group_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax)
ax.set_ylabel('')
ax.set_title('Age Category-wise Contribution')
st.pyplot(fig)

# Age Group vs. Gender count plot
st.subheader("Age Group vs. Gender")
fig, ax = plt.subplots()
sns.countplot(data=df, x='Age_Group', hue='Gender', ax=ax)
for bars in ax.containers:
    ax.bar_label(bars)
st.pyplot(fig)

# Top 10 states by orders bar chart
st.subheader("Top 10 States by Orders")
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
fig, ax = plt.subplots(figsize=(16, 5))
sns.barplot(data=sales_state, x='State', y='Orders', ax=ax)
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 9), textcoords='offset points')
st.pyplot(fig)

# Scatter plot of Amount vs. State for Top 10 States
st.subheader("Scatter Plot: Amount vs. State for Top 10 States")
state_amount = df.groupby('State')['Amount'].sum().sort_values(ascending=False).head(10)
top_10_states_data = df[df['State'].isin(state_amount.index)]
fig, ax = plt.subplots(figsize=(15, 6))
ax.scatter(top_10_states_data['State'], top_10_states_data['Amount'], alpha=0.7)
ax.set_title('Scatter Plot of Amount vs State for Top 10 States')
ax.set_xlabel('State')
ax.set_ylabel('Amount')
ax.grid(True)
st.pyplot(fig)

# Subplots for Top 5 States
st.subheader("Top 5 States: Histogram and Scatter Plot")
state_amount = df.groupby('State')['Amount'].sum().sort_values(ascending=False).head(5)
top_5_states_data = df[df['State'].isin(state_amount.index)]

fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Histogram
axs[0].hist(df['State'], bins=range(1, 6), edgecolor='black')
axs[0].set_title('Histogram of States')
axs[0].set_xlabel('State')
axs[0].set_ylabel('Frequency')
axs[0].set_xticks(range(1, 6))
axs[0].grid(True)

# Scatter plot
axs[1].scatter(top_5_states_data['State'], top_5_states_data['Amount'], alpha=0.7)
axs[1].set_title('Scatter Plot of Top 5 States vs Amount')
axs[1].set_xlabel('State')
axs[1].set_ylabel('Amount')
axs[1].grid(True)

plt.tight_layout()
st.pyplot(fig)
