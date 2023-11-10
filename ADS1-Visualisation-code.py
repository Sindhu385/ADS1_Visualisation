

# imported the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the Csv file into dataFrame
df = pd.read_csv(r"C:\Users\sindh\OneDrive\Desktop\Applied Data Science1\
                 P_Data_Extract_From_Worldwide_Governance_Indicators\
                     Worldwide_governance_Series - Metadata.csv", 
                     index_col = 0) 
print(df)

#Function to create lineplot
def worldgoverence_lineplot(line):
    sns.set_style('whitegrid')
    line.plot(x = 'year', y = ['Algeria', 'Albania', 'Australia', 'Belgium', 
                           'Finland', 'India', 'New Zealand', 'United Kingdom', 
                           'United States'], figsize = (16, 6), marker='o')
# adds title and labels for the figure
    plt.title('Worldwide Governance')
    plt.xlabel('year')
    plt.ylabel('Percentile Rank')
# display legend at the top right corner
    plt.legend(loc = 'upper right')
# sets the limits of the x-axis and y-axis
    plt.xlim(2012, 2024)
    plt.ylim(10, 120)


# Function to create barplot
def worldgoverence_barplot(barplot):
    barplot.plot(x = 'year', y = ['India', 'United Kingdom'], kind = 'bar',
                 title = 'Comparing India and UK',
                 xlabel = 'years', ylabel = 'Percentile Rank', 
                 color = ('Orange', 'blue'))# Adds kind,title,labels and color
    plt.legend(loc = 'upper right')
    plt.figure(figsize = (16, 6))
    plt.show()


# Function to create piechart
def worldgoverence_piechart(df, year, figsize = (4, 5), fontsize = 10,
                            autopct = '%1.0f%%'):
    label = ['American Samoa', 'Algeria', 'Albania', 'Australia', 'Belgium',
             'Finland', 'India', 'New Zealand', 'United Kingdom', 
             'United States']
    plt.figure(figsize = figsize)

    plt.pie(df[str(year)], autopct=autopct, labels = label)
    plt.title(f'World Goverence in {year}', fontsize = fontsize)
    plt.show()

#deleting the rows which has NaN values
df1 = df.iloc[:-7] 

 



#deleting the columns and returning only the columns we need
df2 = df1.drop(["Country Code", "Series Name", "Series Code"], axis = 1)



#changing the column name
df3 = df2.rename(columns = {'2013 [YR2013]': '2013', '2014 [YR2014]': '2014',
                          '2015 [YR2015]': '2015', '2016 [YR2016]': '2016',
                          '2017 [YR2017]': '2017', '2018 [YR2018]': '2018', 
                          '2019 [YR2019]': '2019', '2020 [YR2020]': '2020',
                          '2021 [YR2021]': '2021', '2022 [YR2022]': '2022'})



# To transpose the dataframe df3 and converts its rows and columns
# astype(float) it converts the entire transposed data into float type
df4 = df3.transpose().astype(float)



df5 = df4.round(2)  # rounding up the value to 2 for better understanding


df6 = df5.reset_index(drop = True)  # reset the index with drop=True
print(df6)

# Adding the extra column as year for better understanding
year = pd.Series([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
df6['year'] = year


#changing the last column year as the first column
df7 = pd.concat([df6.iloc[:, -1:], df6.iloc[:, :-1]], axis = 1)





worldgoverence_lineplot(df6)

worldgoverence_barplot(df6)

worldgoverence_piechart(df3, 2013)
worldgoverence_piechart(df3, 2022)
