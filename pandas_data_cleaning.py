# Title: Pandas - Data Cleaning
# Description: This script demonstrates how to clean data using Pandas
# Dataset: [link]
# Guiding Video: https://www.youtube.com/watch?v=bDhvCp3_lYw

# This Python code is for training purposes. It is based on the YouTube video lessons of "Alex The Analyst".
# This Python code should be run in interactive mode (VS Code - Jupyter Interactive Window / Jupyter Notebook / ...).

# This code was not copied from any source.
# To improve the training and learning process, it was created from scratch, based on the guiding video.
# It also includes some changes and improvements, compared to the guiding video and due to continuous changes of the Pandas package.
# etc.
# Other changes and improvements:
# - also suggested by GitHub Copilot & ChatGPT, as well as
# - found at https://stackoverflow.com and in Python & Pandas documentation

import pandas as pd

df = pd.read_excel(r"M:\Pandas\Customer_Call_List.xlsx")
df
df.info()


# Step 1: Remove the duplicate rows
df = df.drop_duplicates()  # So easy!


# Step 2: Remove the "Not_Useful_Column"
df = df.drop(columns=["Not_Useful_Column"])


# Step 3: Column "Last_Name" - Remove the special characters at the beginning and/or end of the string
df["Last_Name"] = df["Last_Name"].str.strip("./_")


# Step 4: Column "Phone_Number" - Format the phone numbers to the standard format "123-456-7890"

# Step 4 - Variant 1: Using a custom function


def fn_format_phone_num(phone):
    if pd.isna(phone):
        return None

    digits = "".join(filter(str.isdigit, str(phone).strip()))  # Extract only the digits from the string

    if len(digits) == 10:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"

    return "Invalid"


df.insert(4, "Ph_Num_f1", df["Phone_Number"].apply(fn_format_phone_num))


# Step 4 - Variant 2: Using Pandas built-in methods / functions and RegEx

# Remove all non-numeric characters from the string and then format the phone numbers
df.insert(5, "Ph_Num_f2", df["Phone_Number"].astype(str).str.replace("[^0-9]", "", regex=True))
df["Ph_Num_f2"] = df["Ph_Num_f2"].str.replace(r"(\d{3})(\d{3})(\d{4})", r"\1-\2-\3", regex=True)

# Display the final results for both Variants 1 & 2
df[["CustomerID", "Phone_Number", "Ph_Num_f1", "Ph_Num_f2"]]


# Step 5: Column "Address" - split the address values into new columns "Street", "State_or_County", "Zip"
df[["Street", "State_or_County", "Zip"]] = df["Address"].str.split(",", n=2, expand=True)
# The original column "Address" can be now removed
df = df.drop(columns=["Address"])


# Step 6: Column "Paying Customer" - unify the values to "Y" or "N"
df.rename(columns={"Paying Customer": "Paying_Customer"}, inplace=True)
df["Paying_Customer"].unique()
df["Paying_Customer"] = df["Paying_Customer"].replace({"Yes": "Y", "No": "N", "N/a": ""})
# or: Convert to Boolean values
# df["Paying_Customer"] = df["Paying_Customer"].replace({"Y": True, "N": False})
# df["Paying_Customer"] = df["Paying_Customer"].astype(bool)


# Step 7: Column "Do_Not_Contact" - unify the values to "Y" or "N"
df["Do_Not_Contact"].unique()
df["Do_Not_Contact"] = df["Do_Not_Contact"].replace({"Yes": "Y", "No": "N"})


# Step 8: DataFrame - Fill NA/NaN/None values with an empty string
df = df.fillna("")


# Step 9: Column "Do_Not_Contact" - Remove the rows with the value "Y"
df = df[df["Do_Not_Contact"] != "Y"]


# Step 10: Column "Phone_Number" - Remove the rows with empty values
df = df[df["Phone_Number"] != ""]
# or: df = df[df["Phone_Number"].notnull()]
# or: df = df.dropna(subset=["Phone_Number"], inplace=True)


# Step 11: Reset the index
df.reset_index(drop=True, inplace=True)


df
df.info()


# Save the cleaned DataFrame to a new Excel file
df.to_excel(r"M:\Pandas\Customer_Call_List_Cleaned.xlsx", index=False)
