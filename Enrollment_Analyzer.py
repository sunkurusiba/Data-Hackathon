import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re
enroll_1 = pd.read_csv("D:\\dataset\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment_0_500000.csv")
enroll_2 = pd.read_csv("D:\\dataset\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment_500000_1000000.csv")
enroll_3 = pd.read_csv("D:\\dataset\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment\\api_data_aadhar_enrolment_1000000_1006029.csv")
df=pd.concat([enroll_1,enroll_2,enroll_3],axis=0,ignore_index=True)
# print(df.shape)
# print(df["state"].nunique())
# print(df["state"].unique())
df.drop(df[df['state'] == "100000"].index,inplace=True,axis=0)
def clean_state_name(state):
    # Handle missing values
    if not isinstance(state, str):
        return "Unknown"

    # Step A: Standardize Casing & Whitespace
    # .strip() removes spaces at start/end
    # .title() converts "andhra pradesh" -> "Andhra Pradesh"
    state = state.strip().title()

    # Step B: Fix specific typos and legacy names using a Dictionary
    # This maps 'Incorrect Name' : 'Correct Name'

    dicti = {  # Odisha
        "Orissa": "Odisha",
        "ODISHA": "Odisha",

        "Jammu And Kashmir": "Jammu and Kashmir",
        "Jammu & Kashmir": "Jammu and Kashmir",

        "Pondicherry": "Puducherry",

        "Andaman & Nicobar Islands": "Andaman and Nicobar Islands",
        "Andaman And Nicobar Islands": "Andaman and Nicobar Islands",

        "andhra pradesh ": "Andhra Pradesh",
        # West Bengal
        "WEST BENGAL": "West Bengal",
        "West Bangal": "West Bengal",
        "Westbengal": "West Bengal",
        "West bengal": "West Bengal",
        "WESTBENGAL": "West Bengal",
        "West  Bengal": "West Bengal",

        # Dadra and Nagar Haveli and Daman and Diu
        "The Dadra And Nagar Haveli And Daman And Diu": "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra & Nagar Haveli": "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra and Nagar Haveli": "Dadra and Nagar Haveli and Daman and Diu",
        "Daman and Diu": "Dadra and Nagar Haveli and Daman and Diu",
        "Daman & Diu": "Dadra and Nagar Haveli and Daman and Diu",
        "Daman And Diu": "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra And Nagar Haveli": "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra And Nagar Haveli And Daman And Diu": "Dadra and Nagar Haveli and Daman and Diu",
    }

    # # Return the corrected name if it exists in our dictionary, else return the standardized name
    return dicti.get(state, state)

# 3. Apply the function to the 'state' column
df['state'] = df['state'].apply(clean_state_name)

# 4. Verify the results
print("Unique States after cleaning:")
print(df['state'].unique())
print(df['state'].nunique())
