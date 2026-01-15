import pandas as pd
import os



BASE_DIR = os.getcwd() + "\\api_data_aadhar_demographic\\"
data_files = ["api_data_aadhar_demographic_0_500000.csv",
                "api_data_aadhar_demographic_500000_1000000.csv",
                "api_data_aadhar_demographic_1000000_1500000.csv",
                "api_data_aadhar_demographic_1500000_2000000.csv",
                "api_data_aadhar_demographic_2000000_2071700.csv",
            ]
df = pd.DataFrame()
for FILE_NAME in data_files:
    df1 = pd.read_csv(BASE_DIR+FILE_NAME)
    df = pd.concat([df,df1])

# print(df.shape)       # size of data frame is returned
del df1
# non_state = ["100000","BALANAGAR","Darbhanga","Madanapalle","Puttenahalli","Raja Annamalai Puram"]

# Dropping all the unwanted datas
df.drop(df[df['state'] == "100000"].index,inplace=True,axis=0)
df.drop(df[df['state'] == "BALANAGAR"].index,inplace=True,axis=0)
df.drop(df[df['state'] == "Darbhanga"].index,inplace=True,axis=0)
df.drop(df[df['state'] == "Nagpur"].index,inplace=True,axis=0)
df.drop(df[df['state'] == "Jaipur"].index,inplace=True,axis=0)
df.drop(df[df['state'] == "Madanapalle"].index,inplace=True,axis=0)
df.drop(df[df['state'] == "Puttenahalli"].index,inplace=True,axis=0)
df.drop(df[df['state'] == "Raja Annamalai Puram"].index,inplace=True,axis=0)

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

    target_state = {
        "Andaman & Nicobar Islands" : "Andman and Nicobar Islands",
        "Andaman And Nicobar Islands" : "Andman and Nicobar Islands",
        "andhra pradesh" : "Andhra Pradesh",
        "Chhatisgarh" : "Chhattisgarh",
        "Dadra & Nagar Haveli" : "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra and Nagar Haveli" : "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra And Nagar Haveli" : "Dadra and Nagar Haveli and Daman and Diu",
        "Dadra And Nagar Haveli And Daman And Diu" : "Dadra and Nagar Haveli and Daman and Diu",
        "Daman & Diu" : "Dadra and Nagar Haveli and Daman and Diu",
        "Daman and Diu" : "Dadra and Nagar Haveli and Daman and Diu",
        "Daman And Diu" : "Dadra and Nagar Haveli and Daman and Diu",
        "Jammu & Kashmir" : "Jammu and Kashmir",
        "Jammu And Kashmir" : "Jammu and Kashmir",
        "ODISHA" : "Odisha",
        "odisha" : "Odisha",
        "Orissa" : "Odisha",
        "Pondicherry" : "Puducherry",
        "Uttaranchal" : "Uttrakhand",
        "WEST BENGAL" : "West Bengal",
        "WESTBENGAL" : "West Bengal",
        "West Bangal" : "West Bengal",
        "West Bengli" : "West Bengal",
        "West bengal" : "West Bengal",
        "West  Bengal" : "West Bengal",
        "Westbengal" : "West Bengal",
        "westbengal" : "West Bengal",
        "Uttarakhand" : "Uttrakhand",
    }

    return target_state.get(state, state)


df['state'] = df['state'].apply(clean_state_name)

print(df['state'].nunique())
print(df['state'].unique())

# for names in target_state.keys():
#     df.replace({'state':names},target_state[names])

# ls = list(df['state'].unique())
# ls.sort()
# print(ls)
# print(df[df['state'] == 'BALANAGAR'].shape)
# print(df['district'].nunique())
# print(df.to_string())