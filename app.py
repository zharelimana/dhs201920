import streamlit as st  # pyright: ignore[reportMissingImports]
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Welcome message
st.title("Welcome to the DHS Data Analysis dashboard and Insights portal")
# Load the dataset
try:
    data = pd.read_csv('dsh201929cln.csv')  # use forward slash (or right click the file and copy relative path and paste between '')
except Exception as e:
    st.error("Failed to load dataset. Please check the file path.")
    st.stop()

# Add a sidebar for user input
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Background", "Summary categorical","Summary numerical", "Visualization"])

# Page Routing
if page == 'Background':
    st.markdown("<h2 style='color: blue;'>Rwanda Demographic and Health Analysis 2019-2020</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: green;'>Demographic and Health (DH) analysis involves the comprehensive study of a population's health, fertility, and related demographic factors through nationally representative surveys, ideally conducted every five years. Key areas of analysis include maternal and child health, nutrition, family planning, HIV/AIDS, and household conditions, providing essential data to inform and evaluate national and international health policies and development programs..</p>", unsafe_allow_html=True)
    #st.header("Rwanda Demographic and Health Analysis 2019-2020")
    st.write("<p style='color: orange;'>The main advantages of Demographic and Health Surveys (DHS) are their national scope, high data quality, and standardized methodology across countries, enabling robust analysis of population health, fertility, and mortality trends over time and for comparisons between regions and countries. Key benefits include providing data where it's lacking, supporting program evaluation, and generating indicators for national and global goals like the SDGs</p>", unsafe_allow_html=True)
    
elif page == 'Summary categorical':
    st.header('categorical data Analysis')
    st.write("Explore the dataset and gain insights into population Demographic and Health information.")
    # Categorical variable distribution

    # Identify categorical columns
    sdata=data[['sample domain', 'region', 'type of place of residence', 'sex of household head', 'occupation', 'educational level', 'literacy', 'has an account in a bank or other financial institution', 'use of internet', 'covered by health insurance', 'current contraceptive method', 'respondent circumcised', 'ever been tested for hiv', 'tuberculosis spread by:']]
    categorical_cols = sdata.select_dtypes(include=['object','category']).columns.tolist()
    #if categorical_cols:
    selected_col = st.selectbox("Select a categorical column", categorical_cols)

        #if selected_col:
    # Count the frequency of each category
    category_counts = sdata[selected_col].value_counts()

            # Plot using seaborn
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=category_counts.index, y=category_counts.values, ax=ax)
    ax.set_title(f"Distribution of participants by '{selected_col}'")
    ax.set_xlabel(selected_col)
    ax.set_ylabel("Count")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Tabulation of participants by educational level
    freq = sdata[selected_col].value_counts()
    percent = sdata[selected_col].value_counts(normalize=True) * 100

    # Combine and format
    table = pd.DataFrame({'Frequency': freq, 'Percentage (%)': percent.round(2)})
    #print(table.to_string())

    # Display the table with tabulate
    st.dataframe(table.reset_index()) #, headers=['SN','Category', 'Frequency', 'Percentage (%)'], tablefmt='grid')


elif page == 'Summary numerical':
    st.header('numerical data Analysis')
    st.write("Explore the dataset and gain insights into population Demographic and Health information.")


    dsdata=data[['current age', 'number of household members (total listed)', 'age of household head', 'total children ever born', 'number of living children', 'ideal number of children', 'age at circumcision']]
    numeric_columns = dsdata.select_dtypes(include=['float64', 'int64']).columns

    # Let user select a column
    selected_column = st.selectbox("Select a variable for description", numeric_columns)

    # Plotting the selected column as a histogram
    st.subheader(f"Description for '{selected_column}'")
   
    #st.dataframe(data.describe())
    st.dataframe(dsdata[selected_column].describe())
    
    # Display basic statistics one by one
    ## st.subheader("Basic statistics for Age:")
    ## st.dataframe(data.describe())
    ##st.dataframe(data['current age'].describe())
    ##st.dataframe(data['current age'].shape)

    st.subheader("Correlation Matrix among numerical variables:")
    
    corr = data.corr(numeric_only=True)
    
    # Plot the heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    plt.title("Correlation Matrix Heatmap")
    st.pyplot(fig)

elif page == 'Visualization':
    st.header('Visualization')
    st.write("Visualize the data to understand trends and patterns.")
    # Add your plots here later

    # Filter numeric columns for plotting
    vsdata=data[['current age', 'number of household members (total listed)', 'age of household head', 'total children ever born', 'number of living children', 'ideal number of children', 'age at circumcision']]
    numeric_columns = vsdata.select_dtypes(include=['float64', 'int64']).columns

    # Let user select a column
    selected_column = st.selectbox("Select a numeric column to plot", numeric_columns)

    # Plotting the selected column as a histogram
    st.subheader(f"Histogram of '{selected_column}'")

    fig, ax = plt.subplots()
    ax.hist(vsdata[selected_column], bins=20, color='skyblue', edgecolor='black')
    ax.set_xlabel(selected_column)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
    #st.write(data[selected_column].describe())
    #st.write(f"Summary Statistics of {data[selected_column].describe()}'")
    st.write(f"Summary Statistics for {selected_column} Variable: {vsdata[selected_column].describe()}'")
    # Draw boxplot
    st.subheader(f"Boxplot of '{selected_column}'")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(vsdata[selected_column], ax=ax)
    plt.title(f"'{selected_column}'Boxplot")
    st.pyplot(fig)

else:
    st.write("Please select a valid page from the sidebar.")

