import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns
import io
# Execute the code from the notebook with exception handling
st.header('Exploratory Data Analysis with Streamlit')

st.write('This is a simple example of a dataframe and a bar chart using Streamlit. Here you can see how easy it is to display a dataframe in Streamlit and how to plot a bar chart for a specific column.Take this data with a grain of salt as it is a corss sectional data. The real value of the data would come from a longitudinal study. The data is generated for the purpose of this example.')
# Define the dataframe 'df' here
df = pd.read_csv('data.txt')
df.set_index('country', inplace=True)
# Display the dataframe using Streamlit
st.dataframe(df)

# Button to show data information
if st.button('Click to show the data information'):
    st.text('DataFrame Info:')
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

# correlation matrix using Streamlit
st.write('Correlation Matrix:')
st.dataframe(df.corr())

# plot the heat map correlation matrix using seaborn
fig, ax = plt.subplots()
sns.heatmap(df.corr(),annot=True, ax=ax)
st.pyplot(fig)

# scatter plot using Streamlit
st.write('Scatter Plot:')
fig, ax = plt.subplots()
df.plot(kind='scatter', x='unemploy_rate', y='poverty_rate', ax=ax)
st.pyplot(fig)

# plot the dataframe using Streamlit where bar chart is plotted for 'population' column
fig, ax = plt.subplots()
bars = ax.bar(df.index, df['poverty_rate'])
figsize = plt.rcParams["figure.figsize"]
figsize[1] = 8
figsize[0] = 15
plt.rcParams["figure.figsize"] = figsize
ax.set_ylabel('Poverty Rate')
ax.set_title('Poverty Rate by Country')
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
st.pyplot(fig)

# Plot the GDP bar chart with country names on top
fig, ax = plt.subplots()
bars = ax.bar(df.index, df['gdp'])
ax.set_ylabel('GDP')
ax.set_title('GDP by Country')
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')
st.pyplot(fig)

# Plot histograms using seaborn
fig, ax = plt.subplots()
sns.histplot(df['mx_tax_rate'], ax=ax, kde=True)
st.pyplot(fig)

fig, ax = plt.subplots()
sns.histplot(df['poverty_rate'], ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
sns.histplot(df['unemploy_rate'], ax=ax)
st.pyplot(fig)

fig, ax = plt.subplots()
sns.histplot(df['inflation'], ax=ax)
st.pyplot(fig)
# plot scatter plot with a regression line using seaborn
fig, ax = plt.subplots()
sns.regplot(x='inflation', y='unemploy_rate', data=df, ax=ax)
st.pyplot(fig)

st.write(' The scatter plot above shows the relationship between inflation and unemployment rate. The regression line shows a positive relationship between inflation and unemployment rate. As inflation increases, the unemployment rate also increases. This is perverse because according to the Phillips curve, there should be a negative relationship between inflation and unemployment rate. This is known as the stagflation phenomenon where inflation and unemployment rate increase simultaneously. ')
