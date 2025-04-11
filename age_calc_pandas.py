# Title: Calculate the age from a sample Pandas DataFrame with birth dates

import pandas as pd
import numpy as np
from datetime import datetime

# Sample DataFrame with birth dates, as of "2025-03-10"
data = {
    "Name": [
        "Alice",
        "John",
        "Charlie",
        "1940_Day_m1",
        "1940_Day_00",
        "1940_Day_p1",
        "Date_Future",
        "Date_Incorrect",
        "Date_None",
        "Date_Yesterday",
        "Date_Today",
        "Date_Tomorrow",
    ],
    "Birthdate": [
        "1990-01-01",
        "1940-10-30",
        "2000-07-23",
        "1940-03-09",
        "1940-03-10",
        "1940-03-11",
        "2042-07-07",
        "20XX-11-11",
        None,
        "2025-03-09",
        "2025-03-10",
        "2025-03-11",
    ],
}
df = pd.DataFrame(data)

# Convert Birthdate column to datetime, Dtype: datetime64[ns]
df["Birthdate"] = pd.to_datetime(df["Birthdate"], errors="coerce")  # Invalid dates become NaT

today = datetime.today()


# Method Nr. 1: "Classical" approach
# **********************************


# Function to calculate age
def calculate_age(birthdate):
    if today < birthdate:
        return None
    else:
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age


# Apply the function 'calculate_age()' to the Birthdate column
df["Age"] = df["Birthdate"].apply(calculate_age)  #  Dtype: float64


# Method Nr. 2: Age - as float
# ****************************

df["Age float"] = (today - df["Birthdate"]).dt.days / 365.2425  #  Dtype: float64;  Diff. of 1 day = 0.0027379 of year
df["Age float"] = df["Age float"].mask(df["Age float"].lt(0), None)

# Age - floor from float, using numpy function
df["Age np_floor"] = df["Age float"].apply(np.floor)  #  Dtype: float64

# Note: If all "Age float" values are numbers, then df["Age float"].astype(int) can be applied,
# or it can be done after filling the invalid / missing values "NaN" with "0"
df["Age int"] = df["Age float"].fillna(0).astype(int)  #  Dtype: int64

df["Age NaN"] = "False"  #  Dtype: object
df["Age NaN"] = df["Age NaN"].mask(df["Age float"].isna(), "True")

df
df.info()


# ************************************************************************************

# This was added later for training purposes only...

# Random order of the DataFrame rows
df.sample(frac=1)

# Shuffle values in one column of the DataFrame
df["Name"] = df["Name"].sample(frac=1).reset_index(drop=True)
# or:
df["Name"] = df["Name"].sample(frac=1).values
