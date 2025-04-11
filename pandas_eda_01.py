# Title: Pandas - EDA
# Description: This script demonstrates EDA using Pandas
# Dataset: [link]
# Guiding Video: https://www.youtube.com/watch?v=Liv6eeb1VfE

# This Python code is for training purposes. It is based on the YouTube video lessons of "Alex The Analyst".
# This Python code should be run in interactive mode (VS Code - Jupyter Interactive Window / Jupyter Notebook / ...).

# This code was not copied from any source.
# To improve the training and learning process, it was created from scratch, based on the guiding video.
# It also includes some changes and improvements, compared to the guiding video and due to continuous changes of the Pandas package.
# etc.
# Other changes and improvements:
# - also suggested by GitHub Copilot & ChatGPT, as well as
# - found at https://stackoverflow.com and in Python & Pandas documentation


# Import the required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Settings for the DataFrame output
# Display all rows of the DataFrame
pd.set_option("display.max.rows", 300)

# Set the 'float' format for the DataFrame output (thousands separator & 2 decimal places)
pd.set_option("display.float_format", "{:,.2f}".format)


# Initial steps
# Read the data from a CSV file & Create a DataFrame
df = pd.read_csv(r"M:\Pandas\World_population.csv")
df
df.info()
df.describe()

df.isnull().sum()  # Check for missing values
df.nunique()  # Check for unique values in each column


# List the unique values in the "Continent" column
continent_list = df["Continent"].unique()
continent_list.sort()
continent_list


# Calculate & Visualize the correlation matrix
df.corr(numeric_only=True)

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=0.5)
plt.show()


# Step 1: Sort the DataFrame by the "2022 Population" column in descending order, display the first / last 10 rows
df.sort_values(by="2022 Population", ascending=False).head(10)
df.sort_values(by="2022 Population", ascending=False).tail(10)


# Step 2: Group the DataFrame by the "Continent" column
df.groupby("Continent").mean(numeric_only=True).sort_values(by="2022 Population", ascending=False)
df.groupby("Continent")["2022 Population"].sum().sort_values(ascending=False)


# Step 3: Filter the DataFrame to show only the countries from the "Oceania" continent,
# sort by the "2022 Population" column in descending order & display top 10
df[df["Continent"] == "Oceania"].sort_values(by="2022 Population", ascending=False).head(10)


# Step 4: Sort the DataFrame by the "Continent" and "2022 Population" columns
dfs = df.sort_values(by=["Continent", "2022 Population"], ascending=[True, False])
dfs

# Create a new column "Rank Continent" with the rank of the "2022 Population" values for each continent
dfs.insert(1, "Rank Continent", dfs.groupby("Continent")["2022 Population"].rank(ascending=False, method="first", na_option="bottom"))
dfs["Rank Continent"] = dfs["Rank Continent"].astype(int, errors="ignore")  # Convert the column to integer
dfs.rename(columns={"Rank": "Rank Global"}, inplace=True)  # Rename the "Rank" column to "Rank Global"
dfs.reset_index(drop=True, inplace=True)  # Reset the index of this DataFrame
dfs.info()

# Create a new Dataframe containing the top 5 countries of "2022 Population" for each Continent
dfs_cont_top5 = dfs[["Rank Global", "Rank Continent", "Continent", "Country", "2022 Population"]].groupby("Continent").head(5)
dfs_cont_top5["2022 Population"] = dfs_cont_top5["2022 Population"].apply(lambda x: f"{x:,.0f}")  # Format the population values
dfs_cont_top5.reset_index(drop=True, inplace=True)
dfs_cont_top5


# Step 5: Visualize the average country population for the period 1970 - 2022, grouped by the "Continent" column
df2 = df.groupby("Continent")[df.columns[5:13]].mean(numeric_only=True).sort_values(by="2022 Population", ascending=False)
df2.columns = df2.columns.str.replace(" Population", "")  # Remove the "Population" word from the column names
df2 = df2[df2.columns[::-1]].T  # Reverse the column order & Transpose the DataFrame --> .T or .transpose()
df2
df2.plot(title="Average Country Population by Continent (1970 - 2022)")


# Step 6: Boxplot
df.boxplot()
df.boxplot(column="2022 Population", by="Continent")


# Step 7: dtypes
df.dtypes
df.select_dtypes(include="object")
df.select_dtypes(include="number")
df.select_dtypes(include="float64")
df.select_dtypes(include="int64")
df.select_dtypes(include=["int64", "object"])


# Additional Possible Steps:

# Step A1: Filter the DataFrame to show only the countries with a population greater than 100 million,
# sort by the "2022 Population" column in descending order
# df[df["2022 Population"] > 100_000_000].sort_values(by="2022 Population", ascending=False)


# Step A2: Change the data type of the "2022 Population" column to integer
# df["2022 Population"] = df["2022 Population"].fillna(0)  # Fill missing values with 0
# df["2022 Population"] = df["2022 Population"].astype(int)


# Step A3: Format the DataFrame output
# dff = df.style.highlight_null(color="grey")
# dff = df.style.set_properties(**{"background-color": "black", "color": "lawngreen", "border": "1px solid white"})

# df.style.format(na_rep="missing", thousands=",", precision=0)

# formatted_df = df.style.format(na_rep="missing", thousands=",", precision=0)
# df.style.format(na_rep="missing", thousands=",", precision=0, subset=["2022 Population"])
