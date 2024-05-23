#imporing pandas
import pandas as pd
 
#Importing dataset
df = pd.read_csv('03. [DAZONE2024] DATASET.csv')
 
#Size of original dataset
print(df.shape)
print(df.isnull().sum())

# Step 1: Calculate the number of NaN values in each row
nan_counts = df.isna().sum(axis=1)

# Step 2: Filter out rows that have less than 10 NaN values
df_filtered = df[nan_counts < 10]

# Step 3: Save the filtered DataFrame to a new CSV file
df_filtered.to_csv('filtered_dataframe.csv', index=False)
print(df_filtered.shape)
