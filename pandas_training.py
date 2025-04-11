# Title:
# Python: Pandas Basics - Training

# Guiding Videos: https://www.youtube.com/@AlexTheAnalyst/videos

# Data Files: https://github.com/AlexTheAnalyst/PandasYouTubeSeries


# Description:
# This Python code is for training purposes. It is based on the YouTube video lessons of "Alex The Analyst".
# This Python code should be run in interactive mode (VS Code - Jupyter Interactive Window / Jupyter Notebook / ...).

# Contents:
# 1. Read the data from a CSV file & Create a DataFrame
# 2. Filtering and Ordering
# 3. Indexing
# 4. Group by & Aggregation
# 5. Merge, Join and Concatenate the DataFrames
# 6. Visualizations


# First, Import the required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.show_versions()  # show versions of OS, machine, Python, packages etc.


# 1. Read the data from a CSV file & Create a DataFrame
# Guiding Video: https://www.youtube.com/watch?v=dUpyC40cF6Q

df = pd.read_csv(r"M:\Pandas\Countries_of_the_World.csv")
df

pd.set_option("display.max.rows", 300)

df.info()
df.shape  # tuple: (number of rows, # of columns)
df.shape[0]  # number of rows
df.columns
df.describe()
df.head(10)
df.tail(10)

df["Country"].head(10)  # Output - simple text, with index
df[["Country"]].head(10)  # Output - formatted, with index
df[["Country"]].head(10).style.hide()  # Output - formatted, without index

df.loc[0:9, "Country"]
df.loc[0:9, ["Country", "Region"]]
df.loc[218]
df.iloc[218]


# 2. Filtering and Ordering
# Guiding Video: https://www.youtube.com/watch?v=kB7FV-ijdqE

df = pd.read_csv(r"M:\Pandas\World_population.csv")
df.info()

df[df["Rank"] <= 10]

sel_countries = ["Bangladesh", "Brazil"]
df[df["Country"].isin(sel_countries)]

df[df["Country"].str.contains("United", case=False, regex=False)]

# Set index to the "Country" column --> df2 DataFrame
df2 = df.set_index("Country")
df2

df2.filter(like="United", axis=0)
df2.filter(items=["Continent", "CCA3"], axis=1)
df2.filter(items=["Zimbabwe"], axis=0)
df2.loc["United States"]
df2.iloc[8]

df[df["Rank"] <= 10].sort_values(by="Rank", ascending=False)
df[df["Rank"] <= 10].sort_values(by="Rank", ascending=True)
df[df["Rank"] <= 10].sort_values(by=["Continent", "Country"], ascending=[True, False])
df[df["Rank"] <= 10].sort_values(by=["Continent", "Country"], ascending=[True, True])
df[df["Rank"] <= 20].sort_values(by=["Continent", "2022 Population"], ascending=[True, False])


# 3. Indexing
# Guiding Video: https://www.youtube.com/watch?v=mBCG9J1TVTc

df = pd.read_csv(r"M:\Pandas\World_population.csv", index_col="Country")
df.info()
df
df.reset_index(inplace=True)
df.set_index("Country", inplace=True)

df.loc["Argentina"]
df.iloc[8]  # result: Argentina

df.set_index(["Continent", "Country"], inplace=True)
df.sort_index(inplace=True, ascending=True)
df.loc["Europe"]
df.loc["Europe", "Germany"]
df.iloc[8]  # result: Africa, Central African Republic


# 4. Group by & Aggregation
# Guiding Video: https://www.youtube.com/watch?v=VRmXto2YA2I

df_fl = pd.read_csv(r"M:\Pandas\Flavors.csv")
df_fl.info()
df_fl

df_fl.groupby("Base Flavor")
df_fl.groupby("Base Flavor").mean("Flavor Rating")
df_fl.groupby("Base Flavor").sum()
df_fl.groupby("Base Flavor").count()
df_fl.groupby("Base Flavor").max()
df_fl.groupby("Base Flavor").min()
df_fl.groupby("Base Flavor").size()

df_fl.groupby("Base Flavor").agg({"Flavor Rating": ["mean", "sum", "count", "max", "min"]})

df_fl.groupby("Base Flavor").agg(
    {
        "Flavor Rating": ["mean", "sum", "count", "max", "min"],
        "Texture Rating": ["mean", "sum", "count", "max", "min"],
    }
)

df_fl.groupby(["Base Flavor", "Liked"]).mean("Flavor Rating")

df_fl.groupby(["Base Flavor", "Liked"]).agg({"Flavor Rating": ["mean", "sum", "count", "max", "min"]})

df_fl.groupby(["Base Flavor", "Liked"]).agg(
    {
        "Flavor Rating": ["mean", "sum", "count", "max", "min"],
        "Texture Rating": ["mean", "sum", "count", "max", "min"],
    }
)

df_fl.groupby(["Base Flavor", "Liked"]).describe()


# 5. Merge, Join and Concatenate the DataFrames
# Guiding Video: https://www.youtube.com/watch?v=TPivN7tpdwc

df1 = pd.read_csv(r"M:\Pandas\LOTR.csv")
df2 = pd.read_csv(r"M:\Pandas\LOTR_2.csv")
df1
df2

df1.merge(df2)
df1.merge(df2, on="FellowshipID", how="inner")
df1.merge(df2, on=["FellowshipID", "FirstName"], how="inner")

df1.merge(df2, how="outer")
df1.merge(df2, how="left")
df1.merge(df2, how="right")

df1.join(df2, on="FellowshipID", how="outer", lsuffix="_1", rsuffix="_2")

df3 = df1.set_index("FellowshipID").join(df2.set_index("FellowshipID"), how="outer", lsuffix="_1", rsuffix="_2")
df3

pd.concat([df1, df2], axis=0)
pd.concat([df1, df2], join="inner", axis=0)
pd.concat([df1, df2], join="outer", axis=0)
pd.concat([df1, df2], join="outer", axis=1)


# 6. Visualizations
# Guiding Video: https://www.youtube.com/watch?v=JpSMse3eVVg

df = pd.read_csv(r"M:\Pandas\Ice_Cream_Ratings.csv")
df
df.set_index("Date", inplace=True)

df.plot()
df.plot(kind="line")
df.plot(kind="line", subplots=True)
df.plot(kind="line", title="Ice Cream Ratings", xlabel="Daily Ratings", ylabel="Scores")

df.plot(kind="bar")
df.plot(kind="bar", stacked=True)

df.plot(kind="barh")
df.plot(kind="barh", stacked=True)

df["Flavor Rating"].plot(kind="bar")
df["Flavor Rating"].plot(kind="bar", color="red")
df["Flavor Rating"].plot(kind="bar", color="red", alpha=0.5)
df["Flavor Rating"].plot(kind="barh", color="red", alpha=0.5)

df.plot(kind="scatter", x="Flavor Rating", y="Texture Rating", s=500)

df.plot(kind="scatter", x="Flavor Rating", y="Texture Rating", s=500, c="Overall Rating")

df.plot(
    kind="scatter",
    x="Flavor Rating",
    y="Texture Rating",
    s=500,
    c="Overall Rating",
    cmap="coolwarm",
)

df.plot(
    kind="scatter",
    x="Flavor Rating",
    y="Texture Rating",
    s=500,
    c="Overall Rating",
    cmap="viridis",
)

df.plot(
    kind="scatter",
    x="Flavor Rating",
    y="Texture Rating",
    s=500,
    c="Overall Rating",
    cmap="plasma",
)

df.plot(kind="hist")  # shows the distribution of the data
df.plot(kind="hist", bins=20)

df.plot(kind="box")
df.plot(kind="box", grid=True)
df.plot(kind="box", vert=False)

df.plot(kind="area")
df.plot(kind="area", figsize=(10, 5))

df.plot(kind="pie", y="Flavor Rating")

plt.style.available
plt.style.use("ggplot")


# Other Suggestions #1:
# df.index = pd.to_datetime(df.index)
# df.index = pd.to_datetime(df.index, format="%m/%d/%Y")
# df.index = pd.to_numeric(df["Flavor Rating"])

# Other Suggestions #2:
plt.show()

np.random.seed(0)
df = pd.DataFrame(np.random.randn(1000, 2), columns=["A", "B"])
df["B"] = df["B"] + np.arange(1000)
df.plot(kind="hexbin", x="A", y="B", gridsize=20)
