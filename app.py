import streamlit as st  # pyright: ignore[reportMissingImports]
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Welcome message
st.title("Welcome to the DHS Data Analysis dashboard and Insights portal")
# Load the dataset
try:
    data = pd.read_csv('Data/dsh201929cln.csv')  # use forward slash (or right click the file and copy relative path and paste between '')
except Exception as e:
    st.error("Failed to load dataset. Please check the file path.")
    st.stop()

# Add a sidebar for user input
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Background", "Summary categorical","Summary numerical", "Visualization"])

# Page Routing
if page == 'Background':
    st.header("Rwanda Demographic and Health Analysis 2019-2020")
    st.write("Demographic and Health (DH) analysis involves the comprehensive study of a population's health, fertility, and related demographic factors through nationally representative surveys, ideally conducted every five years. Key areas of analysis include maternal and child health, nutrition, family planning, HIV/AIDS, and household conditions, providing essential data to inform and evaluate national and international health policies and development programs.")

elif page == 'Summary categorical':
    st.header('categorical data Analysis')
    st.write("Explore the dataset and gain insights into population Demographic and Health information.")
    # Categorical variable distribution

    # Identify categorical columns
    categorical_cols = data.select_dtypes(include=['object','category']).columns.tolist()

    #if categorical_cols:
    selected_col = st.selectbox("Select a categorical column", categorical_cols)

        #if selected_col:
    # Count the frequency of each category
    category_counts = data[selected_col].value_counts()

            # Plot using seaborn
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=category_counts.index, y=category_counts.values, ax=ax)
    ax.set_title(f"Distribution of '{selected_col}'")
    ax.set_xlabel(selected_col)
    ax.set_ylabel("Count")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Tabulate frequency
    freq_table = data[selected_col].value_counts().reset_index()
    freq_table.columns = [selected_col, 'Count']
    # Display table
    st.dataframe(freq_table)

    ## Display variables patterns
    selected_column = st.selectbox("Select a feature you want the description for:", data.columns)
    st.subheader(f"Description of '{selected_column}'")
    st.write(data[selected_column].describe())
    # Display correlation
    st.subheader("Correlation Matrix:")
    #st.write(data.corr())
    corr = data.corr(numeric_only=True)
    #st.write(data[corr].corr())
    # Plot the heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    plt.title("Correlation Matrix Heatmap")
    st.pyplot(fig)
elif page == 'Summary numerical':
    st.header('numerical data Analysis')
    st.write("Explore the dataset and gain insights into population Demographic and Health information.")
    # Display basic statistics
    st.subheader("Basic statistics for Age:")
    #st.dataframe(data.describe())
    st.dataframe(data['current age'].describe())
    st.dataframe(data['current age'].shape)

    st.subheader("Basic statistics for family size:")
    st.dataframe(data['number of household members (total listed)'].describe())
    st.dataframe(data['number of household members (total listed)'].shape)

    st.subheader("Basic statistics for age of the head of the family:")
    st.dataframe(data['age of household head'].describe())
    st.dataframe(data['age of household head'].shape)

    st.subheader("Basic statistics for the number of the famiy birth:")
    st.dataframe(data['total children ever born'].describe())
    st.dataframe(data['total children ever born'].shape)

    st.subheader("Basic statistics for the number of the famiy surviving birth:")
    st.dataframe(data['number of living children'].describe())
    st.dataframe(data['number of living children'].shape)

    st.subheader("Basic statistics for the ideal number of children per family:")
    st.dataframe(data['ideal number of children'].describe())
    st.dataframe(data['ideal number of children'].shape)

    st.subheader("Basic statistics for age of circumcision:")
    st.dataframe(data['age at circumcision'].describe())
    st.dataframe(data['age at circumcision'].shape)

elif page == 'Visualization':
    st.header('Visualization')
    st.write("Visualize the data to understand trends and patterns.")
    # Add your plots here later

    # Filter numeric columns for plotting
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns

    # Let user select a column
    selected_column = st.selectbox("Select a numeric column to plot", numeric_columns)

    # Plotting the selected column as a histogram
    st.subheader(f"Histogram of '{selected_column}'")

    fig, ax = plt.subplots()
    ax.hist(data[selected_column], bins=20, color='skyblue', edgecolor='black')
    ax.set_xlabel(selected_column)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
    #st.write(data[selected_column].describe())
    #st.write(f"Summary Statistics of {data[selected_column].describe()}'")
    st.write(f"Summary Statistics for {selected_column} Variable: {data[selected_column].describe()}'")
    # Draw boxplot
    st.subheader(f"Boxplot of '{selected_column}'")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data[selected_column], ax=ax)
    plt.title(f"'{selected_column}'Boxplot")
    st.pyplot(fig)

else:
    st.write("Please select a valid page from the sidebar.")

